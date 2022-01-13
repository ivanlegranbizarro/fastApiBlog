from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from views import blog

import schemas

router = APIRouter()


@router.post("", status_code=201)
def create(request: schemas.Blog, db: SessionLocal = Depends(get_db)):
    return blog.create(request, db)


@router.get("", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: SessionLocal = Depends(get_db)):
    return blog.get_all_blogs(db)


@router.get("/{blog_id}", status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return blog.get_blog_by_id(blog_id, db)


@router.delete("/{blog_id}", status_code=204)
def delete_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return blog.delete_blog_by_id(blog_id, db)


@router.put("/blog/{blog_id}", status_code=200)
def update_blog_by_id(
    blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)
):
    return blog.update_blog_by_id(blog_id, request, db)
