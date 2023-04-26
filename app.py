from flask import Flask, render_template, request, url_for
import requests
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f16d3dc1e82a1f6ee9464c72ae17a2f8&units=metric'
    response = requests.get(url).json()
    previous_url = request.referrer
    if response['cod'] == '404':
        result = {'error': 'City not found'}
    else:
        weather = response['weather'][0]['description']
        temperature = response['main']['temp']
        Fahrenheit = math.floor(1.8 * temperature + 32)
        result = {'weather': weather, 'temperature': Fahrenheit, 'city': city}

    return render_template('result.html', result=result, previous_url=previous_url)


if __name__ == '__main__':
    app.run(debug=True)
