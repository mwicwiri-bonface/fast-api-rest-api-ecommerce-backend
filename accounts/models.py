import enum

from sqlalchemy import Integer, Column, String, DateTime, func, Enum, Boolean
from sqlalchemy.orm import relationship

from core.settings import Base, engine


class RoleEnum(enum.Enum):
    customer = "customer"
    admin = "admin"
    super_admin = "super_admin"


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    full_name = Column(String(255), nullable=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.customer)
    products = relationship("Product", backref="user", cascade="all, delete-orphan")
    orders = relationship("Order", backref="user", cascade="all, delete-orphan")
    updated_at = Column(DateTime, onupdate=func.now())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return "<User(id='%s', username='%s', email='%s')>" % (self.id, self.username, self.email)


Base.metadata.create_all(engine)
