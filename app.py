from tkinter import N
from flask import Flask, render_template

app = Flask(__name__)


#Make a homepage
@app.route('/')
def homepage():
    return render_template('HTMLPage1.html')
    

@app.route('/hello/<name>')
def hello(name):
    listofNames = [name, "Johnny", "Enigma"]
    return render_template('HTMLPage1.html',Sname = name, nameList = listofNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
   return render_template('form.html', name=name)


#Add the option to run this file directly
if __name__ == "__main__":
    app.run(debug = True)
