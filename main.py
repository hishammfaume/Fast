from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated, List
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
    created_at: str
    updated_at: str

class ProductModel(ProductBase):
    id: int
    class Config:
        form_attributes = True


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    role: str
    created_at: str
    updated_at: str

class UserModel(UserBase):
    id: int
    class Config:
        form_attributes = True
        
        
class CategoryBase(BaseModel):
    name: str
    created_at: str
    updated_at: str
    
class CategoryModel(CategoryBase):
    id: int
    class Config:
        form_attributes = True

class BrandBase(BaseModel):
    name: str
    created_at: str
    updated_at: str

class BrandModel(BrandBase):
    id: int
    class Config:
        form_attributes = True
        

def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
        
        

db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine) # Create the tables in the database

@app.post("/product/", response_model=ProductModel)
async def create_product(product: ProductBase, database: db_dependency):
    db_product = models.Product(**product.model_dump())
    database.add(db_product)
    database.commit()
    database.refresh(db_product)
    return db_product

@app.get("/product/", response_model=List[ProductModel])
async def read_products(database: db_dependency, skip: int=0,limit: int=100):
    products = database.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.post("/user/", response_model=UserModel)
async def create_user(user: UserBase, database: db_dependency):
    db_user = models.User(**user.model_dump())
    database.add(db_user)
    database.commit()
    database.refresh(db_user)
    return db_user


@app.post("/category/", response_model=CategoryModel)
async def create_category(category: CategoryBase, database: db_dependency):
    db_category = models.Category(**category.model_dump())
    database.add(db_category)
    database.commit()
    database.refresh(db_category)
    return db_category

@app.post("/brand/", response_model=BrandModel)
async def create_brand(brand: BrandBase, database: db_dependency):
    db_brand = models.Brand(**brand.model_dump())
    database.add(db_brand)
    database.commit()
    database.refresh(db_brand)
    return db_brand

@app.get("/brand/", response_model=List[BrandModel])
async def read_brands(database: db_dependency, skip=0,limit=100):
    brands = database.query(models.Brand).offset(skip).limit(limit).all()
    return brands