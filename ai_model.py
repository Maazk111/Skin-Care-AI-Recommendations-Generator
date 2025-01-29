import sys
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load user input from Node.js
if len(sys.argv) > 1:
    user_input = json.loads(sys.argv[1])

    # Load the dataset
    dataset_path = "./Refined_Skincare_Dataset.csv"
    data = pd.read_csv(dataset_path)

    # Preprocess the dataset
    label_encoders = {}
    for column in ['Gender', 'Age Range', 'Skin Type', 'Skin Concern', 'Skin Sensitivity', 'Allergic Issue']:
        label_encoders[column] = LabelEncoder()
        data[column] = label_encoders[column].fit_transform(data[column])

    # Train the model
    X = data[['Gender', 'Age Range', 'Skin Type', 'Skin Concern', 'Skin Sensitivity', 'Allergic Issue']]
    y = data['Recommended Products']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Preprocess user input
    for key, value in user_input.items():
        user_input[key] = label_encoders[key].transform([value])[0]

    user_df = pd.DataFrame([user_input])
    prediction = model.predict(user_df)

    # Return the prediction as JSON
    print(json.dumps({"recommended_product": prediction[0]}))
else:
    print(json.dumps({"error": "No input provided"}))