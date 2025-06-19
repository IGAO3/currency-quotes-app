from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

AWESOME_API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/"

MOEDAS = ["USD-BRL", "EUR-BRL", "GBP-BRL", "JPY-BRL", "CAD-BRL"]

@app.route('/')
def index():
    cotacoes = {}
    for moeda_par in MOEDAS:
        try:
            response = requests.get(f"{AWESOME_API_BASE_URL}{moeda_par}")
            response.raise_for_status()

            data = response.json()

            chave_api = moeda_par.replace('-', '')

            if chave_api in data:
                cotacao_data = data[chave_api]
                cotacoes[moeda_par] = {
                    "moeda_base": cotacao_data['code'],
                    "moeda_alvo": cotacao_data['codein'],
                    "valor": float(cotacao_data['bid'])
                }
            else:
                cotacoes[moeda_par] = {
                    "moeda_base": moeda_par.split('-')[0],
                    "moeda_alvo": moeda_par.split('-')[1],
                    "valor": "Erro/N/D"
                }

        except requests.exceptions.RequestException as e:
            cotacoes[moeda_par] = {
                "moeda_base": moeda_par.split('-')[0],
                "moeda_alvo": moeda_par.split('-')[1],
                "valor": "Erro/API"
            }
        except ValueError as e:
            cotacoes[moeda_par] = {
                "moeda_base": moeda_par.split('-')[0],
                "moeda_alvo": moeda_par.split('-')[1],
                "valor": "Erro/Processamento"
            }

    return render_template('index.html', titulo='Cotações de Moedas', cotacoes=cotacoes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
