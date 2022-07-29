from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, String, Enum
from sqlalchemy.orm import relationship

from core.settings import Base, engine


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    token = Column(String(255), nullable=False)
    order_items = relationship("OrderItem", backref="order", cascade="all, delete-orphan")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    status = Column(Enum("pending", "paid", "cancelled"), default="pending")
    updated_at = Column(DateTime, onupdate=func.now())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return "<Order(id='%s', user_id='%s')>" % (self.id, self.user_id)


class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return "<OrderItem(id='%s', order_id='%s', product_id='%s')>" % (self.id, self.order_id, self.product_id)


Base.metadata.create_all(engine)
