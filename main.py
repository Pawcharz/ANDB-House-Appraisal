from fastapi import Depends, FastAPI
from pydantic import BaseModel
# import pickle


app = FastAPI()

# Load the AI model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)


# Define the input data model
class InputData(BaseModel):
    feature1: str
    feature2: str
    feature3: str


@app.get("/predict")
async def predict(input_data: InputData = Depends()):
    # print(input_data.model_dump())
    # Convert input data to a list for the model
    # features = [[input_data.feature1, input_data.feature2]]  # Add more as needed
    # prediction = model.predict(features)
    # return {"predicted_price": prediction[0]}
    return {"predicted_price": 100000}
