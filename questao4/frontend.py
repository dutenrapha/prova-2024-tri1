import flet
import flet.fastapi as flet_fastapi

async def main(page: flet.Page):
    counter_text = flet.Text("0", size=50, data=0)

    async def add_click(e):
        global counter_text
        counter_text.data += 1
        counter_text.value = str(counter_text.data)
        await counter_text.update_async()

    page.floating_action_button = flet.FloatingActionButton(
        icon=flet.icons.ADD, on_click=add_click
    )

    await page.add_async(
        flet.Container(
            counter_text, alignment=flet.alignment.center, expand=True
        )
    )

app = flet_fastapi.app(main)

if __name__ == "__main__":
    app.run()
