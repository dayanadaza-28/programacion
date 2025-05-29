from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from supabase import create_client, client
import os

SUPABASE_URL = os.getenv("SUPABASE_BD_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_BD_KEY","contraseña")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# Creacion de Modelos
class Product(BaseModel):
  id: int
  nombre: str
  cantidad: int
  precio: float

class User(BaseModel):
  id: int
  name: str
  email: str

class Order(BaseModel):
  id: int
  user_id: int
  product_ids: List[int]

@app.post("/products") # Ruta
def create_product(prod: Product): #Endpoint
  try:
    supabase.table("products").insert(prod.model_dump()).execute()
    return {"status":"ok", "msg":"Guardado con exito"}
  except:
    return {"status": "error", "msg": "Error en el servidor"}


@app.get("/products", response_model=List[Product]) # Ruta
def list_products():
  pass