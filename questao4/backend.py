from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitindo solicitações CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lista de tarefas
tasks = []

# Rota para adicionar uma nova tarefa
@app.post("/tasks/")
async def add_task(task: str):
    tasks.append(task)
    return JSONResponse(content={"message": "Task added successfully"})

# Rota para obter todas as tarefas
@app.get("/tasks/")
async def get_tasks():
    return JSONResponse(content={"tasks": tasks})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)