# backend/ai_model/train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from pymongo import MongoClient
from urllib.parse import quote_plus
import os


def load_dataset_from_mongodb(limit=1000):
    username = quote_plus("rsihcahna")
    password = quote_plus("Shaan_@1808")
    uri = f"mongodb+srv://{username}:{password}@cluster0.lmnljuf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri)
    db = client["antivirus"]
    collection = db["signatures"]
    documents = list(collection.find().limit(limit))
    df = pd.DataFrame(documents)
    return df


def preprocess(df):
    df.drop(columns=["_id"], errors="ignore", inplace=True)

    # Clean column names
    df.columns = df.columns.str.strip()

    print("Columns in dataset:", df.columns.tolist())

    if "vtpercent" in df.columns:
        df["vtpercent"] = df["vtpercent"].astype(str).str.replace('%', '', regex=False)

    # Try to convert all columns to numeric where possible
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.fillna(0, inplace=True)

    # Rename 'class' to 'label' if needed
    if "class" in df.columns:
        df.rename(columns={"class": "label"}, inplace=True)

    if "label" not in df.columns:
        raise ValueError("Missing 'label' column for supervised training.")

    X = df.drop(columns=["label"])
    y = df["label"]
    return X, y


def train_and_save_model(model_path):
    print("Loading dataset from MongoDB...")
    df = load_dataset_from_mongodb()

    print("Preprocessing...")
    X, y = preprocess(df)

    if X.shape[1] == 0:
        raise ValueError("No numeric features found after preprocessing!")

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("X_train shape:", X_train.shape)
    print("y_train shape:", y_train.shape)

    print("Training Random Forest model...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    accuracy = clf.score(X_test, y_test)
    print(f"Model accuracy on test set: {accuracy:.2f}")

    print("Saving model...")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)
    print(f"Model saved successfully at: {model_path}")


if __name__ == "__main__":
    model_output_path = "backend/ai_model/backend/malware_model.pkl"
    train_and_save_model(model_output_path)
