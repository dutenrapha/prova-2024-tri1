import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Quiz Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = "adaptive"

    # Função para obter perguntas do backend
    def get_questions():
        return requests.get("http://localhost:8080/questions/").json()

    # Função para enviar respostas ao backend e receber a pontuação
    def submit_answers(user_answers):
        return requests.post("http://localhost:8080/submit/", json={"answers": user_answers}).json()

    # Exibir as perguntas
    questions = get_questions()
    user_answers = []

    def display_question(question_index):
        page.clean()
        question = questions[question_index]
        page.add(ft.Text(f"Pergunta {question_index + 1}: {question['text']}"))
        for i, option in enumerate(question["options"]):
            page.add(ft.ElevatedButton(
                text=f"{i + 1}. {option}",
                on_click=lambda e, option_index=i: select_option(option_index)
            ))

    def select_option(option_index):
        user_answers.append(option_index)
        if len(user_answers) < len(questions):
            display_question(len(user_answers))
        else:
            display_results()

    def display_results():
        page.clean()
        score_data = submit_answers(user_answers)
        page.add(ft.Text(f"Sua pontuação: {score_data['score']} / {score_data['total']}"))

    display_question(0)

if __name__ == "__main__":
    ft.app(target=main)
