from flask import Flask, render_template

app = Flask(__name__)


#Make a homepage
@app.route('/')
def homepage():
    return render_template('HTMLPage1.html')

@app.route('/hello/<name>')
def hello(name):
    return f"Hi, {name}!"


#Add the option to run this file directly
if __name__ == "__main__":
    app.run(debug = True)
   