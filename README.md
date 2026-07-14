<img width="445" height="129" alt="image" src="https://github.com/user-attachments/assets/eebf3f50-592e-475b-b85a-3a3101a86515" />

<img width="599" height="1068" alt="image" src="https://github.com/user-attachments/assets/10effeba-8cd9-43ea-ba7b-3cbf327c3daa" />
 

# Projet AMS Robot Pepper
Distributed Behavioral System for robot Pepper

## 1. Contexte et Objectifs du Projet

### 1.1. Contexte

Le projet vise à développer un système interactif et intelligent pour le robot Pepper, afin de créer
une solution d'accueil et de service au CERI (Centre d'Études et de Recherche en Informatique).
Le robot Pepper, équipé de technologies robotiques avancées, sera programmé pour interagir
avec les visiteurs, répondre à des questions et faciliter diverses tâches dans un environnement
professionnel. Ce projet représente un prototype qui répond à la demande croissante pour des
solutions robotiques et des interfaces naturelles, permettant d’améliorer l’expérience utilisateur
tout en optimisant les processus d'accueil.

### 1.1. Objectifs

- **Développement d’un système de comportement** : Développer un ensemble de
comportements spécifiques pour le robot Pepper, afin d’assurer des interactions fluides
et naturelles.

- **Création d’une application serveur** : Développer une application serveur qui permettra de
communiquer avec le robot Pepper, répondant aux requêtes et contrôlant ses actions en
temps réel.

- **Interface graphique** : Fournir une interface graphique pour l’écran intégré du robot, permettant d’afficher des informations pertinentes et d’interagir avec l’utilisateur de manière visuelle. 

- **Connexion à des services externes** : Connecter le système à des services externes, comme une base de données, un service de reconnaissance vocale, un traducteur automatique, et un modèle de conversation RASA via des endpoints API. 

- **Tests utilisateurs** : Effectuer des tests utilisateurs afin de valider l’efficacité du système et les choix ergonomiques et fonctionnels effectués durant le développement. 

## 2. Périmètre du Projet 

### 2.1. Fonctionnalités attendues 

- **Interaction vocale** : Développer un robot capable d'engager une conversation avec un utilisateur. Les conversations se déroulent à tour de rôle. 

- **Gestion des dialogues** : Un chatbot Rasa capable de comprendre et traiter les requêtes des utilisateurs en français. Le serveur rasa doit fournir une réponse à prononcer par Pepper, ainsi que des informations supplémentaires telles que les positions de réponse appropriées et d'autres informations à restituer sur la vue de la tablette. 

- **Reconnaissance vocale** : Avec l’Api google speech_recognition, intégrer un système de reconnaissance vocale pour capter les commandes des utilisateurs et les convertir en texte. L'audio enregistré est encodé et envoyé au serveur Flask. Là, il est décodé et envoyé au serveur Google qui renvoie une transcription. 

- **Intégration Rasa** : Une fois la transcription fournie, le serveur Flask gère la communication en interne avec le serveur rasa qui s'exécute sur la même machine hôte. Le serveur Flask renvoie ensuite une réponse à Pepper. 

- **Comportements de base** :Dans un premier temps, le robot doit afficher un comportement de base pour effectuer les opérations suivantes : 

- **Suivi de visage** : Le système de suivi étant capricieux et instable, nous avons eu l'idée de créer une mémoire tampon avec un compteur de temps. Que la caméra suive un visage ou perde la cible, un compteur est activé. Si la caméra persiste en dernier, son compteur respectif est activé et l'autre compteur est désactivé. Par exemple : si le suivi détecte un visage, le compteur positif est activé et le compteur désactivé est désactivé. Au bout de 5 secondes, si le compteur n'est pas interrompu par l'un ou l'autre, le script d'attente envoie un signal pour démarrer une nouvelle conversation. Illustration 9.3 

- Dans la boucle de conversation, un booléen indique si une boucle est active. Il empêche le signal du suivi de lancer un nouveau message d'accueil et déclenche un nouvel enregistrement sonore. 

   - A. Des LED indiquent que l'enregistrement est en cours, terminé ou échoué. Pepper affiche des yeux bleus lorsqu'il parle. Il passe ensuite au vert pour signaler qu'il enregistre la parole de l'utilisateur. 

   - B. Recevoir un signal tactile de l’avant de la tête pour interrompre la parole de Pepper 

   - C. Choisir au hasard une animation appropriée pour prononcer les paroles neutres. D. Choisir une animation appropriée en fonction de la position du discours. Par exemple, effectuez un pouce levé lorsque vous prononcez un discours affirmatif. 

   - E. En mode standby, Pepper essaiera de détecter un visage toutes les 3 secondes. 

   - F. Une fois que Pepper détecte un visage, il doit le suivre en alignant son visage avec celui de l'utilisateur. Il passera en mode engagé. 

   - G. En mode engagé, si Pepper perd la trace du visage, il essaiera 3 fois de rétablir le suivi du visage avant d'abandonner. 

   - H. Si le robot ne parvient pas à rétablir le suivi du visage, Pepper doit dire au revoir au désenchantement et revenir en mode standby. 

   - I. Pepper doit afficher sa réponse ainsi que les questions de l'utilisateur sur la vue de la tablette. La vue Web doit être mise à jour à chaque fois qu'une réponse est renvoyée, fournissant ainsi des sous-titres pendant la conversation. 

   - J. La vue Web de la tablette doit afficher le site Web de l'Université d'Avignon comme page standard. 

- **Fonctionnalités principales d’accueil** : Pepper doit répondre aux questions sur le campus du CERI. Les informations suivantes doivent être fournies par la base de données : 

   - A. - Consulter l’emploi du temps des cours du Ceri 

   - B. - Consulter les contacts de professeurs du Ceri 

   - C. - Consulter l’orientation bâtiment du Ceri 

   - D. - Poser des questions ouvertes au LLM 

   - E. - Demander des traductions via le Google Translate API 

   - F. - Consulter la météo 

   - G. - Afficher les sous-titres de la conversation sur l'écran de la tablette 

   - H. - Afficher différentes pages d'URL pour des informations supplémentaires sur l'écran de la tablette 

- **Fonctionnalités additionnelles** : Intégrer des réponses aux questions d’accueil générales: Les informations suivantes doivent être fournies par Rasa: 

   - A. Fournir renseignements sur Avignon, la France 

   - B. Renseignement sur l’université d’Avignon 

   - C. Recommander un restaurant dans la ville 

   - D. Demander l’état mental de l’utilisateur 

- E. Raconter une blague 

- F. Socialisation avec un utilisateur (demander son nom, poids, âge, origine) 

### 2.2. Technologies utilisées 

- **Robot et programmation** : l'outil Choregraphe 2.5.10 pour la programmation des comportements. Les scripts sont exécutés en Python 2.7. 

- **Interface graphique** : Utilisation des frameworks Flask et Jinja avec Python 3.10 pour le développement de l'interface graphique sur l’écran. On utilise le Flask-SocketIO 5.5.1 pour la mise à jour des données vers le navigateur. 

- **Modèle de langage** : Framework Rasa 3.6 avec le Rasa SDK 3.6.20 pour créer un système d'IA conversationnel et gérer les interactions avec l'utilisateur. 

- **Reconnaissance vocale** : Google Speech API pour la conversion vocale en texte. 

- **Base de données** : on utilise la sqlite python library pysqlite3-wheels 0.5.0 pour fournir les renseignements du CERI. 

- **Large Language Model** : on utilise Ollama, un exécuteur de modèles d'IA déployé localement. Le modèle téléchargé et utilisé pour ce système est le llama3.2:latest. 

### 2.3. Livrables 

- **Interaction fluide** : le robot pepper sera capable d’entamer et de maintenir une conversation de manière fluide, en simulation et en test physique. 

- **Précision du modèle Rasa** : Le modèle sera capable de comprendre et de traiter au moins 80% des requêtes correctement. 

- **Simplicité des comportements** : Les mouvements d’accueil de Pepper seront naturels et synchronisés avec la conversation, en simulation comme en réel. 

- **Documentation** : Un rapport sera fourni avec les détails techniques, les choix de conception et les résultats des tests en simulation et en physique. 

## 3. Contraintes et Risques du Projet 

### 3.1. Contraintes techniques 

- L'utilisation du robot virtuel sur Choregraphe limite la portée des tests. Certaines implémentations nécessitent obligatoirement des tests avec le robot réel. Le logiciel ne permet pas d'enregistrer du son par exemple, simulant ainsi toutes les capacités de Pepper. 

- Bien que théoriquement possible, il serait difficile d'interrompre le discours de Pepper par une commande vocale. Pepper devrait implémenter une reconnaissance vocale avancée pour enregistrer et différencier les voix des utilisateurs afin de suivre une commande « stop » par exemple. Pepper pourrait risquer d'enregistrer sa propre voix tout en parlant en même temps. La solution alternative serait d'utiliser les capteurs tactiles sur sa tête à la place. 

- Il est également difficile d'installer des bibliothèques personnalisées sur le système d'exploitation Pepper. La reconnaissance vocale de Google, par exemple, n'est pas installée sur Pepper. Cela nécessite que le fichier audio soit encodé avant d'être envoyé au serveur où il est ensuite renvoyé à Google. Bien que les petits fichiers audio puissent entraîner un lag négligeable, une configuration idéale devrait fournir des réponses rapides et en temps réel du robot pour une conversation naturelle. 

### 3.2. Risques potentiels 

- La complexité du système requiert une courbe d'apprentissage élevée dès qu’on n’est pas familier avec le logiciel Choregraphe pour programmer Pepper. Le Modèles Rasa est aussi assez complexe et entraîner des modèles Rasa peut nécessiter une compréhension approfondie des NLP et des pipelines de formation. La dépendance de la documentation et des tutoriels en ligne pour résoudre les problèmes techniques peut être chronophage.  Cette complexité peut rendre difficile l'évaluation du temps nécessaire pour atteindre tous les objectifs en termes de contrainte de temps. 

- La latence ou les déconnexions entre le robot Pepper et le serveur Flask pourraient impacter la fluidité des interactions, ce qui pourrait nuire à l'expérience utilisateur. 

- Difficultés à obtenir des feedbacks constructifs pour améliorer le système. le résultat des tests dépendra de la coopération et de la participation des utilisateurs 

- Problèmes de sécurité ou de confidentialité des données des utilisateurs. 

### 3.3. Mesures de prévention 

- Utiliser des environnements virtuels (virtualenv ou conda) pour isoler les dépendances Python 2.7. 

- Organiser des formations internes, diviser le projet en sous-tâches simples, et utiliser les forums de support communautaire 

- Effectuer des tests de performances anticipés, utiliser des protocoles légers comme WebSockets et optimiser les appels API. 

- Prévoir des tests utilisateurs réguliers avec des questionnaires simples pour obtenir des retours constructifs. 

## 4. Méthodologie 

- Méthodologie agile avec des itérations de développement. Chaque fonctionnalité sera développée en petite étape, testée et validée avant de passer à la suivante. 

- Utilisation de git pour le suivi des versions et le travail colloboratif. 

- Des enregistrements audio ont été réalisés, et la fonctionnalité Record Audio a été configurée pour Pepper afin de permettre des tests dans Choregraphe, notamment dans les situations où l'accès au robot n'est pas disponible. 

- L'objectif principal était de développer et de tester un prototype permettant une interaction de base. Les systèmes Choregraphe et RASA ont été appris simultanément tout en travaillant vers cet objectif. Les progrès ont été réalisés grâce à un processus itératif impliquant des essais et des erreurs. 

- À chaque étape, nous concevrions différents modèles, à tester dès qu'une opportunité de test se présenterait. 

## 5. Scénarios de Tests Utilisateurs 

### 5.1. Objectifs des tests utilisateurs 

- Valider l’intuitivité de la navigation et des interactions avec Pepper. 

- Tester l'efficacité des fonctionnalités principales du système. 

### 5.2. Questionnaire 

L’interaction vocale avec Pepper était-elle fluide ? 

Très fluide Plutôt fluide Moyennement fluide Peu fluide Pas fluide du tout 

Les réponses de Pepper étaient-elles pertinentes par rapport à vos questions ou demandes ? 

Toujours pertinentes 

Souvent pertinentes 

Moyennement pertinentes Rarement pertinentes Jamais pertinentes 

Les indications visuelles sur l’écran du robot étaient-elles claires et utiles ? 

Très claires Plutôt claires Moyennement claires Peu claires Pas claires du tout 

Les animations et les mouvements de Pepper étaient-ils naturels et synchronisés avec l’interaction ? 

Très naturels Plutôt naturels Moyennement naturels Peu naturels Pas naturels du tout 

#### Fonctionnalités 

Quelle fonctionnalité vous a paru la plus utile ? (Réponse libre) Quelle fonctionnalité vous a paru la moins utile ? (Réponse libre) Avez-vous rencontré de compréhension, etc.) ? (Réponse libre) 

Expérience Générale 

À quel point êtes-vous satisfait(e) de votre interaction globale avec Pepper ? Très satisfait(e) Satisfait(e) Moyennement satisfait(e) Peu satisfait(e) Pas satisfait(e) 

Sur une échelle de 1 à 5, comment évalueriez-vous Pepper en termes de convivialité ?  (1 = Très peu convivial, 5 = Très convivial) 

1 

2 

3 

4 

5 

#### Suggestions et Améliorations 

- Quelles fonctionnalités supplémentaires aimeriez-vous voir dans le système ? (Réponse libre) 

- Avez-vous des suggestions pour améliorer l’expérience avec Pepper ? (Réponse libre) 

## 6. Public Cible 

### 6.1. Profil des utilisateurs 

- **Âge** : 18-45 ans. 

- **Profession** : Étudiants,  Étudiants, professionnels dans les secteurs technologiques et robotiques. 

- **Compétences techniques** : Compétences en informatique de base à avancées. 

### 6.2. Nombre d’utilisateurs 

- Phase 1 : 5 utilisateurs (phase exploratoire) 

## 7. Critères de Réussite et Évaluation 

### 7.1. Indicateurs de Performance (KPI) 

- Taux de réussite des tâches (> 90%). 

- Temps d'accomplissement des tâches (< 2 minutes). 

- Satisfaction utilisateur (notation >4/5). 

### 7.2. Retours des utilisateurs 

- Analyser les feedbacks post-tests. 

- Faire un rapport des fonctionnalités futures possibles à implémenter en fonction des commentaires des utilisateurs 

## 8. Équipe du Projet 

#### **● Diallo Mouhamadou Ahibou** 

  Responsable de l'écriture du modèle de langage RASA, y compris les règles, les histoires
et les actions.
  Écrit les scripts d'action pour que RASA interagisse avec la base de données
  Responsable de l'écriture de la base de données sqlite pour stocker les informations
CERI.

#### **● Silveira Feitosa Tiago** 

  Responsable de la mise en place des comportements de Pepper sur Choregraphe.
  Écrit le Module de conversation, Suivi Visage, et la Mise à jour du Tablet
  Intégration du serveur avec l'installation locale du fournisseur LLM ollama.
  Responsable de l'intégration de Pepper avec les serveurs via endpoints.


## 9. Annexes

<img width="701" height="243" alt="image" src="https://github.com/user-attachments/assets/09a8d087-c815-4702-a165-63b43230b4cf" />

Flux d'informations de l'ensemble du système

<img width="701" height="439" alt="image" src="https://github.com/user-attachments/assets/ac96645a-bae6-48b7-a0ae-0aae0311b46d" />

Boucle de conversation conçu sur application Choregraphe

<img width="583" height="381" alt="image" src="https://github.com/user-attachments/assets/47801462-5296-454a-9a6b-2b69440b67ba" />

Logique du suivi du visage du locuteur par le robot

<img width="602" height="462" alt="image" src="https://github.com/user-attachments/assets/3ce1f594-0a9c-45ed-afa8-f3611159113a" />

Capture d'écran de la vue web que nous prévoyons d'afficher sur la tablette, montrant les sous-titres des conversations ainsi qu'un site web redirigé.

<img width="313" height="328" alt="image" src="https://github.com/user-attachments/assets/75b43400-ba07-4678-968b-b6b7e2dc4d3e" />

Mini chatbot créé pour tester les fonctionnalités du système RASA.


---
---


# Robots and Natural Interactions with Humans



## Tiago Feitosa, France

## Mouhamadou Diallo, France

```
tiago.silveira-feitosa@univ-avignon.fr, mouhamadou-ahibou.diallo@univ-avignon.fr
```
## Abstract

Recent advances in Natural Language Processing (NLP) and
speech technologies have expanded the possibilities for socially
interactive robots. This project presents the design and imple-
mentation of a dialogue system for Aldebaran’s Pepper robot,
integrating the RASA framework with large language models
(LLMs) and external APIs to support natural, voice-driven in-
teractions. The robot functions as an interactive receptionist,
capable of answering student queries related to schedules, pro-
fessor contact details, and building navigation. The architecture
combines a behavior model built with Choregraphe and a Flask
server interfacing with RASA, Ollama LLM, Google Speech
Recognition, translation services, and a SQLite3 database. A
turn-based communication loop allows Pepper to capture audio,
transmit data for processing, and deliver synchronized, gesture-
enhanced verbal responses. Additional interaction is provided
via Pepper’s tablet, which displays subtitles and web content
dynamically through websockets. Despite achieving mostly
fluid conversational exchanges and accurate open-ended LLM
responses, challenges remain. Speech recognition accuracy suf-
fers with acronyms and uncommon names, and response delays
disrupt conversational flow. RASA’s structured dialogue can
constrain flexibility, particularly in multi-step database queries.
Hardware and software limitations in Pepper, Choregraphe, and
the tablet’s browser also hinder system reliability and respon-
siveness. This work highlights both the potential and current
limitations of deploying conversational AI in physical robots,
offering a foundation for improving real-time interaction qual-
ity, multimodal feedback, and system robustness in future itera-
tions.

Index Terms: speech recognition, human-robot interaction,
natural interaction

## 1. Introduction

Recent advancements in Natural Language Processing (NLP)
have accelerated the adoption of robots across various environ-
ments, increasing the demand for intelligent systems capable
of natural and adaptive communication. This project explores
the integration of the RASA dialogue management framework
with Large Language Models (LLMs) in Aldebaran’s Pepper
robot to enhance dynamic and interactive dialogue experiences.
By combining AI-driven text processing with speech recogni-
tion and synthesis technologies, the system enables fluid, open-
ended conversations, allowing users to engage with robots in an
intuitive and human-like manner. Designed for public space in-
teractions, the robot will function as a receptionist, assisting stu-
dents with general inquiries such as schedules, professor con-
tacts, available rooms, and directions within the building.

<img width="348" height="350" alt="image" src="https://github.com/user-attachments/assets/9a5072b7-96d7-42d4-b91c-a126ed902521" />

```
Figure 1:Schematic diagram of conversation loop.
```
## 2. Methods

The system consists of two main components. The first is the
robot behavior model designed on the Choregraphe suite. The
second is the Flask server which connects to several end-points
and communicates their answers to the robot. These APIs in-
clude the main conversation framework: RASA, along with
other APIs for functionalities such as the Ollama LLM provider
for open questions, Google speech recognition, google trans-
late, and sqlite3 database.


2.1. Robot Behavior Model


The Choregraphe suite allows for the creation of modular scripts
that connect sequentially through interactive boxes, represent-
ing different behavioral components. Starting from a template
project, we designed a loop-based turn-taking conversation pat-
tern managed by CommManager, which controls the conversa-
tion flow, as show in Figure 1. The loop follows these steps:

- User Speech Recording:The system records user input
    and sends the data as a JSON object to the Flask server
    via an HTTP request.
- Response Processing:The Flask server determines an
    appropriate reply and returns it to CommManager, which
    decides whether to continue or exit the loop.
- Speech Synthesis & Animation:If the loop continues,
    the response is passed to AnimatedSpeech, where the robot vocalizes it with synchronized movements to enhance gestural realism.

2.1.1. Handling User Interruptions

By default, Pepper cannot reliably record the user voice while
it is speaking. Pepper has microphones and speakers close to-
gether, and does not have echo cancellation in the standard soft-
ware. This means that if you record audio while Pepper is talk-
ing, it will mostly record its own voice. As a result, this would
corrupt the transcript.

Interrupting Pepper with voice command would be the ideal
solution for the closest we could get to a natural human-like
interaction. Although it is possible to interrupt Pepper’s speech
in this way, it would require Pepper to learn and distinguish their
own voice and that of the user. Such capability would have to
be custom implemented, as the suite does not support it natively.
The alternative would be to use the touch sensors provided on
top of their head instead. We added functionality allowing the
user to gently tap on the robot head to interrupt its speech.

2.2. Tablet Interface & WebSocket Updates

The beginning of a conversation loop triggers the tablet to ac-
cess the page rendered by the server. Access to the page grants
an immediate connection to the websocket for real-time up-
dates. The page is divided in two sections. The upper section
displays the subtitles of the conversation. The bottom contains
an HTML iframe element that allows the browser to display
other URLs at the current address rendered by our server. Cer-
tain responses provided by RASA contain a variable for URL
addresses. In such cases, the server detects the URL and sends
a websocket message to the connected clients.

2.3. Face Tracking Integration

The initial idea was to create a face tracking module that runs in
conjunction with the conversation loop module. If the target is
lost, a time counter starts. If the visual detection is not reestab-
lished within that waiting time, the module would trigger a stop
to the conversation loop. Due to difficulties in fine-tuning the
tracking system, we opted for a simpler solution. The tracking
runs independently in parallel and does not trigger or stop the
conversation. The conversation loop is only stopped if the user
gives the command “au revoir” that is detected by CommMan-
ager.

2.4. Challenges and Limitations

The Choregraphe suite does not have the ability to record users’
speech, thus allowing us to test the design in its entirety. A
workaround was to upload recorded wav files to be used in the
conversation loop. The different recorded audio files could not
be changed during execution either, thus limiting our testing
efforts. We used a trial-and-error approach to overcome such
limitations. Several different models were drawn and tested on
the robot when the opportunity became available.

## 3. Results

These results reflect my overall impressions formed through
hands-on testing and direct interaction with the system. As both
a tester and a regular user, my observations encompass the sys-
tem’s performance, usability, and responsiveness across various
scenarios. While these insights are subjective, they stem from
extensive real-world engagement, allowing me to assess the sys-
tem’s strengths, limitations, and areas for improvement.

- The flow of the conversation is mostly fluid.
- Pepper mostly succeeds in keeping the conversation loop
    active.
- Pepper mostly succeeds in responding to open questions
    using the LLM.
- Pepper overall succeeds in responding to queries about
    directions in the CERI building.
- Pepper mostly fails to respond to database queries con-
    cerning student schedules.
- Pepper somewhat fails to respond to database queries
    concerning available classrooms.
- Pepper somewhat succeeds in responding to database
    queries concerning professors’ contact information.
- The LLM responses were the most contextually correct,
    but they had the longest delivery time.
- Pepper somewhat succeeds in keeping visual contact
    with the user.
- Pepper mostly fails to display subtitles and URL updates
    on the tablet screen.

## 4. Discussion


The flow of the conversation is somewhat fluid. The loop suc-
cessfully keeps a turn-taking approach to conversation. How-
ever, the time it takes for Pepper to respond hinders the flow of
conversation. Pepper takes a certain amount of time to respond
to each user statement. That amount of time is usually longer
than that of a natural conversation between two humans. This
delay is due to factors like the connection speed and API re-
sponse times. The LLM connected to the server provided ap-
propriately contextualized responses in cases not covered by
RASA. However, the LLM took the most amount of time to
respond. The LLM model takes time to process the request and
summarize an appropriate response in less than 50 words.
Each time the user desires to consult the LLM, they must
first instruct Pepper, which is actually RASA in the background,
with the command “question ouverte”. This initial step, which
must be repeated each time, making the conversation less fluid
and natural. A different implementation might have yielded im-
proved results. A future implementation should include an op-
tion to query the LLM in case all other RASA queries have been
first checked and fail to provide a response. The LLM, thus, can
provide an alternative way to work as default mechanism and
maintain the perception of naturalness in the conversation.
A fine-tuning of the Google Speech Recognition (GSR) was
necessary. There was a lack of contextualization of the na-
ture of users’ input. The RASA system expected input like
letters and numbers to form acronyms, which would then be
passed to the database. If text is not precisely formatted and
matched, the database query will fail to retrieve an appropriate
response. The GSR failed to transcribe the letter C before a
classroom number, like in C137, for example. It would always
transcribe “c’est” instead. The GSR failed to understand the
“M1 ILSEN” voice input. Different transcripts would contain
“Emma il sc`ene”, “Main scene”, “Mise en sc`ene”. The GSR
also fails to understand first and people’s names. Simple names
like Sophie, Fabrice and Paul were easily identified. Family
names and uncommon names like Nabitz, Koumpli and Jourlin were not transcribed correctly. GSR can struggle with abbrevia-
tions and codified input, especially if they are uncommon or not
part of its standard language model. “Users have to option to
“define custom classes for recognizing specific types of words,
such as acronyms”[1].
The RASA framework for conversation, which includes
rules, stories and polices is a powerful tool to create a set of
general directives. If not properly designed, rules, unlike sto-
ries, can restrict and hinder the conversation flow. In the case
where users want to consult their schedule, for example, they go
through a 3-step process of input. The user asks Pepper/RASA
to consult their schedule. RASA asks the user which major (for-
mation) they want to check, the user responds, then RASA asks
which group they belong to, whether full-time students or stu-
dents enrolled in a work-study program. Finally, RASA asks the
user what time or date they want to consult their schedule. The
user may reply a day of the week, a period of the day, a month
and day etc. The necessary accuracy of the input already is a
major factor to failure when checking the database. With each
step in this process, the probability of failure increases even fur-
ther.
In order to get correct responses from the database, it would
be necessary to develop a more complex and flexible system that
could process a large number of different inputs and transform
them into a standard query term for the database. This system
would transform days of the week, or general periods of time
like morning or next week into a specific date or a date range to
check against the database and thus yield better results.
The Choregraphe software also turned out to be an unre-
liable tool to be used. It would sometimes fail to update the
Pepper movements on the screen. After a certain number of
updates to the model, the software would eventually crash and
stop working, forcing a restart or even leave lingering processes
in the memory working indefinitely. Our reliance on the limita-
tions of the Choregraphe suite, mainly its incapacity to capture
audio resulted in a significant barrier to the progress of our de-
velopment.
The Choregraphe built-in script for face tracking proved
to be unreliable. This simple solution did not maintain proper
tracking. The script triggered “face detected” and “target lost”
a very high number of times in only a few seconds. Pepper
sometimes fails to keep proper angle targeting the user face,
and sometimes would look away. A proper calibration or and
custom adjustment of settings could improve the stability of the
module input/output. If Pepper fails to detect a face for an ex-
tended period, the tracking process might halt altogether. A
solution to reactivate the script must be put in place.
The robot tablet and its browser partially succeeded in up-
dating the browser in real-time via websockets. The URL which
was embedded in an iframe element was updated, however the
straightforward text elements were not updated. The same page
update was completely successful on a different browser in a
different machine. The most probable cause is that the robot
browser might have outdated libraries that do not fully support
websockets used.

## 5. Conclusions

By integrating the RASA framework and NaoQi SDK, we
created a basic interactive system for the Pepper robot. De-
spite limitations, this project provides valuable insights into the
challenges of developing fully interactive social robots, paving
the way for future enhancements in real-time dialogue, speech
recognition, and user interaction.

## 6. References

```
[1] Google Cloud, “Improve transcription results with model adap-
tation,” [Online]. Available: https://cloud.google.com/speech-to-
text/docs/adaptation-model. Accessed: May 11, 2025.
```



