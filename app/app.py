from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cotacoes = {
        "USD_BRL": {"valor": "5.23", "moeda_base": "USD", "moeda_alvo": "BRL"},
        "EUR_BRL": {"valor": "5.65", "moeda_base": "EUR", "moeda_alvo": "BRL"},
        "GBP_BRL": {"valor": "6.50", "moeda_base": "GBP", "moeda_alvo": "BRL"},
        "JPY_BRL": {"valor": "0.033", "moeda_base": "JPY", "moeda_alvo": "BRL"}
    }
    return render_template('index.html', cotacoes=cotacoes, titulo="Cotações de Moedas")

@app.route('/api/cotacoes')
def api_cotacoes():
    cotacoes = {
        "USD_BRL": {"valor": "5.23", "moeda_base": "USD", "moeda_alvo": "BRL"},
        "EUR_BRL": {"valor": "5.65", "moeda_base": "EUR", "moeda_alvo": "BRL"},
        "GBP_BRL": {"valor": "6.50", "moeda_base": "GBP", "moeda_alvo": "BRL"},
        "JPY_BRL": {"valor": "0.033", "moeda_base": "JPY", "moeda_alvo": "BRL"}
    }
    return cotacoes

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
