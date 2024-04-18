from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    description: str
    assigned_to: str 

# Lista temporária para armazenar as tarefas
tasks: List[Item] = []

@app.post("/items/", response_model=Item)
async def add_item(item: Item):
    tasks.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def get_items():
    return tasks

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    try:
        del tasks[item_id]
        return {"message": f"Item with ID {item_id} deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    try:
        tasks[item_id] = updated_item
        return {"message": f"Item with ID {item_id} updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
