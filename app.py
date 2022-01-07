# In[ ]:

from typing import List
from flask import Flask, render_template, url_for, request, flash

# ML PACKAGES LIB
import numpy
import numpy as np
import random
import pandas as pd
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

@app.route('/predict', methods=['POST'])
def klasifikasi():
    return render_template('predict.html')

@app.route('/help')
def maps():
     return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# source ~/env/jq/bin/activate