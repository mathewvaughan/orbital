from fastapi import FastAPI


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
        return result

    return app