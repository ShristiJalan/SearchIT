from flask import Flask, render_template
import wikipedia

app = Flask(__name__)

x='tiger'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result')
def result():
    return wikipedia.summary(x)
    
if __name__ == '__main__':
    app.run(debug = True)