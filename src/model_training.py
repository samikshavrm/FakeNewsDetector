# src/model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

from src.data_preprocessing import clean_text
from src.feature_engineering import create_vectorizer

MODEL_PATH = os.path.join("models", "trained_model.pkl")
DATA_PATH = os.path.join("data", "fake_news.csv")

def train_model():
    print("📂 Loading dataset from:", os.path.abspath(DATA_PATH))
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    print(f"✅ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # Combine title + text if both exist
    if "title" in df.columns and "text" in df.columns:
        df["content"] = df["title"].fillna('') + " " + df["text"].fillna('')
    elif "text" in df.columns:
        df["content"] = df["text"]
    else:
        raise ValueError("Dataset must have 'text' or ('title' and 'text') columns.")

    print("🧹 Cleaning text...")
    df["content"] = df["content"].apply(clean_text)

    print("✂ Splitting train/test...")
    X_train, X_test, y_train, y_test = train_test_split(
        df["content"], df["label"], test_size=0.2, random_state=42
    )

    print("🛠 Creating vectorizer...")
    vectorizer = create_vectorizer(X_train)
    X_train_vec = vectorizer.transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    print("🤖 Training Random Forest...")
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X_train_vec, y_train)

    print(f"💾 Saving model to {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)

    preds = model.predict(X_test_vec)
    print("\n📊 Accuracy:", accuracy_score(y_test, preds))
    print("\nClassification Report:\n", classification_report(y_test, preds))

    print("\n🔍 Sample Predictions:")
    for i in range(5):
        print(f"Text: {X_test.iloc[i][:100]}...")
        print("Predicted:", preds[i], "(1=FAKE, 0=REAL)")
        print("Actual:", y_test.iloc[i])
        print("---")

if __name__ == "__main__":
    train_model()
