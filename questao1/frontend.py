import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    input_text = ft.TextField(hint_text="Add a new task", width=300, autofocus=True)
    assignee_dropdown = ft.Dropdown(options=["Person A", "Person B", "Person C"], label="Assignee")
    submit_button = ft.ElevatedButton(text="Add", on_click=lambda _: add_task(page, input_text, assignee_dropdown))
    task_list = ft.ListView(expand=True)
    
    # Função para adicionar tarefa
    def add_task(page, input_text, assignee_dropdown):
        description = input_text.value.strip()
        assignee = assignee_dropdown.value
        if description:
            response = requests.post("http://localhost:8080/items/", json={"description": description, "assignee": assignee})
            if response.status_code == 200:
                input_text.value = ""
                update_tasks(page, task_list)
            else:
                page.snackbar_text = "Failed to add item"
        page.update()

    # Função para deletar tarefa
    def delete_task(page, item_id):
        response = requests.delete(f"http://localhost:8080/items/{item_id}/")
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to delete item"
        page.update()

    # Função para editar tarefa
    def edit_task(page, item_id, new_description):
        response = requests.put(f"http://localhost:8080/items/{item_id}/", json={"description": new_description})
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to edit item"
        page.update()

    # Função para atualizar a lista de tarefas
    def update_tasks(page, task_list):
        response = requests.get("http://localhost:8080/items/")
        task_list.controls.clear()
        if response.status_code == 200:
            items = response.json()
            for index, item in enumerate(items):
                delete_button = ft.Button(text="Delete", on_click=lambda _, idx=index: delete_task(page, idx))
                edit_button = ft.Button(text="Edit", on_click=lambda _, idx=index: edit_task(page, idx, item['description']))
                task_list.controls.append(ft.Row(items=[
                    ft.ListTile(title=ft.Text(item['description'])),
                    ft.ListTile(title=ft.Text(item['assignee'])),
                    delete_button,
                    edit_button
                ]))
        page.update()

    # Adicionar elementos à página
    page.add(input_text, assignee_dropdown, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)