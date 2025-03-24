#!/bin/bash

REPO="https://github.com/devopsPRO27/movies-api"
FOLDER_NAME="movies-api"
VENV_NAME="venv"
TARGET_MINUTE=48  

install_package() {
    local package_name="$1"
    echo "Installing $package_name..."
    
    if command -v apt >/dev/null 2>&1; then
        sudo apt update
        sudo apt install -y "$package_name"
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y "$package_name"
    else
        echo "Could not determine package manager. Please install $package_name manually."
        return 1
    fi
    return 0
}

check_install_python() {
    echo "Checking for Python..."
    if ! command -v python3 >/dev/null 2>&1; then
        echo "Python3 not found. Installing Python3..."
        install_package "python3"
    else
        echo "Python3 is already installed."
    fi
}

check_install_pip() {
    echo "Checking for pip..."
    if ! command -v pip3 >/dev/null 2>&1; then
        echo "pip3 not found. Installing pip3..."
        install_package "python3-pip"
    else
        echo "pip3 is already installed."
    fi
}

check_install_venv() {
    echo "Checking for venv module..."
    if ! python3 -c "import venv" 2>/dev/null; then
        echo "Python venv module not found. Installing..."
        install_package "python3-venv"
    else
        echo "Python venv module is available."
    fi
}

setup_repository() {
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
        return 1
    fi
    return 0
}

setup_virtual_environment() {
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
        return 1
    fi

    # Activate virtual environment
    echo "Activating virtual environment..."
    source "$VENV_NAME/bin/activate"
    return 0
}

install_dependencies() {
    # Find requirements file and install dependencies
    local requirements_file=$(find "$FOLDER_NAME" -maxdepth 1 -type f -name "*.txt" | head -1)

    if [ -z "$requirements_file" ]; then
        echo "No requirements file found in $FOLDER_NAME directory."
        return 1
    fi

    echo "Installing requirements from $requirements_file..."
    pip install -r "$requirements_file"
    return 0
}

wait_for_target_time() {
    echo "Waiting until minute $TARGET_MINUTE to start the application..."
    while [ "$(date +%M)" -ne "$TARGET_MINUTE" ]; do
        echo "Current time: $(date +%H:%M:%S) - Waiting for minute $TARGET_MINUTE..."
        sleep 5
    done
}

start_application() {
    echo "Starting the movies application..."
    python3 ./$FOLDER_NAME/movies.py &
    local python_pid=$!

    echo "Application started with PID: $python_pid"

    # Give the application time to start
    echo "Waiting 5 seconds for the application to start..."
    sleep 5
    
    return $python_pid
}

test_api() {
    local python_pid=$1
    
    echo "Testing the API..."
    if ! command -v curl >/dev/null 2>&1; then
        echo "curl not found. Installing curl..."
        install_package "curl"
    fi

    # Make the API request
    curl http://localhost:80/movie > output.txt

    # Check if the API request was successful
    if [ $? -eq 0 ]; then
        echo "API test successful. Output saved to output.txt"
    else
        echo "API test failed."
    fi

    echo "To stop the application, run: kill $python_pid"
}

main() {
    check_install_python
    check_install_pip
    check_install_venv
    
    setup_repository || exit 1
    setup_virtual_environment || exit 1
    install_dependencies || exit 1
    
    wait_for_target_time
    
    local app_pid
    app_pid=$(start_application)
    
    test_api "$app_pid"
    
    echo "Setup completed successfully!"
}

main