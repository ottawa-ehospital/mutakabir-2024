from fastapi import FastAPI

from api import prediction 

app = FastAPI()

# Include API routers
app.include_router(prediction.router, tags=["prediction"])

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
