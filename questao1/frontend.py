import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para adicionar tarefa
    def add_task():
        description = input_text.value.strip()
        if description:
            # Corrigindo o payload da solicitação para incluir a chave "description"
            response = requests.post("http://localhost:8080/items/", json={"description": description})
            if response.status_code == 200:
                input_text.value = ""
                update_tasks()
            else:
                page.snackbar_text = "Failed to add item"

    # Função para chamar add_task sem argumentos
    def on_submit_click():
        add_task()

    # Elementos da UI
    input_text = ft.TextField(hint_text="Add a new task", width=300, autofocus=True)
    submit_button = ft.ElevatedButton(text="Add", on_click=lambda _: on_submit_click())
    task_list = ft.ListView(expand=True)
    
    # Função para deletar tarefa
    def delete_task(item_id):
        response = requests.delete(f"http://localhost:8080/items/{item_id}")
        if response.status_code == 200:
            update_tasks()
        else:
            page.snackbar_text = "Failed to delete item"

    # Função para atualizar tarefa
    def update_task(item_id, new_description):
        response = requests.put(f"http://localhost:8080/items/{item_id}", json={"description": new_description})
        if response.status_code == 200:
            update_tasks()
        else:
            page.snackbar_text = "Failed to update item"

    # Função para editar tarefa
    def edit_task(item_id, description):
        new_description = page.prompt("Edit Task", initial_value=description)
        if new_description is not None:
            update_task(item_id, new_description)

    # Função para atualizar a lista de tarefas
    def update_tasks():
        response = requests.get("http://localhost:8080/items/")
        task_list.controls.clear()
        if response.status_code == 200:
            items = response.json()
            for item in items:
                item_id = item['id']
                description = item['description']
                delete_button = ft.Button(text="Delete", on_click=lambda _, item_id=item_id: delete_task(item_id))
                edit_button = ft.Button(text="Edit", on_click=lambda _, item_id=item_id, description=description: edit_task(item_id, description))
                task_list.controls.append(ft.Row(children=[
                    ft.ListTile(title=ft.Text(description)),
                    delete_button,
                    edit_button
                ]))

    # Adicionar elementos à página
    page.add(input_text, submit_button, task_list)
    update_tasks()

ft.app(target=main, port=8000)
