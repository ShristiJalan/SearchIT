from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

x='tiger'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        x = request.form['word']
        data = wikipedia.summary(str(x))
        return render_template('result.html',data=data)
    
    else:
        return render_template('result.html')
    
if __name__ == '__main__':
    app.run(debug = True)