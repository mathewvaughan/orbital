from fastapi import FastAPI, HTTPException


def get_app(data):
    app = FastAPI()


    @app.get("/api/titles")
    async def title_list():
        return data

    @app.get("/api/titles/{id}")
    async def title_details(id):
        result = None
        for title in data:
            if title["id"] == id:
                result = title
        if result is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return result

    return app