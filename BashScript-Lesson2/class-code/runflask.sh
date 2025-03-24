#!/bin/bash

# Configuration variables
REPO="https://github.com/devopsPRO27/movies-api"
FOLDER_NAME="movies-api"
VENV_NAME="venv"
TARGET_MINUTE=48  # The minute when we want to start the application

# Check for Python and install if not present
echo "Checking for Python..."
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 not found. Installing Python3..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install -y python3
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y python3
    else
        echo "Could not determine package manager. Please install Python3 manually."
        exit 1
    fi
else
    echo "Python3 is already installed."
fi

# Check for pip and install if not present
echo "Checking for pip..."
if ! command -v pip3 >/dev/null 2>&1; then
    echo "pip3 not found. Installing pip3..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt install -y python3-pip
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y python3-pip
    else
        echo "Could not determine package manager. Please install pip3 manually."
        exit 1
    fi
else
    echo "pip3 is already installed."
fi

# Check for venv module
echo "Checking for venv module..."
if ! python3 -c "import venv" 2>/dev/null; then
    echo "Python venv module not found. Installing..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt install -y python3-venv
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y python3-venv
    else
        echo "Could not determine package manager. Please install python3-venv manually."
        exit 1
    fi
else
    echo "Python venv module is available."
fi

# Remove existing repository if it exists
if [ -d "$FOLDER_NAME" ]; then
    echo "Removing existing $FOLDER_NAME directory..."
    rm -rf "$FOLDER_NAME"
fi

# Clone the repository
echo "Cloning the repository from $REPO..."
git clone "$REPO"

# Check if clone was successful
if [ ! -d "$FOLDER_NAME" ]; then
    echo "Failed to clone the repository."
    exit 1
fi

# Remove existing venv if it exists
if [ -d "$VENV_NAME" ]; then
    echo "Removing existing virtual environment..."
    rm -rf "$VENV_NAME"
fi

# Create new virtual environment
echo "Creating new virtual environment..."
python3 -m venv "$VENV_NAME"

if [ ! -f "$VENV_NAME/bin/activate" ]; then
    echo "Failed to create virtual environment."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_NAME/bin/activate"

# Find requirements file and install dependencies
REQUIREMENTS_FILE=$(find "$FOLDER_NAME" -maxdepth 1 -type f -name "*.txt" | head -1)

if [ -z "$REQUIREMENTS_FILE" ]; then
    echo "No requirements file found in $FOLDER_NAME directory."
    exit 1
fi

echo "Installing requirements from $REQUIREMENTS_FILE..."
pip install -r "$REQUIREMENTS_FILE"

# Wait until the target minute
echo "Waiting until minute $TARGET_MINUTE to start the application..."
while [ "$(date +%M)" -ne "$TARGET_MINUTE" ]; do
    echo "Current time: $(date +%H:%M:%S) - Waiting for minute $TARGET_MINUTE..."
    sleep 5
done

# Start the Python application
echo "Starting the movies application..."
python3 ./$FOLDER_NAME/movies.py &
PYTHON_PID=$!

echo "Application started with PID: $PYTHON_PID"

# Give the application time to start
echo "Waiting 5 seconds for the application to start..."
sleep 5

# Test the API
echo "Testing the API..."
if ! command -v curl >/dev/null 2>&1; then
    echo "curl not found. Installing curl..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt install -y curl
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y curl
    else
        echo "Could not determine package manager. Please install curl manually."
        exit 1
    fi
fi

# Make the API request
curl http://localhost:80/movie > output.txt

# Check if the API request was successful
if [ $? -eq 0 ]; then
    echo "API test successful. Output saved to output.txt"
else
    echo "API test failed."
fi

echo "To stop the application, run: kill $PYTHON_PID"
echo "Setup completed successfully!"