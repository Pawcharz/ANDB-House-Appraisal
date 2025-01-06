from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field
# import pickle


app = FastAPI()

# Load the AI model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)


class InputData(BaseModel):
    bedrooms: int = Field(..., gt=0, lt=400, description="Number of bedrooms must be greater than 0 and less than 400")
    bathrooms: int = Field(..., gt=0, lt=400, description="Number of bathrooms must be greater than 0 and less than 400")
    house_size: int = Field(..., gt=0, description="House size must be greater than 0")



@app.get("/predict")
async def predict(input_data: InputData = Depends()):
    # print(input_data.model_dump())
    # Convert input data to a list for the model
    # features = [[input_data.feature1, input_data.feature2]]  # Add more as needed
    # prediction = model.predict(features)
    # return {"predicted_price": prediction[0]}
    return {"predicted_price": 100000}
