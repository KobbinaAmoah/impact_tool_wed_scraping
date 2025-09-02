# app.py

from flask import Flask, render_template, request
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the path for our CSV file
CSV_FILE = 'submissions.csv'

# Define the main route for our application
@app.route('/')
def form():
    # This function just renders and displays our HTML form page
    return render_template('form.html')

# Define the route that handles the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the data from the submitted form
    form_data = request.form.to_dict()

    # --- Data Saving Logic ---
    # Create a DataFrame from the new submission
    new_submission_df = pd.DataFrame([form_data])

    # Check if the CSV file already exists
    if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
        # If it exists and is not empty, append without the header
        new_submission_df.to_csv(CSV_FILE, mode='a', header=False, index=False)
    else:
        # If it's a new file, write with the header
        new_submission_df.to_csv(CSV_FILE, mode='w', header=True, index=False)

    # Return a simple thank you message to the user
    return "<h1>Thank you for your submission!</h1><p>Your data has been saved.</p>"

# This line allows us to run the app directly
if __name__ == '__main__':
    # debug=True will auto-reload the server when you save changes
    app.run(debug=True)