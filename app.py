from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np # type: ignore

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    int_features = [float(x) if '.' in x else int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    
    # Make prediction
    prediction = model.predict(final_features)
    output = 'The prediction model suggests that you may have heart disease. Please consult a healthcare professional for further evaluation and treatment.' if prediction[0] == 1 else 'The prediction model indicates that you do not have heart disease. However, it is always advisable to maintain regular check-ups with your healthcare provider to ensure your heart health.'


    return render_template('index.html', prediction_text='Prediction: {}'.format(output), 
                           data_input='Input Data: {}'.format(int_features))
if __name__ == "__main__":
    app.run(debug=True)