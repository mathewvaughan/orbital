from fastapi import FastAPI, HTTPException, Depends
from fastapi_pagination import Page, paginate, add_pagination, Params
from pydantic import BaseModel

class Title(BaseModel):
    id : str
    title_number : str
    title_class : str
    content: str


def get_app(data):
    app = FastAPI()


    @app.get("/api/titles", response_model=Page[Title])
    async def title_list(
        params: Params = Depends(),
        _sort: str = None,
        _order: str = None,
        title_class: str = None,
    ):
        result = data

        if _sort:
            result.sort(key=lambda x: x[_sort], reverse=_order == "desc")

        if title_class:
            result = [x for x in data if x["title_class"] == title_class]
        
        return paginate(result, params)

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
