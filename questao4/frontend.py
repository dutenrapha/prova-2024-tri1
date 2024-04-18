import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Age Checker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    name_input = ft.TextField(hint_text="Enter your name", width=300, autofocus=True)
    age_input = ft.TextField(hint_text="Enter your age", width=300)
    submit_button = ft.ElevatedButton(text="Submit", on_click=lambda _: check_age(page, name_input, age_input))
    result_text = ft.Text("", width=300)

    # Função para verificar a idade
    def check_age(page, name_input, age_input):
        name = name_input.value.strip()
        age = age_input.value.strip()
        if name and age:
            try:
                age = int(age)
                response = requests.post("http://localhost:8080/person/", json={"name": name, "age": age})
                if response.status_code == 200:
                    result = response.json()
                    message = result["message"]
                    is_minor = result["is_minor"]
                    result_text.text = f"{message} Você é {'menor' if is_minor else 'maior'} de idade."
                else:
                    result_text.text = "Failed to submit data"
            except ValueError:
                result_text.text = "Invalid age. Please enter a valid number."
        else:
            result_text.text = "Please enter your name and age."
        page.update()

    # Adicionar elementos à página
    page.add(name_input, age_input, submit_button, result_text)

ft.app(target=main, port=8000)
