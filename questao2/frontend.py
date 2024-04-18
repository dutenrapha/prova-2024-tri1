import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Quiz App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    question_list = ft.ListView(expand=True)
    submit_button = ft.ElevatedButton(text="Submit Answers", on_click=lambda _: submit_answers(page, question_list))

    # Função para buscar e exibir as perguntas
    def get_questions(page, question_list):
        response = requests.get("http://localhost:8080/questions/")
        question_list.controls.clear()
        if response.status_code == 200:
            questions = response.json()
            for idx, question in enumerate(questions):
                options = []
                for i, option_text in enumerate(question['options']):
                    option_radio = ft.TextButton(text=str(i+1), on_click=lambda _, idx=idx, i=i: select_option(page, question_list, idx, i))
                    options.append(option_radio)
                options_layout = ft.Row(options)
                question_list.controls.append(ft.ListTile(title=ft.Text(f"{idx + 1}. {question['text']}"), subtitle=options_layout))
        page.update()

    # Função para selecionar a opção
    def select_option(page, question_list, question_idx, option_idx):
        for control in question_list.controls[question_idx].subtitle.children:
            control.style = ft.ButtonStyle.OUTLINE
        question_list.controls[question_idx].subtitle.children[option_idx].style = ft.ButtonStyle.FILLED

    # Função para enviar respostas e exibir o resultado
    def submit_answers(page, question_list):
        answers = []
        for control in question_list.controls:
            selected_option = None
            if control.subtitle is not None:
                for i, button in enumerate(control.subtitle.children):
                    if button.style == ft.ButtonStyle.FILLED:
                        selected_option = i
                        break
            answers.append(selected_option)
        response = requests.post("http://localhost:8080/submit/", json={"answers": answers})
        if response.status_code == 200:
            result = response.json()
            page.alert_text = f"Your score: {result['score']} out of {result['total']}"
        else:
            page.alert_text = "Failed to submit answers"
        page.update()

    # Adicionar elementos à página
    page.add(question_list, submit_button)
    get_questions(page, question_list)

ft.app(target=main, port=8000)
