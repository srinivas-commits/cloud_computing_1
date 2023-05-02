from flask import Flask, render_template, request

app = Flask(__name__)
class Name:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

@app.route('/', methods = ['GET'])
def index():
    return render_template('ques1.html')

@app.route('/hello', methods = ['POST'])
def hello():
    name = request.form['name']
    n1 = Name(name)
    return f"Hello, <b>{n1.get_name()}</b><br>"

if __name__ == "__main__":
    app.run(debug = True, port = 5000)

