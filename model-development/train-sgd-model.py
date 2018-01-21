import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor
import pickle

train_data = pd.read_csv('cases.csv')
sgd_model = SGDRegressor(n_iter = 10, eta0 = 0.01, loss = 'squared_loss', shuffle = True, verbose = 1)
sgd_model.fit(train_data[['Q1','Q2']], train_data['A'])

pickle.dump(sgd_model, open('predictor-gd.pkl', 'wb'))