from sqlalchemy.orm import Session

from order.models import Order


def get_current_user_orders_(db: Session, user_id: int) -> list:
    return db.query(Order).filter(Order.user_id == user_id).all()

