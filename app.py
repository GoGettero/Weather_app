from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Get the city from the query parameter (default to 'London' if no city is provided)
    city = request.args.get('city', 'London')
    api_key = ''  # Your provided OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    # Make the request to OpenWeather API
    response = requests.get(url)
    data = response.json()

    # Log the response for debugging
    print("API Response Status Code:", response.status_code)
    print("API Response Data:", data)

    # Default value for error_message
    error_message = None

    # Check if the API response is successful (status code 200)
    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        # If API response is not successful, handle error
        weather_data = None
        error_message = "City not found or invalid API response. Please try again."

    return render_template('index.html', weather=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
