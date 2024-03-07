from fastapi import FastAPI

from api import prediction 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://www.e-hospital.ca/",
        "https://www.e-hospital.ca/",
        "http://localhost:3000",
        "https://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include API routers
app.include_router(prediction.router, tags=["prediction"])

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app)
