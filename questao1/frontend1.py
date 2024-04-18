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
    def delete_task(page, task_list, item_id):
        response = requests.delete(f"http://localhost:8080/items/{item_id}/")
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to delete item"
        page.update()
        
    def edit_task(page, task_list, item_id, new_description):
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
                task_list.controls.append(
                    ft.ListTile(
                        title=ft.Text(item['description']),
                        trailing=ft.IconButton(
                            icon="delete",
                            on_click=lambda _, idx=index: delete_task(page, task_list, idx)  # Correção aqui
                        )
                    )
                )
        page.update()

    # Adicionar elementos à página
    page.add(input_text, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)
