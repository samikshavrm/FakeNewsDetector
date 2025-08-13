#!/bin/bash

echo "🚀 Preparing Fake News Detector for Render deployment..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository. Please initialize git first:"
    echo "   git init"
    echo "   git remote add origin <your-repo-url>"
    exit 1
fi

# Check git status
echo "📊 Checking git status..."
git status

# Add all files
echo "📁 Adding all files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Configure for Render deployment - $(date)"

# Push to remote
echo "🚀 Pushing to remote repository..."
git push

echo ""
echo "✅ Code pushed successfully!"
echo ""
echo "🌐 Now deploy on Render:"
echo "1. Go to https://render.com"
echo "2. Click 'New +' → 'Web Service'"
echo "3. Connect your repository"
echo "4. Configure:"
echo "   - Name: fake-news-detector"
echo "   - Environment: Python 3"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn app:app"
echo "5. Click 'Create Web Service'"
echo ""
echo "📚 For detailed instructions, see RENDER_DEPLOYMENT.md"
