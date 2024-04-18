from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/cadastrar")
async def cadastrar(titulo: str = Form(...), preco: float = Form(...)):
    # Aqui você pode processar os dados recebidos, como salvar em um banco de dados
    # Por enquanto, apenas retornaremos os dados recebidos
    return {"titulo": titulo, "preco": preco}

@app.get("/")
async def main_page():
    # Aqui você pode retornar o HTML com o formulário
    return {"titulo": titulo, "preco": preco}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)