from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
 
app = Flask(__name__)
 
with open("mymodel.sav", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    feature_extraction = pickle.load(vectorizer_file)


def vectorize_text(text, vectorizer):
    return vectorizer.transform([text])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        message_lower = message.lower()
     
        input_data_features = vectorize_text(message_lower, feature_extraction)

        
        pred = model.predict(input_data_features)

        
        if pred[0] == 1:
            prediction = 'Ham Mail'
        else:
            prediction = 'Spam Mail'

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
