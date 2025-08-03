from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    quantity: int
    price: float

class ProductOut(ProductCreate):
    id: int
