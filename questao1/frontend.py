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

    # Função para deletar tarefa
    def delete_task(task_index):
        response = requests.delete(f"http://localhost:8080/items/{task_index}")
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to delete item"
        page.update()

    # Função para editar tarefa
    def edit_task(task_index, new_description):
        response = requests.put(f"http://localhost:8080/items/{task_index}", json={"description": new_description})
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
                task_item = ft.ListTile(title=ft.Text(item['description']))
                delete_button = ft.ElevatedButton(text="Delete", on_click=lambda _, idx=index: delete_task(idx))
                edit_button = ft.ElevatedButton(text="Edit", on_click=lambda _, idx=index: edit_task(idx, item['description']))
                task_item.content = [delete_button, edit_button]
                task_list.controls.append(task_item)
        page.update()

    # Adicionar elementos à página
    page.add(input_text, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)


