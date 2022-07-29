from sqlalchemy.orm import Session

from store import schemas
from store.models import Product, Category


def get_all_products_(db: Session) -> list:
    return db.query(Product).all()


def get_all_categories_(db: Session) -> list:
    return db.query(Category).all()


def get_product_(db: Session, product_id: int) -> Product:
    return db.query(Product).filter(Product.id == product_id).first()


def get_category_(db: Session, category_id: int) -> Category:
    return db.query(Category).filter(Category.id == category_id).first()


def get_product_by_category_(db: Session, category_id: int) -> list:
    return db.query(Product).filter(Product.category_id == category_id).all()


def create_product_(db: Session, product: schemas.ProductCreate) -> schemas.ProductCreate:
    db.add(Product(**product.dict()))
    db.commit()
    return product


def create_category_(db: Session, category: schemas.CategoryCreate) -> schemas.CategoryCreate:
    db.add(Category(**category.dict()))
    db.commit()
    return category
