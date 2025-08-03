from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from app.db.async_db import db
from app.schemas.schemas import ProductCreate, ProductOut
from typing import List
import asyncio

router = APIRouter()

@router.on_event("startup")
async def startup():
    await db.init_pool()

@router.get("/products/", response_model=List[ProductOut])
async def list_products():
    prods = await db.fetch_products()
    return prods

@router.post("/products/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    prod_id = await db.add_product(product.name, product.category, product.quantity, product.price)
    if prod_id is None:
        raise HTTPException(status_code=409, detail="Product already exists in this category.")
    return {
        'id': prod_id,
        'name': product.name,
        'category': product.category,
        'quantity': product.quantity,
        'price': product.price
    }
