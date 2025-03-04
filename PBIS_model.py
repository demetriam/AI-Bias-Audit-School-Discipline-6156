import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import json 

data = pd.read_csv("synthetic_school_discipline.csv")
print("columns in dataset:", data.columns)

X = data.drop(columns=['TOT_PSDISC']) 
y = data['TOT_PSDISC']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

models = {
    "decision tree": DecisionTreeClassifier(max_depth=5, random_state=42),
    "random forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

model_accuracies = {}
for name, model in models.items():
    print(f"\ntraining {name} model")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    model_accuracies[name] = accuracy
    
    print(f"{name} accuracy: {accuracy}")
    print(f"{name} classification Report:\n{classification_report(y_test, y_pred)}")
    joblib.dump(model, f"{name.replace(' ', '_').lower()}_model.pkl")

with open("model_accuracies.json", "w") as f:
    json.dump(model_accuracies, f)

print("\nmodel accuracies saved")
label_encoders = {}
categorical_columns = []  
for col in categorical_columns:
    label_encoders[col] = LabelEncoder()
    data[col] = label_encoders[col].fit_transform(data[col])
if label_encoders:
    joblib.dump(label_encoders, "label_encoders.pkl")

joblib.dump(label_encoders, "label_encoders.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nSaved")