from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    description: str
    assignee: str = None

# Lista temporária para armazenar as tarefas
tasks: List[Item] = []
next_id = 1

@app.post("/items/")
async def add_item(item: Item):
    global next_id
    item.id = next_id
    next_id += 1
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global tasks
    for i, item in enumerate(tasks):
        if item.id == item_id:
            del tasks[i]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
async def edit_item(item_id: int, new_item: Item):
    global tasks
    for item in tasks:
        if item.id == item_id:
            item.description = new_item.description
            return {"message": "Item edited successfully"}
    raise HTTPException(status_code=404, detail="Item not found")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)