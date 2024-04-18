import flet as ft
import requests

def main(page: ft.Page):
    page.title = "nome = App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    input_text = ft.TextField(hint_text="Digite seu nome", width=300, autofocus=True)
    submit_button = ft.ElevatedButton(text="Enviar", on_click=lambda _: send_name(page, input_text))
    response_text = ft.Text()

    # Função para enviar o nome para o back-end
    def send_name(page, input_text):
        name = input_text.value.strip()
        if name:
            response = requests.post("http://localhost:8080/getName", json={"name": name})
            if response.status_code == 200:
                response_text.value = response.json()['message']
            else:
                response_text.value = "Falha ao enviar nome"
        page.update()

    # Adicionar elementos à página
    page.add(input_text, submit_button, response_text)

ft.app(target=main, port=8000)
