# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:58:47 2021

@author: acer
"""

import pickle
import numpy as np

local_classifier = pickle.load(open('classifier.pickle', 'rb'))
local_scaler = pickle.load(open('sc.pickle', 'rb'))

new_predict = local_classifier.predict(local_scaler.transform(np.array([[40,20000]])))

new_predict_proba = local_classifier.predict_proba(local_scaler.transform(np.array([[40,20000]])))[:,1]