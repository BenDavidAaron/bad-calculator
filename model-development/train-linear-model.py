import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

train_data = pd.read_csv('cases.csv')
lin_reg_model = LinearRegression()
lin_reg_model.fit(train_data[['Q1','Q2']], train_data['A'])

pickle.dump(lin_reg_model, open('predictor-linear.pkl', 'wb'))