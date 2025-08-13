#!/usr/bin/env python3
"""
Test script to verify Flask app compatibility with Vercel deployment
"""

import os
import sys
import importlib.util

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing module imports...")
    
    try:
        # Test Flask
        import flask
        print("✅ Flask imported successfully")
        
        # Test joblib
        import joblib
        print("✅ Joblib imported successfully")
        
        # Test scikit-learn
        import sklearn
        print("✅ Scikit-learn imported successfully")
        
        # Test pandas
        import pandas
        print("✅ Pandas imported successfully")
        
        # Test numpy
        import numpy
        print("✅ Numpy imported successfully")
        
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    
    return True

def test_app_creation():
    """Test if Flask app can be created"""
    print("\n🔍 Testing Flask app creation...")
    
    try:
        # Import the app module
        spec = importlib.util.spec_from_file_location("app", "app.py")
        app_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_module)
        
        # Check if app exists
        if hasattr(app_module, 'app'):
            print("✅ Flask app created successfully")
            return True
        else:
            print("❌ Flask app not found in app.py")
            return False
            
    except Exception as e:
        print(f"❌ App creation failed: {e}")
        return False

def test_file_structure():
    """Test if required files exist"""
    print("\n🔍 Testing file structure...")
    
    required_files = [
        "app.py",
        "requirements.txt",
        "vercel.json",
        "runtime.txt",
        "models/trained_model.pkl",
        "vectorizers/tfidf_vectorizer.pkl",
        "src/__init__.py",
        "src/data_preprocessing.py",
        "src/feature_engineering.py",
        "templates/index.html",
        "templates/result.html",
        "static/style.css"
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} required files")
        return False
    else:
        print("\n✅ All required files present")
        return True

def test_model_loading():
    """Test if models can be loaded"""
    print("\n🔍 Testing model loading...")
    
    try:
        # Import the app module
        spec = importlib.util.spec_from_file_location("app", "app.py")
        app_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_module)
        
        # Try to load models
        if hasattr(app_module, 'load_models'):
            success = app_module.load_models()
            if success:
                print("✅ Models loaded successfully")
                return True
            else:
                print("❌ Model loading failed")
                return False
        else:
            print("❌ load_models function not found")
            return False
            
    except Exception as e:
        print(f"❌ Model loading test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Fake News Detector - Vercel Deployment Test")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("File Structure", test_file_structure),
        ("App Creation", test_app_creation),
        ("Model Loading", test_model_loading)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your app is ready for Vercel deployment.")
        return True
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix issues before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
