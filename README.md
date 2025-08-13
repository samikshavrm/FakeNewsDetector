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

## Deployment on Render

### Prerequisites

- Render account
- Git repository (GitHub, GitLab, etc.)

### Deployment Steps

1. **Sign up for Render**: Go to [render.com](https://render.com)

2. **Connect your repository**:
   - Click "New +" → "Web Service"
   - Connect your Git repository
   - Select your `FakeNewsDetector` repository

3. **Configure the service**:
   - **Name**: `fake-news-detector`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Deploy**: Click "Create Web Service"

5. **Wait for build** (usually 5-10 minutes)

### Why Render?

- ✅ **No size limits** - Perfect for large ML models
- ✅ **Python 3.9+ support** - Stable and reliable
- ✅ **Easy deployment** - Simple web interface
- ✅ **Automatic HTTPS** - Secure by default
- ✅ **Better for ML** - Designed for data science workloads

For detailed deployment instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md).

## Project Structure

```
FakeNewsDetector/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render configuration
├── runtime.txt           # Python runtime specification
├── models/               # ML models (no size limits!)
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
