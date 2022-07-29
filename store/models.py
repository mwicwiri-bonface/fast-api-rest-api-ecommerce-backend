from sqlalchemy import Integer, Column, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from core.settings import Base, engine


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(255), nullable=False)
    products = relationship("Product", backref="category", cascade="all, delete-orphan")

    def __repr__(self):
        return "<Category(id='%s', name='%s')>" % (self.id, self.name)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(255), nullable=False)
    description = Column(Text(), nullable=False)
    price = Column(Float(), nullable=False)
    category_id = Column(Integer(), ForeignKey("category.id"), nullable=False)
    user_id = Column(Integer(), ForeignKey("user.id"), nullable=False)
    order_items = relationship("OrderItem", backref="product", cascade="all, delete-orphan")

    def __repr__(self):
        return "<Product(id='%s', name='%s')>" % (self.id, self.name)


Base.metadata.create_all(engine)
