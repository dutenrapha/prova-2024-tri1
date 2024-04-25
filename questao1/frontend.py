import flet as ft
import requests

def main(page: ft.Page):
    page.title = "To-Do List App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Elementos da UI
    input_text = ft.TextField(hint_text="Add a new task", width=300, autofocus=True)
    submit_button = ft.ElevatedButton(text="Add", on_click=lambda _: add_task(page, input_text))
    task_list = ft.ListView(expand=True)
    
    # Dropdown list para ações
    actions_dropdown = ft.Dropdown(
        options=["Delete", "Update"],  # Usando 'options' em vez de 'items'
        hint_text="Select Action",
        on_change=lambda selected_action: handle_action(page, selected_action, task_list)
    )

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
                task_list.controls.append(
                    ft.ListTile(
                        title=ft.Text(item['description']),
                        trailing=actions_dropdown  # Adicionando dropdown para cada item
                    )
                )
        page.update()

    # Função para lidar com a ação selecionada na dropdown list
    def handle_action(page, selected_action, task_list):
        selected_item_index = task_list.controls.index(page.active_element)
        selected_item_id = items[selected_item_index]['id']  # Supondo que 'id' está presente nos itens
        if selected_action == "Delete":
            delete_task(selected_item_id)
        elif selected_action == "Update":
            update_task(selected_item_id)
        update_tasks(page, task_list)

    # Funções para atualizar e deletar tarefa
    def delete_task(item_id):
        requests.delete(f"http://localhost:8080/items/{item_id}")

    def update_task(item_id):
        # Lógica para atualizar a tarefa
        new_description = input("Enter updated description: ")
        requests.put(f"http://localhost:8080/items/{item_id}", json={"description": new_description})

    # Adicionar elementos à página
    page.add(input_text, submit_button, task_list)
    update_tasks(page, task_list)

ft.app(target=main, port=8000)
