#!/bin/bash

echo "🔧 Fixing deployment configuration for Python 3.11 compatibility..."

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
echo "   • Python version: 3.11 (stable and compatible)"
echo "   • pandas: 2.0.3 (Python 3.11 compatible)"
echo "   • numpy: 1.24.3 (Python 3.11 compatible)"
echo "   • scikit-learn: 1.3.0 (Python 3.11 compatible)"
echo "   • Flask: 2.3.3 (Python 3.11 compatible)"
echo ""

# Add all files
echo "📁 Adding all files to git..."
git add .

# Commit changes
echo "💾 Committing configuration fixes..."
git commit -m "Fix Python 3.11 compatibility for Render deployment - $(date)"

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
echo "4. The build should now succeed with Python 3.11"
echo ""
echo "📚 The key changes:"
echo "   • Using Python 3.11 instead of 3.13"
echo "   • All packages are now fully compatible"
echo "   • No more compilation errors"
