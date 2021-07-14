from fastapi import FastAPI

import stocker

app = FastAPI()


@app.get("/")
def index():
    msg = "Request /predict/{stock_code} and get the following day price prediction \n Please be patience - it will take a moment \n stock_code must be inserted as per Yahoo finance naming, e.g. XAUUSD is GC=F"
    return msg


@app.get("/predict/{stock_code}")
def predict(stock_code: str):
    return stocker.predict.tomorrow(stock_code)
