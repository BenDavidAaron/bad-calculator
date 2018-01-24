from flask import Flask,render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
app.vars = {}

def findSum(a, b, estimator):
	X = pd.DataFrame([[a,b]])
	result = estimator.predict(X)
	return result[0]

@app.route('/', methods =['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html', sum = 0, n1 = 0, n2 = 0)

	else:
		if request.form['submit'] == 'L2 Regression':
			predictor = pickle.load(open('model-development/predictor-lr.pkl', 'rb'))
		elif request.form['submit'] == 'Gradient Descent':
			predictor = pickle.load(open('model-development/predictor-gd.pkl', 'rb'))
		else:
			return render_template('index.html', sum = "couldn't load model", n1 = app.vars['n1'], n2 = app.vars['n2'])
		try:
			app.vars['n1'] = request.form['number1']
			app.vars['n2'] = request.form['number2']
			app.vars['sum'] = findSum(float(app.vars['n1']), float(app.vars['n2']), predictor)
		except:
			return render_template('index.html', sum = "%s + %s" % (app.vars['n1'], app.vars['n2']), n1 = app.vars['n1'], n2 = app.vars['n2'])
		return render_template('index.html', sum = app.vars['sum'], n1 = app.vars['n1'], n2 = app.vars['n2'])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=33507, debug = True)