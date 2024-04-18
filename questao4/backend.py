from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Name(BaseModel):
    name: str

@app.post("/getName")
async def get_name(name: Name):
    return {"message": f"Olá, {name.name}! Seu nome foi recebido com sucesso."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)