from fastapi import Depends
from database import SessionLocal, get_db
import schemas
import models
from werkzeug.security import generate_password_hash

from fastapi.exceptions import HTTPException


def create_user(request: schemas.User, db: SessionLocal = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=generate_password_hash(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show_users(db: SessionLocal = Depends(get_db)):
    users = db.query(models.User).all()
    return users


def show_user_by_id(user_id: int, db: SessionLocal = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return user


def delete_user_by_id(user_id: int, db: SessionLocal = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    db.delete(user)
    db.commit()
    return {"message": f"User with id {user_id} deleted"}


def update_user_by_id(
    user_id: int, request: schemas.User, db: SessionLocal = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    user.name = request.name
    user.email = request.email
    db.commit()
    db.refresh(user)
    return user
