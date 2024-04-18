import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Quiz Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    question_text = ft.Text("")
    option_buttons = []
    for i in range(5):
        option_buttons.append(ft.ElevatedButton(text="", on_click=lambda _, option=i: select_option(option)))
    result_text = ft.Text("")

    # Função para solicitar e exibir uma nova pergunta
    def get_question():
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            question = response.json()[0]
            question_text.value = question['text']
            for i, option in enumerate(question['options']):
                option_buttons[i].text = option
        else:
            question_text.value = "Failed to load question"
        page.update()

    # Função para enviar a resposta do usuário e exibir o resultado
    def select_option(option):
        response = requests.post("http://localhost:8080/submit/", json={"answers": [option]})
        if response.status_code == 200:
            result = response.json()
            result_text.value = f"Your score: {result['score']} / {result['total']}"
        else:
            result_text.value = "Failed to submit answer"
        page.update()

    # Adicionar elementos à página
    page.add(question_text)
    for button in option_buttons:
        page.add(button)
    page.add(result_text)

    # Obter a primeira pergunta ao iniciar o aplicativo
    get_question()

ft.app(target=main, port=8000)
