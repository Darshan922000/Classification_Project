from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

app = FastAPI()

with open("models/catboost_model.pkl", "rb") as file:
    model = pickle.load(file)

class DataInput(BaseModel):
    features: list[float]
    
@app.get("/")
async def root():
    return {"message": "Welcome to Classification...!!"}

@app.post("/predict/")
async def predict(data: DataInput):
    try:
        #prediction = int(model.predict([data.features]))
        #return {"prediction": prediction}
    
        proba = model.predict_proba([data.features])[0][1]
        result = "Bankrupt" if proba >= 0.5 else "Not Bankrupt"
        return {"prediction": result, "probability": proba}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


