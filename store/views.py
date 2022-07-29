from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from core.settings import get_db
from store import schemas
from store.helpers import get_all_products_, get_all_categories_, get_product_, create_product_, create_category_

router = APIRouter(
    prefix="/store",
    tags=['Store']
)


@router.get('/products/', status_code=status.HTTP_200_OK, response_model=list[schemas.ProductBase])
async def get_products(db: Session = Depends(get_db)):
    products = get_all_products_(db)
    return products


@router.get('/categories/', status_code=status.HTTP_200_OK, response_model=list[schemas.CategoryBase])
async def get_categories(db: Session = Depends(get_db)):
    categories = get_all_categories_(db)
    return categories


@router.get('/products/{product_id}/', status_code=status.HTTP_200_OK, response_model=schemas.ProductBase)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_(db, product_id)
    return product


@router.post('/products/', status_code=status.HTTP_201_CREATED, response_model=schemas.ProductBase)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = create_product_(db, product)
    return product


@router.post('/categories/', status_code=status.HTTP_201_CREATED, response_model=schemas.CategoryCreate)
async def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = create_category_(db, category)
    return category


