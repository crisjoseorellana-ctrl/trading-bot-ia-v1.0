from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.signal_service import get_signal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/signal/{symbol}")
def signal(symbol: str):
    return get_signal(symbol)