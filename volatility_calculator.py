import pandas as pd
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


def calculate_volatility(data):
    # Task 1
    # Calculate Daily Returns
    data['Daily Returns'] = data['Close'].pct_change()

    # Calculate Daily Volatility
    daily_volatility = data['Daily Returns'].std()

    # Calculate Annualized Volatility
    annualized_volatility = daily_volatility * np.sqrt(len(data))

    return daily_volatility, annualized_volatility


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate_volatility', methods=['POST'])
def calculate_volatility_endpoint():
    """
    Endpoint to calculate Daily and Annualized Volatility.

    Parameters:
    - file: CSV file containing historical stock data with 'Close' column.

    Returns:
    - JSON response with Daily and Annualized Volatility.
    """
    try:
        # Check if the file is uploaded or provided as parameter
        if 'file' in request.files:
            file = request.files['file']
            data = pd.read_csv(file)
        elif 'file_path' in request.form:
            file_path = request.form['file_path']
            data = pd.read_csv(file_path)
        else:
            return jsonify({'error': 'No file provided'}), 400
        # Validate the required 'Close' column in the dataset
        if 'Close' not in data.columns:
            return jsonify({'error': 'Column "Close" not found in the dataset'}), 400

        # Calculate volatility
        daily_volatility, annualized_volatility = calculate_volatility(data)

        # Render HTML template with results
        return render_template('result.html',
                               daily_volatility=daily_volatility,
                               annualized_volatility=annualized_volatility)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True,port=8000)
