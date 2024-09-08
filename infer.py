from utils import *
import pandas as pd


def infer(new_data):
    # Load the model and scaler
    model = load_obj(model_file_path)
    scaler = load_obj(scaler_file_path)

    # Preprocess new data
    new_data_scaled = scaler.transform(new_data)

    # Make predictions
    predictions = model.predict(new_data_scaled)
    return predictions

# Function to get user input
def get_user_input():
    input_str = input(f"Enter values for {', '.join(feature_columns)} (comma-separated): ")
    user_data = [float(value) for value in input_str.split(',')]
    return pd.DataFrame([user_data], columns=feature_columns)

# Get user input for inference
new_data = get_user_input()
predictions = infer(new_data)
print(f"Predictions: {predictions}")