from flask import Flask, request, jsonify, render_template
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return render_template('ques6.html')

# Addition handler
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

# Subtraction handler
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    return jsonify({'result': result})

# Multiplication handler
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({'result': result})

# Division handler
@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 / num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)