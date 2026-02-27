import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("data/training/wine_training.csv")

X = df.drop(columns=["quality_label"])
y = df["quality_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3, 
    random_state=40,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=40
)

model.fit(X_train, y_train)


joblib.dump(model, "models/random_forest_model.pkl")

print("Modelo entrenado y guardado correctamente")