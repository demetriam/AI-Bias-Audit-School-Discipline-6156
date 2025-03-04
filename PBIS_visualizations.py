import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

with open("model_accuracies.json", "r") as f:
    model_accuracies = json.load(f)

models = list(model_accuracies.keys())
accuracies = list(model_accuracies.values())

plt.figure(figsize=(8, 5))
plt.bar(models, accuracies, color=['blue', 'green'])
plt.ylim(0, 1) 
plt.ylabel("Accuracy Score")
plt.xlabel("AI Models")
plt.title("Comparison of AI Model Accuracy in Predicting Discipline Outcomes")

for i, v in enumerate(accuracies):
    plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=12)

plt.savefig("model_accuracy_comparison.png")
plt.show()

data = pd.read_csv("synthetic_school_discipline.csv")
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap for Student Discipline Data")
plt.savefig("feature_correlation_heatmap.png")
plt.show()