from fastapi import FastAPI


def get_app():
    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app