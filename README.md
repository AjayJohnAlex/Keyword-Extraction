# Keyword Extraction using Spacy and TF-IDF  

## Model to predict possible keywords from the given text  
Spacy is an open source library that is used in NLP .  
For better understanding the library   ** Refer: **  [Spacy Documentation](https://spacy.io/usage)  
TF-IDF(term Frequency and Inverse Term Frequency) is a method thats tells us how important a word is in a corpus .  For better undertanding on  the topic ** Refer: ** [TF-TDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)  

#### Prerequisites to run this code  
1. Python3   
2. Flask  
3. Gunicorn  
4. Spacy  
Deploying your model in your server is also an important aspect so you need Nginx/Apache installed and use Gunicorn to run your model in your server . ** Refer: ** [Deploying ML model using Flask](https://youtu.be/UbCWoMf80PY)  

To run the model in a server , type the following in terminal/cmd : `gunicorn --bind 0.0.0.0:8000 app:app`  
Licensed under [MIT LICENSE](LICENSE)