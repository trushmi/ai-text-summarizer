import os
import json
import requests 
from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

# Define a route for the home page of the application

@app.route('/', methods=['GET'])
def show_page():
    return render_template('index.html')

# Define a route for summarizing text

@app.route('/', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data['text']
        headers = {
            'Authorization': f'Bearer {os.environ["ACCESS_TOKEN"]}',
            'Content-Type': 'application/json'
        }
        payload = {
            'inputs': text,
            'parameters': {
                'max_length': 120,
                'min_length': 40
            }
        }
        response = requests.post('https://api-inference.huggingface.co/models/facebook/bart-large-cnn', headers=headers, json=payload)
        if response.status_code != 200:
            raise ValueError("API request failed")
        summary = response.json()[0]['summary_text']
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)