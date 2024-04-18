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

    # Função para deletar uma tarefa
    def delete_task(page, item_id):
        response = requests.delete(f"http://localhost:8080/items/{item_id}")
        if response.status_code == 200:
            update_tasks(page, task_list)
        else:
            page.snackbar_text = "Failed to delete item"
        page.update()

    # Função para editar uma tarefa
    def edit_task(page, item_id, new_description):
        response = requests.put(f"http://localhost:8080/items/{item_id}", json={"description": new_description})
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
            for item in items:
                # Criar botões de delete e edit para cada item
                delete_button = ft.Button(text="Delete", on_click=lambda _, item_id=item['id']: delete_task(page, item_id))
                edit_button = ft.Button(text="Edit", on_click=lambda _, item_id=item['id']: edit_task_dialog(page, item_id, item['description']))
                # Adicionar o item à lista de tarefas junto com os botões de delete e edit
                task_list.controls.append(ft.Row(children=[ft.ListTile(title=ft.Text(item['description'])), delete_button, edit_button]))
        page.update()

    # Função para exibir um diálogo modal para editar uma tarefa
    def edit_task_dialog(page, item_id, current_description):
        # Criar um campo de texto editável dentro de um diálogo modal
        edit_text_field = ft.TextField(value=current_description, width=300)
        dialog = ft.Dialog(title="Edit Task", children=[edit_text_field], actions=[
            ft.DialogAction(text="Cancel", on_click=lambda _: page.close_dialog()),
            ft.DialogAction(text="Save", on_click=lambda _: save_edited_task(page, item_id, edit_text_field.value))
        ])
        page.open_dialog(dialog)

    # Função para salvar uma tarefa editada
    def save_edited_task(page, item_id, new_description):
        edit_task(page, item_id, new_description)
        page.close_dialog()

    # Adicionar elementos à página
    page.add(input_text, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)