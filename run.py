import uvicorn
from fastapi import FastAPI
from app.routes import router


def get_application() -> FastAPI:
    application = FastAPI(
        title="scrapper"
    )
    application.include_router(router)
    return application



app = get_application()



def run():
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        reload=True,
        port=8095
    )


if __name__ == '__main__':
    run()
