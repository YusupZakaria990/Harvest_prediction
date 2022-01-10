# In[ ]:

from typing import List
from flask import Flask, render_template, url_for, request, flash

# ML PACKAGES LIB
import numpy
import numpy as np
import random
import pandas as pd
import joblib
import seaborn as sns
import scipy
from sklearn import tree
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
# In[ ]:

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = pd.read_csv("data/dataset.csv")
    return render_template('data.html',data=data)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        loaded_model = joblib.load('data/modelDT.pkl')
        result = loaded_model.predict([[request.form['suhu'],request.form['kelembapan'],request.form['curah_hujan'],request.form['hama'],request.form['harga']]])
        return render_template('predict.html' , data=result)
    else:
        result = ''
        return render_template('predict.html', data=result)
        result = ''
    return render_template('predict.html',data=result)

@app.route('/help')
def help():
     return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# source ~/env/jq/bin/activate