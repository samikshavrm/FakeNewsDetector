#!/bin/bash

echo "🐍 Setting up Python 3.11 environment..."

# Check available Python versions
echo "Available Python versions:"
ls /usr/bin/python* 2>/dev/null || echo "No Python versions found in /usr/bin"
which python3.11 || echo "python3.11 not found in PATH"

# Try to use Python 3.11 explicitly
if command -v python3.11 &> /dev/null; then
    echo "✅ Using Python 3.11"
    PYTHON_CMD="python3.11"
elif command -v python3.11.7 &> /dev/null; then
    echo "✅ Using Python 3.11.7"
    PYTHON_CMD="python3.11.7"
else
    echo "⚠️  Python 3.11 not found, trying to find compatible version..."
    # Look for any Python 3.11.x
    for py in python3.11*; do
        if command -v $py &> /dev/null; then
            echo "✅ Found $py"
            PYTHON_CMD="$py"
            break
        fi
    done
    
    if [ -z "$PYTHON_CMD" ]; then
        echo "❌ No Python 3.11 found, falling back to python3"
        PYTHON_CMD="python3"
    fi
fi

echo "🔧 Using: $PYTHON_CMD"
echo "🔧 Version: $($PYTHON_CMD --version)"

# Upgrade pip
echo "📦 Upgrading pip..."
$PYTHON_CMD -m pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
$PYTHON_CMD -m pip install -r requirements.txt

echo "✅ Build completed successfully!"
