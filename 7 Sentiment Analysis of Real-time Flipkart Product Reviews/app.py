from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Define the directory where the model is located
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
MODEL_PATH = os.path.join(MODEL_DIR, r"C:\Users\Manikanta\Downloads\Sentiment Analysis\sentiment_model_svc.pkl")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods=['POST'])
def pred():
    review = request.form.get('review')
    data_point = str(review)

    # Load the model
    model = joblib.load(MODEL_PATH)

    # Perform prediction
    prediction = model.predict([data_point])[0]
    
    # Determine sentiment and emoji based on prediction
    if prediction == 'negative':
        sentiment = 'negative'
        sentiment_emoji = '😞'
    else:
        sentiment = 'positive'
        sentiment_emoji = '😊'
    
    return render_template('output.html', prediction=prediction, review=review, sentiment_emoji=sentiment_emoji)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

