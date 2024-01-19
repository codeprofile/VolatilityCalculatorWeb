# VolatilityCalculatorWeb
A simple web application built with Flask that calculates the daily and annualized volatility of a financial dataset. Users can upload a CSV file containing historical stock data or provide a file path to calculate and display volatility metrics in a user-friendly interface.

Features:

File Upload: Easily upload a CSV file with historical stock data.
Calculate Volatility: Compute daily and annualized volatility based on the uploaded dataset.
Bootstrap UI: Enhanced user interface with Bootstrap for a clean and responsive design.
Flask Endpoint: RESTful API endpoint for volatility calculation accessible via HTTP POST requests.
Usage:

Upload a CSV file or provide a file path.
Click "Calculate Volatility" to see the daily and annualized volatility.
Results are displayed in a Bootstrap-styled table for easy comprehension.


Getting Started:

# Clone the repository
git clone https://github.com/codeprofile/VolatilityCalculatorWeb.git

# Navigate to the project directory
cd VolatilityCalculatorWeb

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python volatility_calculator.py

