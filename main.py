
from data_preprocess import load_data, preprocess_data
from train_pipeline.train_model import train_model, evaluate_model
from utils import *


# Load and preprocess data
data = load_data(data_file_path)
X_train_scaled, X_test_scaled, y_train, y_test, scaler = preprocess_data(data, feature_columns, label_columns)

# Save the scaler
save_obj(scaler, scaler_file_path)

# Train the model
model = train_model(X_train_scaled, y_train)

# Evaluate the model
mse, r2 = evaluate_model(model, X_test_scaled, y_test)
print(f'Mean Squared Error for Threshold Voltage: {mse[0]}')
print(f'Mean Squared Error for Drain Current: {mse[1]}')
print(f'R^2 Score: {r2}')

# Save the trained model
save_obj(model, model_file_path)
print('Model and scaler saved to disk.')
