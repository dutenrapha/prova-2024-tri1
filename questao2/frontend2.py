import tkinter as tk
from tkinter import messagebox
import requests

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.quiz_frame = tk.Frame(root)
        self.quiz_frame.pack(padx=20, pady=20)

        self.question_labels = []
        self.radio_vars = []
        self.questions = []

        self.load_questions()

        self.submit_btn = tk.Button(root, text="Submit Answers", command=self.submit_answers)
        self.submit_btn.pack(pady=10)

    def load_questions(self):
        try:
            response = requests.get('http://localhost:8080/questions/')
            self.questions = response.json()

            for i, question in enumerate(self.questions):
                question_label = tk.Label(self.quiz_frame, text=f"{i + 1}. {question['text']}")
                question_label.grid(row=i, column=0, sticky='w')
                self.question_labels.append(question_label)

                radio_var = tk.IntVar()
                for j, option in enumerate(question['options']):
                    radio_btn = tk.Radiobutton(self.quiz_frame, text=option, variable=radio_var, value=j)
                    radio_btn.grid(row=i, column=j+1, sticky='w')
                self.radio_vars.append(radio_var)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to load questions: {e}")

    def submit_answers(self):
        answers = [var.get() for var in self.radio_vars]

        try:
            response = requests.post('http://localhost:8080/submit/', json={"answers": answers})
            result = response.json()
            messagebox.showinfo("Result", f"Your Score: {result['score']} / {result['total']}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to submit answers: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
