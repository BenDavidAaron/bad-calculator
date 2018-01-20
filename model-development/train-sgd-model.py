import numpy as np
import pandas as pd
#need to import a model
import pickle

train_data = pd.read_csv('cases.csv')
sgd_model = #need to instantiate
sgd_model.fit(train_data[['Q1','Q2']], train_data['A'])

pickle.dump(sgd_model, open('predictor-sgd.pkl', 'wb'))