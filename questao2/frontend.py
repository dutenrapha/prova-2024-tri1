import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Quiz App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    questions_container = ft.ListView(expand=True)

    def fetch_questions():
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            questions = response.json()
            questions_container.clean()  # Limpar qualquer conteúdo anterior
            for question in questions:
                question_text = ft.Text(question['text'])
                options_group = ft.RadioGroup(options=[ft.Radio(label=option) for option in question['options']])
                questions_container.add(question_text, options_group)

    fetch_button = ft.ElevatedButton(text="Fetch Questions", on_click=lambda _: fetch_questions())
    page.add(fetch_button, questions_container)

ft.app(target=main, port=8000)
