from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field
import tensorflow as tf
import numpy as np



# Creating and loading ML model

model = tf.keras.Sequential(
  [
    tf.keras.layers.Input([3]),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1),
  ]
)

# Load the AI model
MODEL_PATH = "model.h5"
try:
    model.load_weights(MODEL_PATH, skip_mismatch=False)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

class InputData(BaseModel):
    bedrooms: int = Field(..., gt=0, lt=400, description="Number of bedrooms must be greater than 0 and less than 400")
    bathrooms: int = Field(..., gt=0, lt=400, description="Number of bathrooms must be greater than 0 and less than 400")
    house_size: int = Field(..., gt=0, description="House size must be greater than 0")


app = FastAPI()

@app.get("/predict")
async def predict(input_data: InputData = Depends()):
    features = np.array([[input_data.bedrooms, input_data.bathrooms, input_data.house_size]])

    print(f"Features for prediction: {features}")
    # Make prediction
    prediction = model.predict(features)  # Predict using the model

    # Extract the predicted value (assuming a regression task)
    predicted_price = prediction[0][0]

    return {"predicted_price": round(float(predicted_price))}

