import flet as ft
import requests

def main(page: ft.Page):
    lbl_output = ft.Text("", size=100, text_align="center", width=3000)

    def on_send_click(e):
        text = txt_input.value
        response = requests.post("http://localhost:8080/sentiments", json={"text": text})
        sentiment_response = ""
        if response.status_code == 200:
            sentiment = response.json()["sentiment"]
            sentiment_response = "😊" if sentiment == "positivo" else "😞"
        else:
            sentiment_response = "Erro ao processar o sentimento"

        lbl_output.value = sentiment_response
        lbl_output.update()

        txt_input.value = ""
        page.update()

    txt_input = ft.TextField(hint_text="Digite seu texto aqui", width=300, autofocus=True)
    send_button = ft.ElevatedButton(text="Enviar", on_click=on_send_click)

    input_container = ft.Row(
        controls=[txt_input, send_button],
        alignment="center",
        expand=True
    )

    main_container = ft.Column(
        controls=[lbl_output, input_container],
        alignment="center",
        expand=True
    )

    page.add(main_container)

ft.app(target=main)