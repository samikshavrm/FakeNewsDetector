# Fake News Detector

A machine learning-based web application that can detect fake news articles using natural language processing and machine learning techniques.

## Features

- Text-based fake news detection
- Confidence scoring for predictions
- Clean and intuitive web interface
- Machine learning model trained on real and fake news datasets

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd FakeNewsDetector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:8080`

## Deployment on Vercel

### Prerequisites

- Vercel account
- Vercel CLI installed
- Git repository

### Deployment Steps

1. **Install Vercel CLI** (if not already installed):
```bash
npm i -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy to Vercel**:
```bash
vercel
```

4. **Follow the prompts**:
   - Set up and deploy: `Y`
   - Which scope: Select your account
   - Link to existing project: `N`
   - Project name: `fake-news-detector` (or your preferred name)
   - Directory: `.` (current directory)
   - Override settings: `N`

5. **For production deployment**:
```bash
vercel --prod
```

### Important Notes for Vercel Deployment

- The app is configured for serverless deployment
- Model files (`models/trained_model.pkl` and `vectorizers/tfidf_vectorizer.pkl`) must be included in your repository
- Maximum function duration is set to 30 seconds
- Python 3.9 runtime is specified

### Environment Variables (Optional)

You can set environment variables in Vercel dashboard:
- `FLASK_ENV`: Set to `production` for production deployment
- `SECRET_KEY`: Custom secret key for Flask sessions

## Project Structure

```
FakeNewsDetector/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── runtime.txt           # Python runtime specification
├── models/               # Trained ML models
├── vectorizers/          # TF-IDF vectorizers
├── src/                  # Source code modules
├── templates/            # HTML templates
└── static/               # CSS and static files
```

## Model Information

The application uses:
- **Algorithm**: Machine Learning classifier (trained on news dataset)
- **Features**: TF-IDF vectorization of text
- **Input**: News article text (minimum 10 characters)
- **Output**: Prediction (Real/Fake) with confidence score

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
