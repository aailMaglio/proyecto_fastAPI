import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Lista(BaseModel):
    nombre: str

class Listas(BaseModel):
    listas: List[Lista]



app = FastAPI()

origins = [
    "http://localhost:3000",
]

#cross-origin resource sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memoria_db = {"listas": []}


@app.get("/listas", response_model=Listas)
def get_listas():
    return Listas(listas=memoria_db["listas"])  


@app.post("/listas", response_model=Lista)
def add_lista(lista: Lista):
    memoria_db["listas"].append(lista)
    return lista


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)