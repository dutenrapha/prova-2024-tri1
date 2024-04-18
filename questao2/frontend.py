import flet as ft
import requests

class QuizApp:
    def __init__(self):
        self.current_question_index = 0
        self.answers = []

    def start_quiz(self):
        self.answers = []
        self.current_question_index = 0
        self.fetch_questions()

    def fetch_questions(self):
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            self.questions = response.json()
            self.show_question()
        else:
            print("Failed to fetch questions.")

    def show_question(self):
        question = self.questions[self.current_question_index]
        options = [ft.Button(text=option, on_click=lambda _, index=i: self.submit_answer(index)) for i, option in enumerate(question['options'])]
        question_widget = ft.Column(
            children=[
                ft.Text(question['text']),
                *options
            ]
        )
        ft.update(question_widget)

    def submit_answer(self, index):
        self.answers.append(index)
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.send_answers()

    def send_answers(self):
        response = requests.post("http://localhost:8080/submit/", json={"answers": self.answers})
        if response.status_code == 200:
            score_data = response.json()
            self.show_results(score_data['score'], score_data['total'])
        else:
            print("Failed to submit answers.")

    def show_results(self, score, total):
        result_text = f"Your score: {score}/{total}"
        result_widget = ft.Text(result_text)
        ft.update(result_widget)

if __name__ == "__main__":
    app = QuizApp()
    app.start_quiz()
    ft.app()
