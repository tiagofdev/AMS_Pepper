from flask import Flask, request, jsonify, render_template, send_file
import urllib.request
import json
import time
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"), auto_reload=True)
from  flask_socketio import SocketIO, emit
from jinja2 import Template


app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"
url_param = "https://univ-avignon.fr"

# Allow all origins or specify the accepted origin
socketio = SocketIO(app, cors_allowed_origins="*")
@app.route('/')
def index():
    webview()
    return render_template('index.html')

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
    socketio.emit('update_url', {'url_param': url_param})


@app.route("/webview", methods=["GET", "POST"])
def webview():
    global url_param
    return render_template('dynamic_page.html', url_param=url_param, encoding='utf-8')

@app.route('/chat', methods=['POST'])
def chat():
    global url_param
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({
            "replies": ["Bonjour, bienvenue, Que puis-je faire pour vous?"]
        })

    data = json.dumps({"sender": "user", "message": user_message}).encode('utf-8')
    req = urllib.request.Request(RASA_URL, data=data, headers={'Content-Type': 'application/json'})

    try:
        with urllib.request.urlopen(req) as response:
            bot_responses = json.loads(response.read().decode('utf-8'))
            # print("Réponse de Rasa:", bot_responses)
    except Exception as e:
        print("Erreur lors de la requête à Rasa:", e)
        return jsonify({"replies": ["Erreur de connexion avec Rasa."]})

    if bot_responses:
        replies = []
        for resp in bot_responses:
            if "text" in resp:
                replies.append(resp["text"])

            if "custom" in resp:
                if "url" in resp["custom"]:
                    # replies.append(f"Vous pouvez consulter ce lien pour plus d'informations : {resp['custom']['url']}")
                    replies.append(resp['custom']['url'])
                    url_param = resp['custom']['url']
                    # webview()
                    send_url()
                if "text" in resp["custom"]:
                    replies.append(resp['custom']["text"])
                if "email" in resp["custom"]:
                    replies.append(resp['custom']["email"])

        full_response = '\n'.join(replies)
        send_msg(user_message, full_response)
        print("replies: ",full_response)
        return jsonify({"replies": replies})
    else:
        print("pas de réponse de RASA")
        send_msg(user_message, "J'ai pas compris!")
        return jsonify({"replies": ["J'ai pas compris!"]})





@app.route("/experience", methods=["GET", "POST"])
def experience():

    if request.method == 'POST':
        responses = request.form
        return f"Responses received: {responses}"

    return render_template('../../UAPV/AMS_Projet1/questionnaire/questionnaire/experience.html', encoding='utf-8')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
