from flet import prompt, Choice
import requests
def load_questions():
    response = requests.get("http://localhost:8080/questions/")
    questions = response.json()
    return questions

# Função para exibir as questões e coletar respostas do usuário
def play_quiz(questions):
    user_answers = []
    for question in questions:
        options = [Choice(index=i, label=option) for i, option in enumerate(question["options"])]
        answer = prompt(question["text"], options=options, type=Choice)
        user_answers.append(answer.index)
    return user_answers

# Função para enviar as respostas ao backend e exibir o resultado
def submit_answers(user_answers):
    response = requests.post("http://localhost:8080/submit/", json={"answers": user_answers})
    result = response.json()
    return result

# Função principal
def main():
    print("Welcome to the Quiz App!\n")
    questions = load_questions()
    user_answers = play_quiz(questions)
    result = submit_answers(user_answers)
    print(f"\nYour score: {result['score']} out of {result['total']}")

if __name__ == "__main__":
    main()
