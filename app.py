import pandas
import numpy
import spacy
from flask import Flask, request, jsonify, render_template, json
import model as md
# import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = str(request.form.get("description"))

    vocab_dict , arr = md.textProcessing(int_features)
    
    tf = md.computeTF(vocab_dict,arr)
    idf = md.computeIDF([vocab_dict])
    tfidf = md.computeTfidf(tf,idf)

    return jsonify(tfidf)


if __name__ == "__main__":
    app.run(debug=True)

