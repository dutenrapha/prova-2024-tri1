from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    description: str
    id: Optional[int] = None

# Lista temporária para armazenar as items
tasks: List[Item] = []

@app.post("/items/")
async def add_item(item: Item):
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/")
async def get_items(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": tasks})

@app.delete("/items/{item_id}")
def deletar_item(item_id: int, request: Request):
    global tasks
    tasks = [item for item in tasks if item.id != item_id]
    return RedirectResponse(url="/items/", status_code=303)  # Redireciona para a rota com "index"

@app.put("/items/{item_id}")
def atualizar_item(item_id: int, item: Item, request: Request):
    for task in tasks:
        if task.id == item_id:
            task.description = item.description
            return RedirectResponse(url="/items/", status_code=303)  # Redireciona para a rota com "index"
    raise HTTPException(status_code=404, detail=f"Item com ID {item_id} não encontrado.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
