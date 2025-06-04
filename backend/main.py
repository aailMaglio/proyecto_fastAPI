import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Ingrediente(BaseModel):
    id: int = None
    nombre: str

class Ingredientes(BaseModel):
    ingredientes: List[Ingrediente]



app = FastAPI()

origins = [
    "http://localhost:1000", "http://localhost:5173"
]

#cross-origin resource sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memoria_db = {"ingredientes": []}


@app.get("/ingredientes", response_model=Ingredientes)
def get_ingredientes():
    return Ingredientes(ingredientes=memoria_db["ingredientes"])  


@app.post("/ingredientes", response_model=Ingrediente)
def add_ingrediente(ingrediente: Ingrediente):
    if ingrediente.id is None:
        ingrediente.id = len(memoria_db["ingredientes"]) + 1
    memoria_db["ingredientes"].append(ingrediente)
    return ingrediente

@app.delete("/ingredientes/{id}", response_model=Ingrediente)
def delete_ingrediente(id: int):
    for i, ingrediente in enumerate(memoria_db["ingredientes"]):
        if ingrediente.id == id:
            return memoria_db["ingredientes"].pop(i)
    return {"error": "Ingrediente no encontrado"}

@app.put("/ingredientes/{id}", response_model=Ingrediente)
def update_ingrediente(id: int, ingrediente: Ingrediente):
    for i, ing in enumerate(memoria_db["ingredientes"]):
        if ing.id == id:
            memoria_db["ingredientes"][i] = ingrediente
            return ingrediente
    return {"error": "Ingrediente no encontrado"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1000)