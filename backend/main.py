import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Ingrediente(BaseModel):
    nombre: str

class Ingredientes(BaseModel):
    ingredientes: Ingrediente[Ingrediente]



app = FastAPI()

origins = [
    "http://localhost:5000", "http://localhost:5173/", "http://localhost:3000",
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
    return Ingredientes(listas=memoria_db["ingredientes"])  


@app.post("/ingredientes", response_model=Ingrediente)
def add_ingrediente(ingrediente: List):
    memoria_db["ingredientes"].append(ingrediente)
    return ingrediente


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)