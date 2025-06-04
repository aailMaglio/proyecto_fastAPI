import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
from models import Base, IngredienteDB

class Ingrediente(BaseModel):
    id: int = None
    nombre: str

class Ingredientes(BaseModel):
    ingredientes: List[Ingrediente]

app = FastAPI()

origins = [
    "http://localhost:1000", "http://localhost:5173", "http://localhost:5050",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ingredientes", response_model=Ingredientes)
def get_ingredientes(db: Session = Depends(get_db)):
    ingredientes = db.query(IngredienteDB).all()
    return Ingredientes(ingredientes)

@app.post("/ingredientes", response_model=Ingrediente)
def add_ingrediente(ingrediente: Ingrediente, db: Session = Depends(get_db)):
    db_ingrediente = IngredienteDB(nombre=ingrediente.nombre)
    db.add(db_ingrediente)
    db.commit()
    db.refresh(db_ingrediente)
    return db_ingrediente

@app.delete("/ingredientes/{id}", response_model=Ingrediente)
def delete_ingrediente(id: int, db: Session = Depends(get_db)):
    ingrediente = db.query(IngredienteDB).filter(IngredienteDB.id == id).first()
    if ingrediente is None:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    db.delete(ingrediente)
    db.commit()
    return ingrediente

@app.put("/ingredientes/{id}", response_model=Ingrediente)
def update_ingrediente(id: int, ingrediente: Ingrediente, db: Session = Depends(get_db)):
    db_ingrediente = db.query(IngredienteDB).filter(IngredienteDB.id == id).first()
    if db_ingrediente is None:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    db_ingrediente.nombre = ingrediente.nombre
    db.commit()
    db.refresh(db_ingrediente)
    return db_ingrediente

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1000)