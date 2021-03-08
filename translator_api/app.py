from flask import Flask, render_template, request
import requests, os, uuid, json
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Lê o texto que o usuário inseriu e o idioma selecionado no formulário
    original_text = request.form['text']
    target_language = request.form['language']

    # Lê as variáveis ambientais que criamos anteriormente no arquivo .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # Indique que queremos traduzir e a versão da API (3.0) e o idioma de destino
    path = '/translate?api-version=3.0'
    # Adicione o parâmetro de idioma de destino
    target_language_parameter = '&to=' + target_language
    # Crie o URL completo
    constructed_url = endpoint + path + target_language_parameter

    # Configure as informações do cabeçalho, que incluem nossa chave de assinatura
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Crie o corpo da solicitação com o texto a ser traduzido
    body = [{ 'text': original_text }]

    # Chama post em requests para chamar o serviço de Tradução
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Recupera a resposta JSON do servidor, que inclui o texto traduzido
    translator_response = translator_request.json()
    # Recupera o texto traduzido
    translated_text = translator_response[0]['translations'][0]['text']

    # Chama render_template para exibir a página de resposta,
    # texto original e idioma de destino para o modelo
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )