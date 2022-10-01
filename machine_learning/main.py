import pandas as pd
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import sentry_sdk

sentry_sdk.init(
    dsn="https://3bad9da4b28d45eea807782ec2e661aa@o1421963.ingest.sentry.io/6768230",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)
from ml import ML

app = FastAPI()

origins = ["http://127.0.0.1:5500/",
           "https://tsyka-prog.github.io/PCO/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers=["*"]
)

@app.get('/')
async def get_root():
    return {'message' : "Bienvenue sur l'API de prédiction de prix de maison"}

# @app.get('/metrics')
# async def get_metrics():
#     pass

@app.post("/house_price/")
async def house_price(
    bedrooms: float = Form(...),
    bathrooms: float = Form(...),
    sqft_living: float = Form(...),
    floors: float = Form(...),
    waterfront: float = Form(...),
    view: float = Form(...),
    sqft_basement: float = Form(...),
):

    house = dict ((('bedrooms',bedrooms),
        ('bathrooms',bathrooms),
        ('sqft_living',sqft_living),
        ('floors',floors),
        ('waterfront',waterfront),
        ('view',view),
        ('sqft_basement', sqft_basement)))

    X = pd.DataFrame(house, index=[0])
    prediction = ML()
    pred = prediction.model_predict_test(X)
    X= X.values.tolist()
    return pred

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)