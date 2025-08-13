#!/usr/bin/env python3
"""
Test script for the improved Fake News Detector model
"""

import joblib
from src.data_preprocessing import clean_text
from src.feature_engineering import load_vectorizer

def test_model():
    """Test the model with various news examples"""
    
    print("🧪 Testing Improved Fake News Detector Model")
    print("=" * 50)
    
    # Load the model and vectorizer
    model = joblib.load("models/trained_model.pkl")
    vectorizer = load_vectorizer()
    
    # Test cases
    test_cases = [
        # Real news examples
        {
            "text": "NASA successfully launches new satellite to study climate change",
            "expected": "REAL"
        },
        {
            "text": "Scientists discover new species of deep-sea creatures in the Pacific Ocean",
            "expected": "REAL"
        },
        {
            "text": "World Health Organization releases updated guidelines for COVID-19 prevention",
            "expected": "REAL"
        },
        {
            "text": "Study shows benefits of regular exercise on mental health",
            "expected": "REAL"
        },
        {
            "text": "Renewable energy sources now provide 30% of global electricity",
            "expected": "REAL"
        },
        
        # Fake news examples
        {
            "text": "Aliens control the government - shocking revelation",
            "expected": "FAKE"
        },
        {
            "text": "Miracle cure for cancer discovered - doctors trying to hide it",
            "expected": "FAKE"
        },
        {
            "text": "One simple trick to lose 50 pounds in a week - doctors hate this",
            "expected": "FAKE"
        },
        {
            "text": "World ending tomorrow according to ancient prophecy - NASA confirms",
            "expected": "FAKE"
        },
        {
            "text": "Secret society controls world economy - shocking revelations",
            "expected": "FAKE"
        }
    ]
    
    correct_predictions = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases, 1):
        text = test_case["text"]
        expected = test_case["expected"]
        
        # Clean and predict
        cleaned_text = clean_text(text)
        text_vec = vectorizer.transform([cleaned_text])
        prediction = model.predict(text_vec)[0]
        confidence = model.predict_proba(text_vec)[0]
        confidence_score = max(confidence) * 100
        
        result = "FAKE" if prediction == 1 else "REAL"
        is_correct = result == expected
        
        if is_correct:
            correct_predictions += 1
        
        # Display results
        status = "✅" if is_correct else "❌"
        print(f"\n{status} Test {i}: {result} (Expected: {expected})")
        print(f"   Text: {text}")
        print(f"   Confidence: {confidence_score:.1f}%")
        print(f"   {'CORRECT' if is_correct else 'INCORRECT'}")
    
    # Summary
    accuracy = (correct_predictions / total_tests) * 100
    print(f"\n" + "=" * 50)
    print(f"📊 Test Results Summary:")
    print(f"   Correct Predictions: {correct_predictions}/{total_tests}")
    print(f"   Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 90:
        print("🎉 Model is working excellently!")
    elif accuracy >= 80:
        print("👍 Model is working well!")
    elif accuracy >= 70:
        print("⚠️ Model needs improvement")
    else:
        print("❌ Model needs significant improvement")
    
    print(f"\n🚀 The Flask application is ready at: http://127.0.0.1:8080")

if __name__ == "__main__":
    test_model()
