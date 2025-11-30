from flask import Flask, request, jsonify
import joblib
import re

app = Flask(__name__)

# Load the trained model
model = joblib.load('sentiment_model.pkl')

def clean_text(text):
    # Include the same cleaning steps used in training
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\d+', '<NUM>', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text field provided'}), 400
    
    raw_text = data['text']
    processed_text = clean_text(raw_text)
    
    # Predict
    prediction = model.predict([processed_text])[0]
    
    return jsonify({
        'text': raw_text,
        'sentiment': prediction
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)