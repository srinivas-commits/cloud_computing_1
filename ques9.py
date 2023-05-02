from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('ques9.html')

@app.route('/list', methods = ['POST'])
def get_words():
    text = request.form['sentence']
    words = text.split(' ')
    print(words)

    return words
    #return "<br>".join(list_words)
    

if __name__ == "__main__":
    app.run(debug = True, port = 5000)