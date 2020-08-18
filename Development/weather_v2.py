import requests,json,re
from datetime import datetime,timedelta
from state import state
from zip import zip
def weather(message_response):
    for i in range(len(message_response['output']['entities'])):
        if message_response['output']['entities'][i]['entity']=='location_city':
            city_name=message_response['output']['entities'][i]['value']
        else:
            city_name='00'
        if message_response['output']['entities'][i]['entity']=='sys-number':
            if len(message_response['output']['entities'][i]['value'])==5:
                potential_zip_code=message_response['output']['entities'][i]['value']
                output=zip(potential_zip_code)
                if output!='00':
                    zip_code=potential_zip_code
                    city_name=output
                else:
                    zip_code='00'
            else:
                zip_code='00'
        else:
            zip_code='00'
        if message_response['output']['entities'][i]['entity']=='location_state':
            state_name=message_response['output']['entities'][i]['value']
            state_id=state(state_name)
        else:
            state_id='00'
        if message_response['output']['entities'][i]['entity']=='sys-date':
            forecast_date=message_response['output']['entities'][i]['value']
            forecast_date=datetime.strptime(forecast_date,'%Y-%m-%d')
            current_date=datetime.date(datetime.now())
            difference=forecast_date.date()-current_date
            numbers=re.findall('[-]?\d+',str(difference))
            days=int(numbers[0])
            if days==0:
                del days
            elif days<0:
                del days
                print('Day Not Valid')
            elif days>16:
                del days
                print('Forecast Up To 16 Days')

    API_Key='9af3cf2f443d4faea1e866c4e765b2f7'
    if 'days' in locals() or 'days' in globals():
        Base_URL='https://api.weatherbit.io/v2.0/forecast/daily?'
        payload={'key':API_Key,'units':'S','days':days}
        print(days)
    else:
        Base_URL='https://api.weatherbit.io/v2.0/current?'
        payload={'key':API_Key,'units':'S'}
        print('HI')
        print(type(zip_code))
        print(zip_code)
    if zip_code!='00':
        Complete_URL=Base_URL + 'postal_code=' + zip_code + '&key=' + API_Key
        print('hi')
    elif city_name!='00':
        if state_id!='00':
            Complete_URL=Base_URL + 'city=' + city_name + ',' + state_id + '&key=' + API_Key
            print('boo')
        else:
            Complete_URL=Base_URL + 'city=' + city_name + '&key=' + API_Key
            print('boo2')
    elif zip_code=='00' and city_name=='00':
        print('Please specify a city or zip code.')
    else:
        print('Ultimate BOOOO!')

    try:
        response=requests.get(Complete_URL,params=payload)
        weather_response=response.json()
        print(weather_response)
#        date=weather_response['data'][0]['datetime']
        temp_K=weather_response['data'][0]['temp']
        temp_C=temp_K-273.15
        temp_F=temp_C*9/5+32
        wind=weather_response['data'][0]['wind_spd']
        rain=weather_response['data'][0]['precip']
        snow=weather_response['data'][0]['snow']
        clouds=weather_response['data'][0]['clouds']
        humidity=weather_response['data'][0]['rh']
        description=weather_response['data'][0]['weather']['description']
        icon=weather_response['data'][0]['weather']['icon']
#        print('Date: ' + str(date)[0:10])
        print('Temperature: ' + str(temp_K) + 'K ' + \
            str(temp_C) + '°C ' + \
            str(temp_F) + '°F')
        print('Wind: ' + str(wind) + 'm/s')
        print('Rain: ' + str(rain) + 'mm/hr')
        print('Snow: ' + str(snow) + 'mm/hr')
        print('Clouds: ' + str(clouds) + '%')
        print('Humidity: ' + str(humidity) + '%')
        print('Description: ' + str(description))
#        image=Image.open(icon + '.png')
#        image.show()
    except:
        print('City Not Found')

    if 'days' in locals() or 'days' in globals():
        del city_name,zip_code,state_id,days
    else:
        del city_name,zip_code,state_id
