from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
# URL da AwesomeAPI para cotações de moedas
# Documentação: https://docs.awesomeapi.com.br/api-de-moedas
AWESOME_API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/"

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao serviço de cotações de moedas! Use /cotacoes para ver as cotações."})

@app.route('/cotacoes')
def get_cotacoes():
    try:
        # Exemplos de pares de moedas que queremos buscar
        # Você pode adicionar mais pares conforme necessário
        moedas = "USD-BRL,EUR-BRL,BTC-BRL,JPY-BRL"

        # Faz a requisição HTTP para a AwesomeAPI
        response = requests.get(f"{AWESOME_API_BASE_URL}{moedas}")
        response.raise_for_status() # Lança um erro para status de erro HTTP

        cotacoes_data = response.json()

        # Formata os dados para exibição, se desejar
        # Para simplificar, vamos retornar os dados brutos da API por enquanto
        # Em um projeto real, faríamos um parse mais cuidadoso

        return jsonify(cotacoes_data)

    except requests.exceptions.RequestException as e:
        # Lida com erros de conexão ou outros erros da requisição
        app.logger.error(f"Erro ao buscar cotações da AwesomeAPI: {e}")
        return jsonify({"error": "Não foi possível obter as cotações no momento."}), 500
    except ValueError as e:
        # Lida com erros de parse JSON
        app.logger.error(f"Erro ao processar a resposta da API: {e}")
        return jsonify({"error": "Erro ao processar dados das cotações."}), 500
    except Exception as e:
        # Captura quaisquer outros erros inesperados
        app.logger.error(f"Ocorreu um erro inesperado: {e}")
        return jsonify({"error": "Ocorreu um erro inesperado."}), 500

# Define a porta a partir de uma variável de ambiente ou usa 5000 como padrão
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
