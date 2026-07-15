# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import random
from deep_translator import GoogleTranslator
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from bd.schedule import select_data_schedule
from bd.salles_disponibles import select_data_salles
from bd.orientation_batiment import select_data_orientation
from bd.texter_prof import select_data_send_message
from bd.meteo import select_data_meteo
from actions.ollama_service import ask_ollama
from rasa_sdk.events import EventType
from rasa_sdk.events import SlotSet

# ---------------------------------------------------------------------------------

class ActionConsulterOllama(Action):

    def name(self) -> Text:
        return "action_consulter_ollama"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action consulter ollama")
        # Get the professor's name from the slot
        question = tracker.get_slot("question")

        response = ask_ollama(question)
        if response:
            print("Données récupérées: ", response)
            result = format(response)
            dispatcher.utter_message(text = result)
        else:
            print("Erreur de Ollama")
            dispatcher.utter_message(text = "Désolé, Ollama n'a pas répondu!")

        return [SlotSet("question", None)]


# ---------------------------------------------------------------------------------
class ActionTranslate(Action):
    def name(self):
        return "action_translate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        phrase = tracker.get_slot("phrase")
        print("pharase: ", phrase)
        target_langue = tracker.get_slot("target_langue")
        print("target: ", target_langue)
        if not phrase:
            dispatcher.utter_message("Je n'ai pas trouvé de phrase à traduire.")
            return [SlotSet("phrase", None), SlotSet("target_langue", None)]

        traduction = ""

        if target_langue == "anglais":
            traduction += GoogleTranslator(source="fr", target="en").translate(phrase)
            print("traduction anglais : ", traduction)

        if target_langue == "arabe":
            traduction += GoogleTranslator(source="fr", target="ar").translate(phrase)
            print("traduction arabe : ", traduction)

        dispatcher.utter_message(f"La traduction est : {traduction}")

        return [SlotSet("phrase", None), SlotSet("target_langue", None)]

# -----------------------------------------------------------------------------------

class ActionConsulterEdt(Action):

    def name(self) -> Text:
        return "action_consulter_edt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("action consulter edt")


        section = tracker.get_slot("section")
        print("section: ", section)
        groupe = tracker.get_slot("groupe")
        print("groupe: ", groupe)
        date = tracker.get_slot("date")
        print("date: ", date)


        emploi_du_temps = select_data_schedule(section, groupe, date)
        if emploi_du_temps:
            print("Données récupérées: ", emploi_du_temps)
            result = format(emploi_du_temps)
            dispatcher.utter_message(text = result)
        else:
            dispatcher.utter_message(text = "Désolé, aucune donnée n'a été trouvé pour les informations fournies.")

        print("reset success")
        return [SlotSet("section", None), SlotSet("groupe", None), SlotSet("date", None)]


class ActionSallesLibres(Action):

    def name(self) -> Text:
        return "action_salles_libres"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Action consulter libres salles")
        print("")
        heure = tracker.get_slot("heure_salle")
        print("heure: ", heure)
        print("")

        reponse_db = select_data_salles(heure)
        if reponse_db:
            result = format(reponse_db)
            print("result : ", result)
            dispatcher.utter_message(text = result)
        else:
            dispatcher.utter_message(text = "Désolé, aucune donnée n'a été trouvé pour les informations fournies.")

        return [SlotSet("heure_salle", None)]


class ActionOrienterBatiment(Action):

    def name(self) -> Text:
        return "action_orienter_batiment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Action consulter orienter")
        print("")
        place = tracker.get_slot("place")
        print("place: ", place)
        print("")

        try:
            select_place = select_data_orientation(place)
            if select_place:
                result = format(select_place)
                print("result : ", result)
                dispatcher.utter_message(text = result)
            else:
                dispatcher.utter_message(text=f"Salle {place} pas trouvée!\n")
        except Exception as e:
            print("Error during database operation: ", str(e))
            dispatcher.utter_message(text="Désolé, une erreur s'est produite lors de la recherche dans la base de données.")

        print("reset success")
        return [SlotSet("place", None)]


# Define the action
class ActionTexterProf(Action):
    def name(self) -> Text:
        return "action_texter_prof"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        print("Action consulter texter prof")

        nom_prof = tracker.get_slot("nom_prof_tp")
        print("nom_prof_tp : ", nom_prof)

        try:
            email = select_data_send_message(nom_prof)
            if email:
                dispatcher.utter_message(json_message={"text": f"L'email de {nom_prof} est :\n",
                                                       "email": f"{email}"})
            else:
                dispatcher.utter_message(text=f"Aucune adresse email trouvée pour {nom_prof}.\n")
        except Exception as e:
            print("Error during database operation: ", str(e))
            dispatcher.utter_message(text="Désolé, une erreur s'est produite lors de la recherche dans la base de données.")

        # Reset the slot
        return [SlotSet("nom_prof_tp", None)]


class ActionConsulterMeteo(Action):

    def name(self) -> Text:
        return "action_consulter_meteo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Action consulter meteo")
        print("")
        moment = tracker.get_slot("moment")
        print("date : ", moment)
        print("")

        valid_moments = ["cet instant", "nuit", "soir", "matinée", "matin", "minuit", "cinq heures du matin",
                         "fin d'après-midi", "weekend", "tôt le matin", "pendant le déjeuner", "dix-neuf heures"]
        if moment not in valid_moments:
            print("Aucune donnée n'a été trouvé pour les informations fournis.")
            dispatcher.utter_message(text = "Désolé, aucune donnée n'a été trouvé pour les informations fournies.")

        else:
            select_moment = select_data_meteo(moment)
            if select_moment:
                result = format(select_moment)
                print("result : ", result)
                dispatcher.utter_message(text = result)

        print("reset success")
        return [SlotSet("moment", None)]


questions_de_relance = [
    "Est-ce que tu aimes faire du sport ?",
    "En quelle année d'université es-tu ?",
    "Sur quel site es-tu, comme CERI, Université Centre, Agrosciences ou IUT ?",
    "Quelle est ta nationalité ?",
    "Tu as quel âge?",
    "Comment-tu te sens?"
]


class ActionPoserQuestionReprise(Action):
    def name(self) -> Text:
        return "action_poser_question_reprise"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[EventType]:
        question = random.choice(questions_de_relance)
        dispatcher.utter_message(text = question)
        return []


class ActionWaitUneMinute(Action):
    def name(self) -> Text:
        return "action_wait_une_minute"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> list[
        list[dict[str, Any]]]:
        dispatcher.utter_message(text = "Hmm... tu es toujours là ?")
        return [ActionPoserQuestionReprise().run(dispatcher, tracker, domain)]