import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    input_text = ft.TextField(hint_text="Add a new task", width=300, autofocus=True)
    submit_button = ft.ElevatedButton(text="Add", on_click=lambda _: add_task(page, input_text))
    task_list = ft.ListView(expand=True)
    
    # Função para adicionar tarefa
    def add_task(page, input_text):
        description = input_text.value.strip()
        if description:
            response = requests.post("http://localhost:8080/items/", json={"description": description})
            if response.status_code == 200:
                input_text.value = ""
                update_tasks(page, task_list)
            else:
                page.snackbar_text = "Failed to add item"
        page.update()

    # Função para atualizar a lista de tarefas
    def update_tasks(page, task_list):
        response = requests.get("http://localhost:8080/items/")
        task_list.controls.clear()
        if response.status_code == 200:
            items = response.json()
            for item in items:
                item_row = ft.Row(
                    children=[
                        ft.ListTile(title=ft.Text(item['description'])),
                        ft.Button(text="Edit", on_click=lambda _, item_id=item['id']: edit_task(page, item_id)),
                        ft.Button(text="Delete", on_click=lambda _, item_id=item['id']: delete_task(page, item_id))
                    ]
                )
                task_list.controls.append(item_row)
        page.update()

    # Função para editar tarefa
    def edit_task(page, item_id):
        new_description = ft.TextField(hint_text="Edit task", width=300)
        confirm_button = ft.Button(text="Confirm", on_click=lambda _: confirm_edit(page, item_id, new_description))
        page.add(new_description, confirm_button)
        page.update()

    def confirm_edit(page, item_id, new_description_field):
        new_description = new_description_field.value.strip()
        if new_description:
            response = requests.put(f"http://localhost:8080/items/{item_id}", json={"description": new_description})
            if response.status_code == 200:
                page.remove(new_description_field)
                update_tasks(page, task_list)
            else:
                page.snackbar_text = "Failed to edit item"
        page.update()

    # Função para deletar tarefa
    def delete_task(page, item_id):
        response = requests.delete(f"http://localhost:8080/items/{item_id}")
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to delete item"
        page.update()

    # Adicionar elementos à página
    page.add(input_text, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)
