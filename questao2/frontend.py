import tkinter as tk
from tkinter import messagebox
import requests

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x300")

        self.questions = self.get_questions()
        self.user_answers = [None] * len(self.questions)
        self.current_question = 0

        self.question_label = tk.Label(self.root, text="", wraplength=380, justify="center")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(5):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.select_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

    def get_questions(self):
        response = requests.get("http://localhost:8080/questions/")
        if response.status_code == 200:
            return response.json()
        else:
            messagebox.showerror("Error", "Failed to retrieve questions from the server")
            return []

    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["text"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)

    def select_answer(self, answer_index):
        self.user_answers[self.current_question] = answer_index
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
            self.next_button.config(state=tk.DISABLED)
        else:
            self.submit_answers()

    def submit_answers(self):
        response = requests.post("http://localhost:8080/submit/", json={"answers": self.user_answers})
        if response.status_code == 200:
            result = response.json()
            score = result["score"]
            total_questions = result["total"]
            messagebox.showinfo("Quiz Result", f"You scored {score} out of {total_questions}")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Failed to submit answers to the server")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    app.display_question()
    root.mainloop()
