from flask import Flask, render_template, request
import joblib
from src.data_preprocessing import clean_text
from src.feature_engineering import load_vectorizer
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("models", "trained_model.pkl")
model = joblib.load(MODEL_PATH)
vectorizer = load_vectorizer()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    news_text = request.form["news_text"]
    cleaned_text = clean_text(news_text)
    text_vec = vectorizer.transform([cleaned_text])
    prediction = model.predict(text_vec)[0]
    result = "FAKE News" if prediction == 1 else "REAL News"
    return render_template("result.html", news_text=news_text, prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
