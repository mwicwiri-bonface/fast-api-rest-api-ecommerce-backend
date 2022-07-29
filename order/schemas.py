from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OrderSchema(BaseModel):
    id: int
    user_id: int
    status: Optional[Enum] = None
    created_at: str
    updated_at: str


class OrderItemSchema(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    created_at: str
    updated_at: str
