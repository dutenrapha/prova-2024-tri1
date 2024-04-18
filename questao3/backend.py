from flask import Flask, render_template, request
from flet import Flet, Text, Column, Row, TextField, Button
from yahoofinance import YahooFinance

app = Flask(__name__)

@app.route("/getPrice", methods=["POST"])
def getPrice():
    symbol = request.form["symbol"]
    yf = YahooFinance(symbol)
    price = yf.price["regularMarketPrice"]
    return f"Preço atual de {symbol}: {price:.2f}"


@app.route("/")
def index():
    flet = Flet()

    with flet.Column(controls=[
        TextField(label="Nome da Ação", hint="Ex: AAPL"),
        Button(text="Obter Preço", on_click=getPrice)
    ]):
        flet.Text(id="priceLabel")

    return flet.render()

if __name__ == "__main__":
    app.run(debug=True)