from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    description: str

# Lista temporária para armazenar as tarefas
tasks: List[Item] = []

@app.post("/items/")
async def add_task(item: Item):
    if not item.description:
        raise HTTPException(status_code=422, detail="Item description cannot be empty")
    
    tasks.append(item)
    return {"message": "Item added successfully"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks

@app.delete("/items/{item_id}")
async def delete_task(item_id: int):
    global tasks
    tasks = [item for item in tasks if item.id != item_id]
    return {"message": "Item deleted successfully"}

@app.put("/items/{item_id}")
async def update_task(item_id: int, updated_item: Item):
    for index, item in enumerate(tasks):
        if item.id == item_id:
            tasks[index] = updated_item
            return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)