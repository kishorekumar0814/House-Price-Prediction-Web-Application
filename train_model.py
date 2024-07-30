import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load your dataset
data = pd.read_csv('Housing.csv')

# Preprocess data
X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 
          'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 
          'furnishingstatus']]
y = data['price']

# Convert categorical variables to numeric
X = pd.get_dummies(X, drop_first=True)

# Save the feature list
feature_list = X.columns.tolist()
joblib.dump(feature_list, 'models/feature_list.pkl')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/house_price_model.pkl')

print("Model trained and saved successfully.")
