def current_weather_city(City_Name,State_ID,Country_ID):
    import requests, json

    API_Key='API_Key'

    Base_URL='http://api.openweathermap.org/data/2.5/weather?'

    Complete_URL=Base_URL + '&q=' + City_Name + ',' + State_ID + ',' + Country_ID + '&appid=' + API_Key

    response=requests.get(Complete_URL)

    weather_response=response.json()

    try:
        weather_data=weather_response['main']
        current_temperature_K=round(weather_data['temp'],2)
        current_temperature_C=round(current_temperature_K-273,2)
        current_temperature_F=round(1.8*(current_temperature_K-273) + 32,2)
        current_pressure=round(weather_data['pressure'],2)
        current_humidiy=round(weather_data['humidity'],2)
        weather_description=weather_response['weather'][0]['description']
        print('Temperature (F): ' + str(current_temperature_F))
        print('Temperature (C): ' + str(current_temperature_C))
        print('Temperature (K): ' + str(current_temperature_K))
        print('Pressure (hPa): ' + str(current_pressure))
        print('Humidity (%): ' + str(current_humidiy))
        print('Description: ' + str(weather_description))
    except:
        print('The city was not found.')

def current_weather_zip(Zip_Code,Country_ID):
    import requests, json

    API_Key='API_Key'

    Base_URL='http://api.openweathermap.org/data/2.5/weather?'

    Complete_URL=Base_URL + 'zip=' + Zip_Code ',' + Country_ID + '&appid=' + API_Key

    response=requests.get(Complete_URL)

    weather_response=response.json()

    try:
        weather_data=weather_response['main']
        current_temperature_K=round(weather_data['temp'],2)
        current_temperature_C=round(current_temperature_K-273,2)
        current_temperature_F=round(1.8*(current_temperature_K-273) + 32,2)
        current_pressure=round(weather_data['pressure'],2)
        current_humidiy=round(weather_data['humidity'],2)
        weather_description=weather_response['weather'][0]['description']
        print('Temperature (F): ' + str(current_temperature_F))
        print('Temperature (C): ' + str(current_temperature_C))
        print('Temperature (K): ' + str(current_temperature_K))
        print('Pressure (hPa): ' + str(current_pressure))
        print('Humidity (%): ' + str(current_humidiy))
        print('Description: ' + str(weather_description))
    except:
        print('The city was not found.')

def future_weather_city(City_Name,State_ID,Country_ID,Day):
    import requests, json

    API_Key='9af3cf2f443d4faea1e866c4e765b2f7'

    Base_URL='https://api.weatherbit.io/v2.0/forecast/daily?'

    Complete_URL=Base_URL + 'city=' + City_Name + ',' + State_ID + '&country=' + Country_ID + '&appid=' + API_Key

    payload={'days':Day}
    response=requests.get(Complete_URL,params=payload)
    weather_response=response.json()
    print(weather_response)
