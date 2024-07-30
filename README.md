# House-Price-Prediction-Web-Application
## Overview
This project is a web application built using Python Flask that predicts house prices based on various input features. The application allows users to input house features and obtain a predicted price, which can be downloaded as a PDF report.

## Features
 - *Interactive User Interface*: Users can input house features such as area, number of bedrooms, bathrooms, and more.
 - *Price Prediction*: The application uses a trained Random Forest model to predict house prices based on the input features.
 - *Result Display*: Predicted prices and selected features are displayed on a results page.
PDF Download: Users can download the prediction results as a PDF document.

## Project Structure
    house-price-prediction/
    │
    ├── app.py                # Main application file with Flask routes and logic
    ├── train_model.py        # Script to train the Random Forest model and save it
    ├── models/               # Directory to store the trained model and feature list
    │   ├── house_price_model.pkl
    │   └── feature_list.pkl
    │
    ├── static/
    │   ├── css/
    │   │   └── style.css     # CSS file for styling the HTML pages
    │   └── results/          # Directory to store generated PDF reports
    │
    └── templates/
        ├── index.html        # HTML template for the home page
        └── result.html       # HTML template for displaying prediction results

## Installation
## 1. Clone the Repository:
    git clone https://github.com/yourusername/house-price-prediction.git
    cd house-price-prediction

## 2. Set Up a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## 3. Install Dependencies:
    pip install -r requirements.txt

## 4. Train the Model:
    python train_model.py

## 5. Run the Application:
    python app.py
Open your web browser and go to http://127.0.0.1:5000 to access the web application.

## Usage
## 1. Enter House Features:
 - Navigate to the home page and fill in the house features in the form.
 - Click on "Predict Price" to get the predicted price based on the entered features.
## 2. View Results:
 - After submission, the result page will display the predicted price and the features used.
 - You can download the results as a PDF by clicking the "Download Result as PDF" button.

## Requirements
 - Python 3.x
 - Flask
 - scikit-learn
 - pandas
 - fpdf

## Install the required libraries by running:
    pip install flask scikit-learn pandas fpdf

## Contributing
Feel free to submit issues or pull requests to improve the project. Please make sure to follow the coding standards and write clear commit messages.

## License
This project is licensed under the **MIT License** - see the **LICENSE** file for details.

## Contact
  You can reach me through the following channels:

- Email: [Gmail](mailto:your-email@example.com)
- LinkedIn: [linkedin](https://www.linkedin.com/in/kishorekumar1409/)

*Project Report*:[Project Report.docx](https://github.com/user-attachments/files/16426148/Project.Report.docx)
