#!/bin/bash

echo "=== Loading echoart util from GitHub ==="

# Check Git
if ! command -v git &> /dev/null; then
    echo "Git not found. Please install Git and try again."
    read -n 1 -s -r -p "Press any key to exit..."
    echo
    exit 1
fi

# Clone repo
if ! git clone https://github.com/WarerCode/echoart.git; then
    echo "Failed to clone repository."
    read -n 1 -s -r -p "Press any key to exit..."
    echo
    exit 1
fi

# Enter repo directory
cd echoart || {
    echo "Failed to enter echoart directory."
    read -n 1 -s -r -p "Press any key to exit..."
    echo
    exit 1
}

# Check Python
if ! command -v python &> /dev/null; then
    echo "Python not found. Please install Python and try again."
    read -n 1 -s -r -p "Press any key to exit..."
    echo
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
if ! sudo pip install -r requirements.txt --break-system-packages; then
    echo "Failed to install requirements."
    read -n 1 -s -r -p "Press any key to exit..."
    echo
    exit 1
fi

# Make echoart.sh executable
echo "Setting execution permissions..."
if ! sudo chmod +x echoart.sh; then
    echo "Failed to set execution permissions for echoart.sh"
    read -n 1 -s -r -p "Press any key to exit..."
    echo
    exit 1
fi

# Run the script
echo "Running echoart..."
./echoart.sh --input assets/image.jpg

# Show help
./echoart.sh --help

read -n 1 -s -r -p "Press any key to exit..."
echo
