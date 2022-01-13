from http.client import HTTPException
from fastapi import Depends
from database import SessionLocal, get_db
import models
from sqlalchemy.orm import Session


def create(request: models.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=request.title, body=request.body, user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all_blogs(db: SessionLocal = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {blog_id} not found")
    return blog


def delete_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {blog_id} not found")
    db.delete(blog)
    db.commit()
    return blog


def update_blog_by_id(
    blog_id: int, request: models.Blog, db: Session = Depends(get_db)
):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {blog_id} not found")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return blog
