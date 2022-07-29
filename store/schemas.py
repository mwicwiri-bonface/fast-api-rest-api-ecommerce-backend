from typing import Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    products: list

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: float
    description: str = None

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    category: Optional[CategoryCreate]
