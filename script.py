import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the data
data = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

# Define features (X) and target variable (y)
X = data.drop(["NObeyesdad"], axis=1) # Dropping original label for training
y = data["NObeyesdad"]

# Encode categorical variables
X_encoded = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.33, random_state=42)

# Train the RandomForestClassifier model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Function to get input and make prediction
def predict_obesity():
    age = float(input("Age: "))
    gender = input("Gender (Male/Female): ")
    height = float(input("Height: "))
    weight = float(input("Weight: "))
    calc = input("CALC (SOMETIMES/FREQUENTLY/NO): ")
    favc = input("FAVC (yes/no): ")
    fcvc = int(input("FCVC: "))
    ncp = int(input("NCP: "))
    scc = input("SCC (yes/no): ")
    smoke = input("SMOKE (yes/no): ")
    ch2o = int(input("CH2O: "))
    family_history = input("Family History with Overweight (yes/no): ")
    faf = int(input("FAF: "))
    tue = int(input("TUE: "))
    caec = input("CAEC (no/Sometimes/Frequently/Always): ")
    mtrans = input("MTRANS (Automobile/Motorbike/Bike/Public_Transportation/Walking): ")

    # Create dataframe from input
    input_df = pd.DataFrame({
        "Age": [age],
        "Gender_Male": [1 if gender == "Male" else 0],
        "Height": [height],
        "Weight": [weight],
        "CALC_no": [1 if calc == "NO" else 0],
        "CALC_Sometimes": [1 if calc == "SOMETIMES" else 0],
        "CALC_Frequently": [1 if calc == "FREQUENTLY" else 0],
        "FAVC_yes": [1 if favc == "yes" else 0],
        "FCVC": [fcvc],
        "NCP": [ncp],
        "SCC_yes": [1 if scc == "yes" else 0],
        "SMOKE_yes": [1 if smoke == "yes" else 0],
        "CH2O": [ch2o],
        "family_history_with_overweight_yes": [1 if family_history == "yes" else 0],
        "FAF": [faf],
        "TUE": [tue],
        "CAEC_no": [1 if caec == "no" else 0],
        "CAEC_Sometimes": [1 if caec == "Sometimes" else 0],
        "CAEC_Frequently": [1 if caec == "Frequently" else 0],
        "CAEC_Always": [1 if caec == "Always" else 0],
        "MTRANS_Automobile": [1 if mtrans == "Automobile" else 0],
        "MTRANS_Motorbike": [1 if mtrans == "Motorbike" else 0],
        "MTRANS_Bike": [1 if mtrans == "Bike" else 0],
        "MTRANS_Public_Transportation": [1 if mtrans == "Public_Transportation" else 0],
        "MTRANS_Walking": [1 if mtrans == "Walking" else 0]
    })

    # Align input DataFrame columns with training data columns
    input_df = input_df.reindex(columns=X_train.columns, fill_value=0)

    # Make prediction
    prediction = model.predict(input_df)
    return prediction

# Make predictions
predicted_obesity = predict_obesity()
print("Predicted Obesity Level:", predicted_obesity)
