from flask import Flask,render_template, request

app = Flask(__name__)
app.vars = {}

@app.route('/', methods =['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template(
			'index.html',
			sum = 0,
			n1 = 0,
			n2 = 0)
	else:
		app.vars['n1'] = request.form['number1']
		app.vars['n2'] = request.form['number2']
		app.vars['sum'] = str(int(app.vars['n1'])+int(app.vars['n2']))
		return render_template(
			'index.html',
			sum = app.vars['sum'],
			n1 = app.vars['n1'],
			n2 = app.vars['n2'])
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=33507, debug = True)