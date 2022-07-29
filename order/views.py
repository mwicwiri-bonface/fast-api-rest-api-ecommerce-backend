from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from accounts.auth import UserSchema, get_current_active_user
from core.settings import get_db
from order import schemas
from order.helpers import get_current_user_orders_

router = APIRouter(
    prefix="/order",
    tags=['Order']
)


@router.get("/orders/", status_code=status.HTTP_200_OK, response_model=list[schemas.OrderSchema])
async def get_orders(current_user: UserSchema = Depends(get_current_active_user), db: Session = Depends(get_db)):
    orders = get_current_user_orders_(db=db, user_id=current_user.id)
    return orders

