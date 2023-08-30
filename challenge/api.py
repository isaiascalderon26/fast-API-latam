from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
from challenge.model import DelayModel

class PredictionInput(BaseModel):
    OPERA: str
    MES: str
    TIPOVUELO: str
    # Define las demás columnas necesarias

app = FastAPI()

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}

@app.post("/predict/")
def predict(data: PredictionInput):
    try:
        # Crea un DataFrame con los datos de entrada
        input_data = pd.DataFrame([data.dict()])

        # Carga el modelo
        model = DelayModel()  # Crea una instancia de tu modelo aquí

        # Preprocesa los datos y realiza la predicción
        features = model.preprocess(data=input_data)
        predicted_delay = model.predict(features)

        # Devuelve la respuesta como JSON
        response_data = {"predicted_delay": predicted_delay[0]}
        return JSONResponse(content=response_data, status_code=200)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail="Invalid input data")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error during prediction")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
