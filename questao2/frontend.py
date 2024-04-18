import requests
import click

@click.command()
@click.option('--port', default=8080, help='Porta do servidor backend')
def play_quiz(port):
    # URL do backend
    backend_url = f"http://localhost:{port}"

    # Obter perguntas do backend
    response = requests.get(f"{backend_url}/questions/")
    if response.status_code != 200:
        click.echo("Erro ao obter perguntas do servidor.")
        return

    questions = response.json()

    # Iniciar o quiz
    click.echo("Bem-vindo ao Quiz!\nResponda as seguintes perguntas:")
    user_answers = []
    for i, question in enumerate(questions):
        click.echo(f"\n{i+1}. {question['text']}")
        for j, option in enumerate(question['options']):
            click.echo(f"   {j+1}. {option}")

        answer = click.prompt("Sua resposta (digite o número da opção):", type=int)
        user_answers.append(answer - 1)  # Índice baseado em 0

    # Enviar respostas para o backend
    response = requests.post(f"{backend_url}/submit/", json={"answers": user_answers})
    if response.status_code != 200:
        click.echo("Erro ao enviar respostas para o servidor.")
        return

    result = response.json()
    click.echo(f"\nVocê acertou {result['score']} de {result['total']} questões.")

if __name__ == "__main__":
    play_quiz()
