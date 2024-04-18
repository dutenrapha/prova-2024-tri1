import flet as ft
import requests

#Função para buscar perguntas da API
def get_questions():
    response = requests.get("http://localhost:8080/questions/")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch questions:", response.status_code)

#Função para enviar respostas para a API
def submit_answers(answers):
    response = requests.post("http://localhost:8080/submit/", json={"answers": answers})
    if response.status_code == 200:
        data = response.json()
        return data["score"], data["total"]
    else:
        print("Failed to submit answers:", response.status_code)

# Função de perguntas e respostas do usuário
def take_quiz(questions):
    print("Welcome to the Quiz!")
    print("====================")
    user_answers = []
    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['text']}")
        for j, option in enumerate(question['options']):
            print(f"{j + 1}. {option}")
        answer = input("Your answer (enter option number): ")
        user_answers.append(int(answer) - 1) 
    return user_answers

# main
def main():
    questions = get_questions()
    if questions:
        user_answers = take_quiz(questions)
        score, total = submit_answers(user_answers)
        print(f"\nYour score: {score}/{total}")

if __name__ == "__main__":
    main()