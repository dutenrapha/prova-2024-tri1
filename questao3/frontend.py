from flet import Flet, Text, Column, Row, TextField, Button
from backend import getPrice

def main():
    flet = Flet()

    with flet.Column(controls=[
        TextField(label="Nome da Ação", hint="Ex: AAPL"),
        Button(text="Obter Preço", on_click=getPrice)
    ]):
        flet.Text(id="priceLabel")

    flet.show()

if __name__ == "__main__":
    main()