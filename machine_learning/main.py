import pandas as pd
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from ml import ML

app = FastAPI()

origins = ["house-price-pred-simplon.herokuapp.com","https://house-price-pred-simplon.herokuapp.com/","https://house-price-pred-simplon.herokuapp.com/house_price/","http://127.0.0.1:5500/"]

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

@app.post("/house_price/")
async def house_price(
    bedrooms: float = Form(...),
    bathrooms: float = Form(...),
    sqft_living: float = Form(...),
    sqft_lot: float = Form(...),
    floors: float = Form(...),
    waterfront: float = Form(...),
    view: float = Form(...),
    sqft_above: float = Form(...),
    sqft_basement: float = Form(...),
):

    house = dict ((('bedrooms',bedrooms),
        ('bathrooms',bathrooms),
        ('sqft_living',sqft_living),
        ('sqft_lot',sqft_lot),
        ('floors',floors),
        ('waterfront',waterfront),
        ('view',view),
        ('sqft_above',sqft_above),
        ('sqft_basement', sqft_basement)))

    print("1")
    X = pd.DataFrame(house, index=[0])

    prediction = ML()
    pred = prediction.model_predict_test(X)
    print("2")
    X= X.values.tolist()

    print('3')

    # resultat = prediction_house(X)
    print("4")
    return pred

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)