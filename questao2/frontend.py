import flet as ft
import aiohttp
import uvicorn

base_url = "http://localhost:8080"

class QuizApp(ft.UserControl):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.questions = []
        self.questions_display = None

    async def load_questions(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/") as response:
                self.questions = await response.json()
        await self.update_async()

    async def submit_answers(self, answers):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/submit/", data=answers) as response:
                result = await response.text()
        print(result)  # For debugging purposes, you can remove this line in production

    def build(self):
        self.question_inputs = [ft.TextInput() for _ in range(len(self.questions))]  # Create text inputs for questions
        self.submit_button = ft.buttons.Button(text="Submit", on_click=self.submit_clicked)
        self.questions_display = ft.Column()  # Initialize questions_display here
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    [ft.Text(value="Quiz", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                self.questions_display,
                self.submit_button,
            ],
        )

    async def submit_clicked(self, e):
        answers = ",".join([input.value for input in self.question_inputs])
        await self.submit_answers(answers)

    async def update_async(self):
        self.questions_display.controls = []
        for idx, question in enumerate(self.questions):
            question_label = ft.Text(value=question["text"])
            self.questions_display.controls.append(ft.Row(controls=[question_label, self.question_inputs[idx]]))


async def main(page: ft.Page):
    base_url = "http://localhost:8080"  # Update with your FastAPI server URL
    page.title = "Quiz App TESTE"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    quiz_app = QuizApp(base_url)
    await quiz_app.load_questions()  # Load questions before building
    quiz_app.build()  # Build after loading questions
    await page.add_async(quiz_app)


ft.app(main)
