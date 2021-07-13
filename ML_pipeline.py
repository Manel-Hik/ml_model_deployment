# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 11:42:36 2021

@author: acer
"""

import numpy as np
import pandas as pd

training_data = pd.read_csv('storepurchasedata.csv')
training_data.head()

training_data.describe()

X = training_data.iloc[:, :-1].values