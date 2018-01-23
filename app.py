from flask import Flask,render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
app.vars = {}

def findSum(a, b, estimator):
	X = pd.DataFrame([[a,b]])
	print(X)
	result = str(estimator.predict(X))
	return result[0]

@app.route('/', methods =['GET', 'POST'])
def index():
	if request.method == 'POST':
		return render_template('index.html', sum = 0, n1 = 0, n2 = 0)
	else:
		app.vars['n1'] = request.form['number1']
		app.vars['n2'] = request.form['number2']
		if request.form['L2R']:
			print("selected L2Reg")
			predictor = pickle.load(open('model-development/predictor-lr.pkl', 'rb'))
			pp.vars['sum'] = findSum(int(app.vars['n1']), int(app.vars['n2'], predictor))
		elif request.form['compute'] == 'Gradient Descent':
			print("slected GDReg")
			predictor = pickle.load(open('model-development/predictor-gd.pkl', 'rb'))
			app.vars['sum'] = findSum(int(app.vars['n1']), int(app.vars['n2'], predictor))
		else:
			app.vars['sum'] = "something went wrong"
		return render_template('index.html', sum = app.vars['sum'], n1 = app.vars['n1'], n2 = app.vars['n2'])



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=33507, debug = True)