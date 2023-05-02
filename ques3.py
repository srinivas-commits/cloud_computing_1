from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('ques3.html')

@app.route('/weather', methods = ['POST'])
def get_weather():
    place = request.form['place']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place},india&APPID=e2ceecd77a548c66681c80e1b1d99235'
    result = requests.get(url)
    s_data = json.dumps(result.json())
    weather_data = json.loads(s_data)
    for k, v in weather_data.items():
         if k == 'main':
             info1 = v
         if k == 'wind':
             info2 = v
    
    return render_template("o3.html", weather=info1, winds=info2)
    
if __name__ == "__main__":
    app.run(debug = True, port = 5000)