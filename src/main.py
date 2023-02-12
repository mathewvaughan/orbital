from fastapi import FastAPI


def get_app(data):
    app = FastAPI()


    @app.get("/api/titles")
    async def root():
        return data

    return app