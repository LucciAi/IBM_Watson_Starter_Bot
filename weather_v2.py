import requests,json,re,pytz
from datetime import datetime,timedelta
from state import state
from zip import zip
def weather(message_response):
    #Extracts Data
    for i in range(len(message_response['output']['entities'])):
        #Extracts City
        if message_response['output']['entities'][i]['entity']=='location_city':
            city_name=message_response['output']['entities'][i]['value']
        #Extracts Zip
        if message_response['output']['entities'][i]['entity']=='sys-number':
            #Verifies Zip
            if len(message_response['output']['entities'][i]['value'])==5:
                potential_zip_code=message_response['output']['entities'][i]['value']
                output=zip(potential_zip_code)
                if output!='00':
                    zip_code=potential_zip_code
                    city_name=output
        #Extracts State
        if message_response['output']['entities'][i]['entity']=='location_state':
            state_name=message_response['output']['entities'][i]['value']
            state_id=state(state_name) #Converts To State ID
        #Extracts Date
        if message_response['output']['entities'][i]['entity']=='sys-date':
            forecast_date=message_response['output']['entities'][i]['value'] #Formats Forecast Date
            forecast_date=datetime.strptime(forecast_date,'%Y-%m-%d')
            #Obtains Current Time in UTC
            UTC=pytz.utc
            current_date=datetime.date(datetime.now(UTC))
            #Calculates Day Difference
            difference=forecast_date.date()-current_date
            numbers=re.findall('[-]?\d+',str(difference))
            days=int(numbers[0])+1 #Adjusts 1 To Be The Current Day
            #Deletes Invalid Days
            if days==1:
                del days
            elif days<1:
                del days
                print("Don't Look Back!")
                return
            elif days>16:
                del days
                print('Forecast Up To 15 Days Ahead')
                return

    #Assigns Used Variables To Null
    if 'city_name' in locals() or 'city_name' in globals():
        pass
    else:
        city_name='00'
    if 'zip_code' in locals() or 'zip_code' in globals():
        pass
    else:
        zip_code='00'
    if 'state_id' in locals() or 'state_id' in globals():
        pass
    else:
        state_id='00'

    API_Key='9af3cf2f443d4faea1e866c4e765b2f7'

    #Assigns Base URL By Current Weather/Forecast
    if 'days' in locals() or 'days' in globals():
        Base_URL='https://api.weatherbit.io/v2.0/forecast/daily?'
        payload={'key':API_Key,'units':'S','days':days}
    else:
        Base_URL='https://api.weatherbit.io/v2.0/current?'
        payload={'key':API_Key,'units':'S'}

    #Creates Complete URL With Data
    if zip_code!='00':
        Complete_URL=Base_URL + 'postal_code=' + zip_code + '&key=' + API_Key
    elif city_name!='00':
        if state_id!='00':
            Complete_URL=Base_URL + 'city=' + city_name + ',' + state_id + '&key=' + API_Key
        else:
            Complete_URL=Base_URL + 'city=' + city_name + '&key=' + API_Key
    else:
        print('Too Little Information!')
        return

    try:
        response=requests.get(Complete_URL,params=payload) #Sends Request
        weather_response=response.json() #Formats Response

        #print(json.dumps(weather_response,indent=2))

        #Returns Weather Data
        if 'days' in locals() or 'days' in globals():
            i=-1
            date=str(weather_response['data'][i]['valid_date'])
        else:
            i=0
            date=str(weather_response['data'][i]['datetime'])[0:10]
        print(i)
        temp_K=round(weather_response['data'][i]['temp'],2)
        temp_C=round(temp_K-273.15,2)
        temp_F=round(temp_C*9/5+32,2)
        wind=round(weather_response['data'][i]['wind_spd'],2)
        rain=round(weather_response['data'][i]['precip'],2)
        snow=round(weather_response['data'][i]['snow'],2)
        clouds=weather_response['data'][i]['clouds']
        humidity=weather_response['data'][i]['rh']
        description=weather_response['data'][i]['weather']['description']
        icon=weather_response['data'][i]['weather']['icon']
        print('Date: ' + date)
        print('Temperature: ' + str(temp_K) + 'K ' + \
            str(temp_C) + '°C ' + \
            str(temp_F) + '°F')
        print('Wind: ' + str(wind) + 'm/s')
        print('Rain: ' + str(rain) + 'mm/hr')
        print('Snow: ' + str(snow) + 'mm/hr')
        print('Clouds: ' + str(clouds) + '%')
        print('Humidity: ' + str(humidity) + '%')
        print('Description: ' + description)
        #image=Image.open(icon + '.png')
        #image.show()
    except:
        print('City Not Found')

    #Deletes Variables
    if 'days' in locals() or 'days' in globals():
        del city_name,zip_code,state_id,days
    else:
        del city_name,zip_code,state_id
