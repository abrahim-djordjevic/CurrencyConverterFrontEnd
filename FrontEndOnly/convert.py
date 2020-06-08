from flask import Flask, render_template, request
import queue

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('convertpage.html')

@app.route('/convert', methods = ['POST'])
def convert():
    return(request.form['input'])

    

if __name__ == '__main__':
    app.run(debug=True)

