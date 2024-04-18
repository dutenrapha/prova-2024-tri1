import flet as ft
import requests

def main(page: ft.Page):
    page.title = "User Registration"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    name_input = ft.TextField(hint_text="Name", width=300)
    email_input = ft.TextField(hint_text="E-mail", width=300)
    password_input = ft.TextField(hint_text="Password", width=300, password=True)
    register_button = ft.ElevatedButton(text="Register", on_click=register_user)
    error_text = ft.Text("", color="red")

    # Função para registrar um novo usuário
    def register_user():
        name = name_input.value.strip()
        email = email_input.value.strip()
        password = password_input.value.strip()

        # Validar se todos os campos foram preenchidos
        if not name or not email or not password:
            error_text.value = "All fields are required"
            return

        # Enviar dados para o backend
        try:
            response = requests.post("http://localhost:8080/register/", json={"name": name, "email": email, "password": password})
            if response.status_code == 200:
                error_text.value = "User registered successfully"
                clear_fields()
            else:
                error_text.value = "Failed to register user"
        except requests.exceptions.RequestException as e:
            error_text.value = "Failed to connect to the server"

    # Função para limpar os campos de entrada
    def clear_fields():
        name_input.value = ""
        email_input.value = ""
        password_input.value = ""
        error_text.value = ""

    # Adicionar elementos à página
    page.add(name_input, email_input, password_input, register_button, error_text)

ft.app(target=main, port=8000)