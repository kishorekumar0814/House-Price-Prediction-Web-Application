from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import joblib
import pandas as pd
import os

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'

# Load the trained model and feature list
model = joblib.load('models/house_price_model.pkl')
feature_list = joblib.load('models/feature_list.pkl')

def predict_price(area, bedrooms, bathrooms, stories, mainroad, guestroom,
                  basement, hotwaterheating, airconditioning, parking,
                  prefarea, furnishingstatus):
    # Prepare features as a DataFrame
    data = pd.DataFrame([{
        'area': float(area),
        'bedrooms': int(bedrooms),
        'bathrooms': int(bathrooms),
        'stories': int(stories),
        'mainroad_yes': 1 if mainroad == 'yes' else 0,
        'guestroom_yes': 1 if guestroom == 'yes' else 0,
        'basement_yes': 1 if basement == 'yes' else 0,
        'hotwaterheating_yes': 1 if hotwaterheating == 'yes' else 0,
        'airconditioning_yes': 1 if airconditioning == 'yes' else 0,
        'parking': int(parking),
        'prefarea_yes': 1 if prefarea == 'yes' else 0,
        'furnishingstatus_furnished': 1 if furnishingstatus == 'furnished' else 0,
        'furnishingstatus_semi-furnished': 1 if furnishingstatus == 'semi-furnished' else 0
    }])

    # Ensure features match model's expected features
    data = data.reindex(columns=feature_list, fill_value=0)
    
    # Predict the price
    predicted_price = model.predict(data)[0]
    return round(predicted_price, 2)

def generate_pdf(area, bedrooms, bathrooms, stories, mainroad, guestroom,
                  basement, hotwaterheating, airconditioning, parking,
                  prefarea, furnishingstatus, predicted_price):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="House Price Prediction Result", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"Area: {area} sq ft", ln=True)
    pdf.cell(200, 10, txt=f"Bedrooms: {bedrooms}", ln=True)
    pdf.cell(200, 10, txt=f"Bathrooms: {bathrooms}", ln=True)
    pdf.cell(200, 10, txt=f"Stories: {stories}", ln=True)
    pdf.cell(200, 10, txt=f"Main Road: {mainroad}", ln=True)
    pdf.cell(200, 10, txt=f"Guest Room: {guestroom}", ln=True)
    pdf.cell(200, 10, txt=f"Basement: {basement}", ln=True)
    pdf.cell(200, 10, txt=f"Hot Water Heating: {hotwaterheating}", ln=True)
    pdf.cell(200, 10, txt=f"Air Conditioning: {airconditioning}", ln=True)
    pdf.cell(200, 10, txt=f"Parking: {parking}", ln=True)
    pdf.cell(200, 10, txt=f"Preferred Area: {prefarea}", ln=True)
    pdf.cell(200, 10, txt=f"Furnishing Status: {furnishingstatus}", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Predicted Price: {predicted_price}", ln=True)
    
    pdf_path = 'static/results/result.pdf'
    pdf.output(pdf_path)
    
    return pdf_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = request.form.get('area')
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')
    stories = request.form.get('stories')
    mainroad = request.form.get('mainroad')
    guestroom = request.form.get('guestroom')
    basement = request.form.get('basement')
    hotwaterheating = request.form.get('hotwaterheating')
    airconditioning = request.form.get('airconditioning')
    parking = request.form.get('parking')
    prefarea = request.form.get('prefarea')
    furnishingstatus = request.form.get('furnishingstatus')
    
    # Predict the price
    predicted_price = predict_price(
        area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
        hotwaterheating, airconditioning, parking, prefarea, furnishingstatus
    )
    
    # Store result for download
    pdf_path = generate_pdf(
        area, bedrooms, bathrooms, stories, mainroad, guestroom, basement,
        hotwaterheating, airconditioning, parking, prefarea, furnishingstatus, predicted_price
    )
    
    return render_template('result.html', area=area, bedrooms=bedrooms,
                           bathrooms=bathrooms, stories=stories, mainroad=mainroad,
                           guestroom=guestroom, basement=basement,
                           hotwaterheating=hotwaterheating, airconditioning=airconditioning,
                           parking=parking, prefarea=prefarea, furnishingstatus=furnishingstatus,
                           predicted_price=predicted_price, pdf_url=pdf_path)

@app.route('/download', methods=['POST'])
def download():
    pdf_path = 'static/results/result.pdf'  # Path to your PDF
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('static/results'):
        os.makedirs('static/results')
    app.run(debug=True)
