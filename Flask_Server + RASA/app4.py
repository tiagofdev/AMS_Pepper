# Cette version le web socketIO pour chaque reponse est implementé, actions modifiées pour chercher prof seulement par nom
# implementer d'envoyer le url au pepper

import json
import urllib.request
from jinja2 import Template
import base64
from flask import Flask, request, jsonify, render_template, send_file
import speech_recognition as sr
import wave
from ast import literal_eval
import sqlite3
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"), auto_reload=True)
from  flask_socketio import SocketIO, emit

# Rasa server URL and endpoint
RASA_URL = "http://127.0.0.1:5005/webhooks/rest/webhook"
url_param = "https://univ-avignon.fr"


# Google Speech Recognition
def get_googleSR():
    file_path = './received_audio.wav'
    transcriber = sr.Recognizer()
    audio_file = None
    with sr.AudioFile(file_path) as source:
        audio_file = transcriber.record(source)
    try:
        print("step 2 : Request to Google Speech Recognition.")
        text = transcriber.recognize_google(audio_file, language="fr-FR")
        print("step 3 : Response from Google successful!")
        return text
    except Exception as e:
        print(e)
        print("step 3 : Error Google Speech!")

app = Flask(__name__)
# Allow all origins or specify the accepted origin
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def hello_world():
    webview()
    return "Pepper Flask Server"

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def send_msg(user, rasa_response):
    socketio.emit('update_transcript', {'user': user, 'rasa': rasa_response})

@socketio.on('message')
def send_url():
    global url_param
    socketio.emit('update_url', {'url_param': url_param})

@app.route("/webview", methods=["GET", "POST"])
def webview():
    global url_param
    return render_template('dynamic_page.html', url_param=url_param, encoding='utf-8')

@app.route("/speech_recognition", methods=["POST"])
def speech_recognition():
    print("Step 1 : Request received from Pepper")
    data = request.get_json(force=True)
    # Decode the audio data
    encoded_audio = data['data']
    audio_data = base64.b64decode(encoded_audio)

    # Decode the parameters
    encoded_params = data['params']
    params = base64.b64decode(encoded_params)
    params = literal_eval(params.decode("utf-8"))

    # Save the audio file
    file_path = 'received_audio.wav'
    with wave.open(file_path, "w") as wave_write:
        wave_write.setparams(params)
        wave_write.writeframes(audio_data)


    transcript = get_googleSR()  # Function for speech-to-text

    if transcript is not None:
        print("Step 4 : transcript: " + transcript)
    else:
        print("transcript is None")
        return jsonify({"response_text": "J'ai pas écouté", "response_disposition":"neutre"}),200

    # From here, send the transcript to Rasa
    response_body = comm_rasa(transcript)

    # Convertir la réponse en JSON
    rasa_response = json.loads(response_body)
    print("Step 5 : Response from RASA : ")

    #     --------------------------------------------------------------------------------------
    # Essaie d'envoyer plus7eurs reponses
    global url_param
    if rasa_response:
        response_disposition = "neutre"
        tablet = []
        parler = []
        for resp in rasa_response:
            if "text" in resp:
                parler.append(resp["text"])
                tablet.append(resp["text"])
            if "custom" in resp:
                if "url" in resp["custom"]:
                    # Pepper, pas parler
                    # response_url = resp['custom']['url']
                    url_param = resp['custom']['url']
                    print("URL: ", url_param)
                    tablet.append(url_param)
                    send_url()
                if "disposition" in resp["custom"]:
                    # Pepper, pas parler
                    response_disposition = (f"{resp['custom']['disposition']}")
                if "text" in resp["custom"]:
                    parler.append(resp['custom']["text"])
                    tablet.append(resp['custom']["text"])
                if "email" in resp["custom"]:
                    tablet.append(resp['custom']["email"])
        parler_full = ''.join(parler)
        # parler_full = ''.join(str(item) for item in parler)
        tablet_full = ''.join(tablet)
        # tablet_full = ''.join(str(item) for item in tablet)
        tablet_clean = tablet_full.replace('[', '')

        print("", parler_full)
        print("", tablet_full)
        send_msg(transcript, tablet_full)
        # print(f"disposition: {response_disposition}")
        return jsonify({"response_text": parler_full, "response_disposition": response_disposition}),200
    else:
        print("pas de réponse")
        send_msg(transcript, "Aucune reponse de Rasa")
        return jsonify({"reponse_text": ["Aucune réponse de la part de Rasa."]})



# Communication Rasa Server
def comm_rasa(transcript):

    # Préparation des données en JSON
    data = json.dumps({"sender": "nao", "message": transcript}).encode('utf-8')
    # Crée une requête avec l'URL et les données
    req = urllib.request.Request(RASA_URL, data=data, headers={'Content-Type': 'application/json'})

    # Envoie la requête
    try:
        with urllib.request.urlopen(req) as response:
            response_code = response.getcode()
            response_body = response.read()

        print("Response code: ", response_code)
        # print("Response body: ", response_body)
        return response_body
    except Exception as e:
        print("Erreur lors de la requête à Rasa:", e)
        return jsonify({"reponse_text": ["Erreur de connexion avec Rasa!"]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
