from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Modelo de dados para o usuário
class User(BaseModel):
    name: str
    email: EmailStr
    password: str

# Lista de usuários (simulando um banco de dados)
users_db: List[User] = []

# Endpoint para registrar um novo usuário
@app.post("/register/")
async def register_user(user: User):
    # Verifica se o e-mail já está em uso
    if any(u.email == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="E-mail already registered")
    users_db.append(user)
    return {"message": "User registered successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)