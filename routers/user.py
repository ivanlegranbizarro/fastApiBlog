from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from views import user


import schemas
import models

router = APIRouter()


@router.post("/", response_model=schemas.ShowUser, status_code=201)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get("", response_model=List[schemas.ShowUser])
def show_users(db: Session = Depends(get_db)):
    return user.show_users(db)


@router.get("/{user_id}", response_model=schemas.ShowUser)
def show_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.show_user_by_id(user_id, db)


@router.delete("/{user_id}", status_code=204)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.delete_user_by_id(user_id, db)


@router.put("/{user_id}", status_code=200)
def update_user_by_id(
    user_id: int, request: schemas.User, db: Session = Depends(get_db)
):
    return user.update_user_by_id(user_id, request, db)
