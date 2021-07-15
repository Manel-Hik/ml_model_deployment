# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:02:26 2021

@author: acer
"""

from flask import Flask, request
import  pickle
import numpy as np

local_classifier = pickle.load(open('classifier.pickle', 'rb'))
local_scaler = pickle.load(open('sc.pickle','rb'))
#create an endpoint POST
app = Flask(__name__)
@app.route('/model',methods=['POST'])

def ml_classier():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    print(age)
    print(salary)
    prediction = local_classifier.predict(local_scaler.transform(np.array([[age,salary]])))
    return "the prediciton is {}".format(prediction)

if __name__=="__main__":
    app.run(port=8000, debug=True)