import requests

# Função para obter perguntas do backend
def get_questions():
    response = requests.get("http://localhost:8080/questions/")
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter perguntas:", response.status_code)
        return None

# Função para enviar respostas do usuário para o backend e receber o resultado
def submit_answers(user_answers):
    response = requests.post("http://localhost:8080/submit/", json=user_answers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao enviar respostas:", response.status_code)
        return None

# Função principal
def main():
    # Obtém as perguntas do backend
    questions = get_questions()

    if questions:
        # Exibe as perguntas para o usuário
        for i, question in enumerate(questions):
            print(f"{i + 1}. {question['text']}")
            for j, option in enumerate(question['options']):
                print(f"   {j + 1}. {option}")

        # Pede ao usuário para responder as perguntas
        user_answers = []
        for _ in range(len(questions)):
            answer = input("Escolha a opção correta (digite o número da opção): ")
            user_answers.append(int(answer) - 1)

        # Envia as respostas para o backend e exibe os resultados
        result = submit_answers({"answers": user_answers})
        if result:
            print(f"\nSua pontuação: {result['score']} / {result['total']}")
    else:
        print("Não foi possível obter as perguntas. Verifique se o backend está em execução.")

if __name__ == "__main__":
    main()