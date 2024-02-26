from fastapi import FastAPI

from api import prediction 

app = FastAPI()

# Include API routers
app.include_router(prediction.router, tags=["prediction"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)