import joblib

# Define file paths
data_file_path = './dataset/mosfet_data.csv'
scaler_file_path = './blob/scaler.pkl'
model_file_path = './blob/mosfet_model.pkl'


# Define columns
feature_columns = [
    'gate_length', 'gate_width', 'oxide_thickness', 'source_doping_concentration',
    'drain_doping_concentration', 'channel_doping_concentration', 'supply_voltage',
    'temperature', 'gate_capacitance', 'subthreshold_slope', 'mobility',
    'temperature_variation', 'noise_factors'
]

label_columns = ['threshold_voltage', 'drain_current']


def save_obj(obj, file_path):
    joblib.dump(obj, file_path)

def load_obj(file_path):
    return joblib.load(file_path)
