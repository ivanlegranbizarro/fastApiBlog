from fastapi import FastAPI

import models
from database import engine
from routers import user, blog


app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(blog.router, prefix="/blogs", tags=["blogs"])

models.Base.metadata.create_all(bind=engine)
