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
                options = "\n".join([f"{i}. {opt}" for i, opt in enumerate(question['options'], start=1)])
                question_list.controls.append(ft.ListTile(title=ft.Text(f"{idx + 1}. {question['text']}\n{options}")))
        page.update()

    # Função para enviar respostas e exibir o resultado
    def submit_answers(page, question_list):
        answers = []
        for control in question_list.controls:
            answer = control.title.split("\n")[-1].split(".")[0]
            answers.append(int(answer))
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
