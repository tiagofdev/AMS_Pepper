from ollama import chat
from ollama import ChatResponse


instruction = ". Donnez-moi une réponse simple et concise en moins de 50 mots. Veuillez ne pas inclure de contexte ni d'explications supplémentaires."

def ask_ollama(question):
    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': '' + question + instruction,
        },
    ])
    return response.message.content

# print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)

if __name__ == '__main__':
    pass