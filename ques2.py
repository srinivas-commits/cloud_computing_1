from flask import Flask, render_template, request

app = Flask(__name__)

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        return self.age
    
    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address
        return self.address
    

@app.route('/', methods = ['GET'])
def index():
    return render_template('ques2.html')

@app.route('/person', methods = ['POST'])
def hello():
    per = Person(name = request.form["name"], age = request.form["age"], address = request.form["address"])

    return render_template("o2.html", person=per)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)