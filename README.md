# Multi-Digit Recognizer
This project implements a multi-digit recognition system using machine learning techniques.

# Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.11
Git
Installation

# Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Praneethgeethanjana/digit-recognizer.git

# Navigate to the project directory:
bash
Copy code
cd digit-recognizer

# Create a virtual environment:
bash
Copy code
python -m venv env

# Activate the virtual environment:

# On Windows:

bash
Copy code
env\Scripts\activate

# On macOS/Linux:

bash
Copy code
source env/bin/activate


# Install the dependencies:

bash
Copy code
pip install -r requirements.txt


# Running the Project
To run the project, execute the following command:
bash
Copy code
uvicorn main:app --reload

# After running the command, copy the provided URL (e.g., http://127.0.0.1:8000) and paste it into your web browser.

# Usage
Capture Image from Camera: Click the "Capture from Camera" button to capture an image using your device's camera.

Upload Image: Click the "Upload Image" button to select an image file from your local system.

Prediction: Once an image is captured or uploaded, the system will predict the digits present in the image and display the results.

# Authors
Praneeth Geethanjana - GitHub