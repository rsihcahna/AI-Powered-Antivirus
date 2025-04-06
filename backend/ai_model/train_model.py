# backend/ai_model/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def load_dataset(path):
    return pd.read_csv(path)

def preprocess(df):
    df.fillna(0, inplace=True)
    X = df.drop("label", axis=1)
    y = df["label"]
    return X, y

def train_and_save_model(data_path, model_path):
    print("Loading dataset...")
    df = load_dataset(data_path)
    print("Preprocessing...")
    X, y = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print("Training Random Forest model...")
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    print(f"Saving trained model to {model_path}")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)

    acc = clf.score(X_test, y_test)
    print(f"Model trained successfully! Accuracy: {acc * 100:.2f}%")

if __name__ == "__main__":
    data_path = "backend/ai_model/malware_dataset.csv"  # Sample dataset path
    model_path = "backend/ai_model/malware_model.pkl"
    train_and_save_model(data_path, model_path)
