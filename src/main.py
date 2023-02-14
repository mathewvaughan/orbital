from fastapi import FastAPI, HTTPException
from fastapi_pagination import Page, paginate, add_pagination
from pydantic import BaseModel

class Title(BaseModel):
    id : str
    title_number : str
    title_class : str
    content: str


def get_app(data):
    app = FastAPI()


    @app.get("/api/titles", response_model=Page[Title])
    async def title_list():
        return paginate(data)

    @app.get("/api/titles/{id}")
    async def title_details(id):
        result = None
        for title in data:
            if title["id"] == id:
                result = title
        if result is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return result

    add_pagination(app)

    return app

# app = FastAPI()


# class User(BaseModel):
#     name: str
#     surname: str


# users = [
#     User(name='Yurii', surname='Karabas'),
#     # ...
# ]


# @app.get('/users', response_model=Page[User])
# async def get_users():
#     return paginate(users)


# add_pagination(app)