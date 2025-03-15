from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
  
)

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    category_id: int
    brand_id: int
    rating: float