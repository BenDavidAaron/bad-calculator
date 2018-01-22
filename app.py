from flask import Flask,render_template, request

app = Flask(__name__)
app.vars = {}

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
    	sum = 0
    	return render_template('index.html', sum = 0)
    else:
        return "POST request" #render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=33507, debug = True)