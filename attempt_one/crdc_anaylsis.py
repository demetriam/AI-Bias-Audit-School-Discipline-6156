# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report

# file_path = "/Users/dede/Desktop/AI-Bias-Audit/2017-18-crdc-data-corrected-publication 2/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Suspensions.csv"  # Update with the actual file path
# df = pd.read_csv(file_path)


# print("Dataset Preview:")
# print(df.head())
# relevant_columns = ["School ID", "State", "Race/Ethnicity", "Gender",
#                     "Total Students", "Suspensions", "Expulsions", "Arrests"]

# df = df[relevant_columns].dropna()
# df["Suspension Rate"] = df["Suspensions"] / df["Total Students"]
# df["Expulsion Rate"] = df["Expulsions"] / df["Total Students"]
# df["Arrest Rate"] = df["Arrests"] / df["Total Students"]
# grouped_df = df.groupby("Race/Ethnicity").mean()[["Suspension Rate", "Expulsion Rate", "Arrest Rate"]]


# plt.figure(figsize=(12, 6))
# grouped_df.plot(kind='bar', colormap="viridis", alpha=0.8)
# plt.title("Discipline Rates by Race/Ethnicity")
# plt.ylabel("Rate")
# plt.xticks(rotation=45)
# plt.grid(axis='y', linestyle="--", alpha=0.5)
# plt.legend(title="Discipline Type")
# plt.show()
# df["Race_Code"] = df["Race/Ethnicity"].astype("category").cat.codes
# df["Gender_Code"] = df["Gender"].astype("category").cat.codes

# features = ["Race_Code", "Gender_Code", "Total Students"]
# target = "Suspensions"

# X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X_train, y_train)
# plt.figure(figsize=(14, 8))
# plot_tree(model, feature_names=features, class_names=["No Suspension", "Suspended"], filled=True)
# plt.show()
# y_pred = model.predict(X_test)
# print("Model Performance:")
# print(classification_report(y_test, y_pred))