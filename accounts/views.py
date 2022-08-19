from typing import List

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from pydantic import EmailStr
from sqlalchemy.orm import Session
from starlette import status

from accounts import schemas
from accounts.auth import get_current_active_user, UserSchema, get_user_by_username_, oauth2_scheme
from accounts.crud import get_user_by_email, create_user_, get_users_, get_user
from accounts.schemas import UserUpdate
from core.email import sending_email_
from core.settings import get_db

router = APIRouter(
    prefix="/accounts",
    tags=['Accounts']
)


async def send_verification_email(email: EmailStr):
    """ Send verification email to user """
    subject = "Verify your email"
    msg = f"Please verify your email by clicking on the link: http://localhost:8000/accounts/verify?email={email}"
    await sending_email_(subject=subject, html=msg, recipients=[email])


@router.post("/users/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
async def create_user(background_tasks: BackgroundTasks, user: schemas.UserCreate, db: Session = Depends(get_db)):
    """ Create a new user and send verification email """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = create_user_(db, user)
    background_tasks.add_task(send_verification_email, user.email)
    return user


@router.get("/users/", status_code=status.HTTP_200_OK, response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_active_user)):
    """ Get all users """
    print(current_user)
    users = get_users_(db, limit=20)
    return users


@router.put("/users/", status_code=status.HTTP_200_OK, response_model=schemas.User)
async def update_user(user: UserUpdate, db: Session = Depends(get_db),
                      current_user: UserSchema = Depends(get_current_active_user)):
    """ Update user """
    db_user = get_user_by_username_(db=db, username=current_user.username)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db_user.full_name = user.full_name
    db_user.is_active = user.is_active
    db.commit()
    return current_user


@router.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.get('/verify-email/{pk}', status_code=status.HTTP_200_OK, response_model=schemas.User)
async def verify_email(pk: int, db: Session = Depends(get_db)):
    user = get_user(db, pk)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.is_active = True
    db.commit()
    return user
