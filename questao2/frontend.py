import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Quiz Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def start_quiz():
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            questions = response.json()
            show_questions(questions)
        else:
            page.snackbar_text = "Failed to fetch questions"
        page.update()

    def show_questions(questions):
        page.clear()
        for question in questions:
            question_text = question["text"]
            options = question["options"]
            question_label = ft.Label(text=question_text)
            option_buttons = [ft.Button(text=option, on_click=lambda _, qid=question["id"], ans=option: answer_question(qid, ans)) for option in options]
            page.add(question_label)
            for button in option_buttons:
                page.add(button)

    def answer_question(question_id, answer):
        response = requests.post("http://localhost:8080/submit/", json={"question_id": question_id, "answer": answer})
        if response.status_code == 200:
            start_quiz()
        else:
            page.snackbar_text = "Failed to submit answer"
        page.update()

    start_button = ft.ElevatedButton(text="Start Quiz", on_click=lambda _: start_quiz())
    page.add(start_button)

ft.app(target=main, port=8000)
