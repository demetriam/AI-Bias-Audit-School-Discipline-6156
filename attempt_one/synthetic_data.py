# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report

# data = {
#     "Disruptive Behavior": [1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
#     "Defiance": [0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
#     "Bullying": [0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
#     "PBIS Strategy": ["Mentorship", "Reflection", "Mediation", "Teacher Training", 
#                       "De-escalation", "Conflict Resolution", "Peer Support", 
#                       "Community Engagement", "Restorative Circle", "Check-in Meeting"]
# }

# df = pd.DataFrame(data)
# df["PBIS Strategy"] = df["PBIS Strategy"].astype("category").cat.codes
# X = df.drop("PBIS Strategy", axis=1)
# y = df["PBIS Strategy"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)


# print(classification_report(y_test, y_pred))

# def predict_strategy(behavior_features):
#     prediction = model.predict([behavior_features])
#     return df["PBIS Strategy"].cat.categories[prediction[0]]

# print("Recommended Method:", predict_strategy([1, 0, 1]))