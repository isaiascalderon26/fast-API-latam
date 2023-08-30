import sys
sys.path.append(".") 

import unittest
from fastapi.testclient import TestClient
from challenge.api import app  # Importa app desde challenge.api
from challenge.model import DelayModel  # Importa DelayModel desde challenge.model

class TestBatchPipeline(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
    def test_should_get_predict(self):
        data = {
            "flights": [
                {
                    "OPERA": "Aerolineas Argentinas", 
                    "TIPOVUELO": "N", 
                    "MES": 3
                }
            ]
        }
        # Crea una instancia de tu modelo aquí
        model = DelayModel()
        
        # Mock la función predict para devolver un valor específico
        model.predict = lambda _: [0]
        
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"predicted_delay": 0})
    

    def test_should_failed_unkown_column_1(self):
        data = {       
            "flights": [
                {
                    "OPERA": "Aerolineas Argentinas", 
                    "TIPOVUELO": "N",
                    "MES": 13
                }
            ]
        }
        # Crea una instancia de tu modelo aquí
        model = DelayModel()
        
        response = self.client.post("/predict", json=data)
        print("Response Status Code:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, 400)

    def test_should_failed_unkown_column_2(self):
        data = {        
            "flights": [
                {
                    "OPERA": "Aerolineas Argentinas", 
                    "TIPOVUELO": "O", 
                    "MES": 13
                }
            ]
        }
        # Crea una instancia de tu modelo aquí
        model = DelayModel()
        
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 400)
    
    def test_should_failed_unkown_column_3(self):
        data = {        
            "flights": [
                {
                    "OPERA": "Argentinas", 
                    "TIPOVUELO": "O", 
                    "MES": 13
                }
            ]
        }
        # Crea una instancia de tu modelo aquí
        model = DelayModel()
        
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
