from flet import TextField, Button, App
import requests

class QuizApp(App):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.current_question_index = 0
        self.answers = []

    def fetch_questions(self):
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            self.questions = response.json()
        else:
            print("Failed to fetch questions")

    def show_question(self):
        question = self.questions[self.current_question_index]
        self.clear()
        self.add(TextField(question["text"]))
        for i, option in enumerate(question["options"]):
            self.add(Button(option, self.handle_answer, args=[i]))

    def handle_answer(self, option_index):
        self.answers.append(option_index)
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.show_question()
        else:
            self.submit_answers()

    def submit_answers(self):
        response = requests.post("http://localhost:8080/submit/", json={"answers": self.answers})
        if response.status_code == 200:
            result = response.json()
            score = result["score"]
            total = result["total"]
            self.clear()
            self.add(TextField(f"Your score: {score}/{total}"))
        else:
            print("Failed to submit answers")

if __name__ == "__main__":
    app = QuizApp()
    app.fetch_questions()
    app.show_question()
    app.run()