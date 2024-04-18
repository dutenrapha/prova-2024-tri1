from flet import App, Text, TextInput, NumberInput, Select, List
import requests

def main():
    print("Welcome to the Quiz App!")
    
    # Obtendo perguntas do servidor
    questions = fetch_questions()
    if not questions:
        print("Failed to fetch questions from the server.")
        return
    
    # Iniciando o quiz
    user_answers = play_quiz(questions)
    
    # Enviando respostas para o servidor e obtendo resultados
    score, total_questions = submit_answers(user_answers)
    
    # Exibindo os resultados
    print(f"Your score: {score}/{total_questions}")

def fetch_questions():
    response = requests.get("http://localhost:8080/questions/")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def play_quiz(questions):
    user_answers = []
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['text']}")
        print("Options:")
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        user_answer = int(input("Your answer (enter option number): ")) - 1
        user_answers.append(user_answer)
    return user_answers

def submit_answers(user_answers):
    response = requests.post("http://localhost:8080/submit/", json={"answers": user_answers})
    if response.status_code == 200:
        result = response.json()
        return result["score"], result["total"]
    else:
        return 0, 0

if __name__ == "__main__":
    main()