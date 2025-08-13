from flask import Flask, render_template, request, flash, redirect, url_for
import joblib
from src.data_preprocessing import clean_text
from src.feature_engineering import load_vectorizer
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Global variables for model and vectorizer
model = None
vectorizer = None

def load_models():
    """Load the trained model and vectorizer with error handling"""
    global model, vectorizer
    try:
        MODEL_PATH = os.path.join("models", "trained_model.pkl")
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        
        model = joblib.load(MODEL_PATH)
        vectorizer = load_vectorizer()
        logger.info("Models loaded successfully")
        return True
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        return False

# Load models on startup
if not load_models():
    logger.error("Failed to load models. Please ensure models are trained.")

@app.route("/")
def index():
    if model is None or vectorizer is None:
        flash("Error: Models not loaded. Please contact administrator.", "error")
        return render_template("index.html")
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check if models are loaded
        if model is None or vectorizer is None:
            flash("Error: Models not available. Please try again later.", "error")
            return redirect(url_for('index'))
        
        # Get and validate input
        news_text = request.form.get("news_text", "").strip()
        
        if not news_text:
            flash("Please enter some text to analyze.", "error")
            return redirect(url_for('index'))
        
        if len(news_text) < 10:
            flash("Please enter at least 10 characters for accurate analysis.", "error")
            return redirect(url_for('index'))
        
        if len(news_text) > 5000:
            flash("Text is too long. Please enter less than 5000 characters.", "error")
            return redirect(url_for('index'))
        
        # Process the text
        cleaned_text = clean_text(news_text)
        
        if len(cleaned_text) < 5:
            flash("Unable to process the text. Please try different content.", "error")
            return redirect(url_for('index'))
        
        # Make prediction
        text_vec = vectorizer.transform([cleaned_text])
        prediction = model.predict(text_vec)[0]
        confidence = model.predict_proba(text_vec)[0]
        confidence_score = max(confidence) * 100
        
        result = "FAKE News" if prediction == 1 else "REAL News"
        confidence_label = "High" if confidence_score > 80 else "Medium" if confidence_score > 60 else "Low"
        
        return render_template("result.html", 
                             news_text=news_text, 
                             prediction=result, 
                             confidence_score=f"{confidence_score:.1f}%",
                             confidence_label=confidence_label)
    
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        flash("An error occurred while analyzing the text. Please try again.", "error")
        return redirect(url_for('index'))

# For Render deployment - restore the main block
if __name__ == "__main__":
    app.run(debug=True, port=8080)
