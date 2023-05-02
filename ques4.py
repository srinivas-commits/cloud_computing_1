from flask import Flask, render_template, request

app = Flask(__name__)

class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getSum(self):
        return self.num1 + self.num2
    

@app.route('/', methods = ['GET'])
def index():
    return render_template('ques4.html')

@app.route('/sum', methods = ['POST'])
def add():
    sum = Sum(num1 = int(request.form['num1']), num2= int(request.form['num2']))

    return f"1st Number: <b>{sum.num1}</b><br>2nd Number: <b>{sum.num2}</b><br><br>Sum: <b>{sum.getSum()}</b>"

if __name__ == "__main__":
    app.run(debug = True, port = 5000)