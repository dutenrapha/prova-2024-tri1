from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import  JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="index.html")


# Modelo de dados para uma pergunta
class Question(BaseModel):
    text: str
    options: List[str]
    answer: int  # índice da resposta correta

# Lista de perguntas
questions = [
    Question(text="What is the capital of France?", options=["London", "Berlin", "Paris", "Rome", "Madrid"], answer=2),
    Question(text="What is 2 + 2?", options=["3", "4", "5", "6", "2"], answer=1),
    Question(text="Who wrote 'Macbeth'?", options=["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy", "Mark Twain"], answer=1),
    Question(text="Which planet is known as the Red Planet?", options=["Earth", "Venus", "Mars", "Jupiter", "Saturn"], answer=2),
    Question(text="What is the largest ocean on Earth?", options=["Atlantic", "Indian", "Arctic", "Pacific", "Southern"], answer=3)
]

@app.get("/", response_class=JSONResponse)
async def display_quiz(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request, "TESTE questions": questions})

# @app.get("/questions/", response_model=List[Question])
# async def get_questions():
#     return questions

# Modelo para as respostas do usuário
class UserAnswers(BaseModel):
    answers: List[Optional[int]]

# Rota para enviar as respostas do usuário e calcular a pontuação
@app.post("/submit/", response_class=JSONResponse)
async def submit_answers(user_answers: str = Form(...)):
    user_answers_list = [int(answer) for answer in user_answers.split(',')]
    if len(user_answers_list) != len(questions):
        raise HTTPException(status_code=400, detail="Número de respostas inválido")
    score = sum(1 for i, answer in enumerate(user_answers_list) if answer == questions[i].answer)
    return templates.TemplateResponse("result.html", {"score": score, "total": len(questions)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
