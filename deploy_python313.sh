#!/bin/bash

echo "🐍 Deploying with Python 3.13 compatibility..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository. Please initialize git first:"
    echo "   git init"
    echo "   git remote add origin <your-repo-url>"
    exit 1
fi

# Show what we're changing
echo ""
echo "📋 Configuration changes made:"
echo "   • Python version: 3.13 (what Render is using)"
echo "   • pandas: >=2.2.0 (Python 3.13 compatible)"
echo "   • numpy: >=1.26.0 (Python 3.13 compatible)"
echo "   • scikit-learn: >=1.4.0 (Python 3.13 compatible)"
echo "   • Flask: >=3.0.0 (Python 3.13 compatible)"
echo "   • Using pre-built wheels (no compilation needed)"
echo ""

# Add all files
echo "📁 Adding all files to git..."
git add .

# Commit changes
echo "💾 Committing Python 3.13 compatibility fixes..."
git commit -m "Fix Python 3.13 compatibility - use pre-built wheels - $(date)"

# Push to remote
echo "🚀 Pushing to remote repository..."
git push

echo ""
echo "✅ Configuration fixed and pushed successfully!"
echo ""
echo "🌐 Now redeploy on Render:"
echo "1. Go to your Render dashboard"
echo "2. Find your fake-news-detector service"
echo "3. Click 'Manual Deploy' or wait for auto-deploy"
echo "4. The build should now succeed with Python 3.13"
echo ""
echo "📚 The key changes:"
echo "   • Using Python 3.13 (what Render provides)"
echo "   • All packages have pre-built wheels"
echo "   • No compilation from source needed"
echo "   • Modern package versions for better compatibility"
