from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import setting


app = FastAPI()

origin = setting.ORIGIN


app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Api is working"}