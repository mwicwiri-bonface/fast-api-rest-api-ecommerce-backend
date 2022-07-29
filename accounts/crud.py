from argon2.exceptions import VerifyMismatchError, InvalidHash
from fastapi import HTTPException
from sqlalchemy.orm import Session
from argon2 import PasswordHasher
from starlette import status

from . import models, schemas

ph = PasswordHasher()


def hash_password(password: str):
    return ph.hash(password)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def verify_user_by_username_(db: Session, username: str, password: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if not db_user:
        return None
    try:
        ph.verify(db_user.password, password)
    except (VerifyMismatchError, InvalidHash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    if ph.check_needs_rehash(db_user.password):
        db_user.password = ph.hash(password)
        db.commit()
    return db_user


def get_users_(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user_(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(**user.dict())
    db_user.password = hashed_password
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_pk_(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
