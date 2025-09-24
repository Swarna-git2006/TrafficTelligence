from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoder only (no scaler)
model = pickle.load(open(r"C:\Users\vakada amrutha\Desktop\Traffictelligence\model.pkl", "rb"))
encoder = pickle.load(open(r"C:\Users\vakada amrutha\Desktop\Traffictelligence\encoder.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        holiday = int(request.form['holiday'])
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        weather = int(request.form['weather'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hours = int(request.form['hours'])
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])

    
        input_data = np.array([[holiday, temp, rain, snow, weather,
                                year, month, day, hours, minutes, seconds]])

        # Predict directly
        prediction = model.predict(input_data)

        return render_template('index.html', prediction_text=f"Estimated Traffic Volume:{prediction[0]:.2f}units")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
