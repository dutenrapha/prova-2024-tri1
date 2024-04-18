import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Quiz Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    question_text = ft.Text("")
    options_buttons = [ft.ElevatedButton(text="", on_click=lambda _: select_answer(page, index)) for index in range(5)]
    submit_button = ft.ElevatedButton(text="Submit", on_click=lambda _: submit_answers(page))

    # Função para carregar e exibir a próxima pergunta
    def load_next_question():
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            questions = response.json()
            if questions:
                question = questions[0]
                question_text.text = question['text']
                for index, option in enumerate(question['options']):
                    options_buttons[index].text = option
                # Remover a pergunta atual da lista de perguntas
                questions.pop(0)
                return True
        return False

    # Função para selecionar uma resposta
    def select_answer(page, index):
        # Desabilitar todos os botões de opções
        for button in options_buttons:
            button.disabled = True
        # Enviar a resposta selecionada para o backend
        response = requests.post("http://localhost:8080/submit/", json={"answers": [index]})
        if response.status_code == 200:
            result = response.json()
            page.alert(f"Your score: {result['score']}/{result['total']}", dismissible=False)

    # Função para submeter as respostas do usuário
    def submit_answers(page):
        # Desabilitar todos os botões de opções
        for button in options_buttons:
            button.disabled = True
        # Enviar as respostas selecionadas para o backend
        user_answers = [index for index, button in enumerate(options_buttons) if not button.disabled]
        response = requests.post("http://localhost:8080/submit/", json={"answers": user_answers})
        if response.status_code == 200:
            result = response.json()
            page.alert(f"Your score: {result['score']}/{result['total']}", dismissible=False)

    # Carregar e exibir a primeira pergunta
    load_next_question()

    # Adicionar elementos à página
    page.add(question_text)
    for button in options_buttons:
        page.add(button)
    page.add(submit_button)

ft.app(target=main, port=8000)
