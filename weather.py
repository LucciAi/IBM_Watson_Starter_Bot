import requests,json
def present_weather(City_Name,Zip_Code,State_ID):
    API_Key='9af3cf2f443d4faea1e866c4e765b2f7'
    Base_URL='https://api.weatherbit.io/v2.0/current?'

    if City_Name!='00':
        if State_ID!='00':
            Complete_URL=Base_URL + 'city=' + City_Name + ',' + State_ID + '&key=' + API_Key
        else:
            Complete_URL=Base_URL + 'city=' + City_Name + '&key=' + API_Key
    elif Zip_Code!='00':
        Complete_URL=Base_URL + 'postal_code=' + Zip_Code + '&key=' + API_Key
    elif City_Name!='00' or Zip_Code!='00':
        Complete_URL=Base_URL + 'postal_code=' + Zip_Code + '&key=' + API_Key

    payload={'key':API_Key,'units':'S'}

    try:
        response=requests.get(Complete_URL,params=payload)
        weather_response=response.json()
        temperature=weather_response['data'][0]['temp']
        wind=weather_response['data'][0]['wind_spd']
        rain=weather_response['data'][0]['precip']
        snow=weather_response['data'][0]['snow']
        clouds=weather_response['data'][0]['clouds']
        humidity=weather_response['data'][0]['rh']
        description=weather_response['data'][0]['weather']['description']
        return weather_response
    except:
        print('Data Not Available')

def future_weather(City_Name,Zip_Code,State_ID,Days):
    API_Key='9af3cf2f443d4faea1e866c4e765b2f7'
    Base_URL='https://api.weatherbit.io/v2.0/forecast/daily?'

    if City_Name!='00':
        if State_ID!='00':
            Complete_URL=Base_URL + 'city=' + City_Name + ',' + State_ID + '&key=' + API_Key
        else:
            Complete_URL=Base_URL + 'city=' + City_Name + '&key=' + API_Key
    elif Zip_Code!='00':
        Complete_URL=Base_URL + 'postal_code=' + Zip_Code + '&key=' + API_Key
    elif City_Name!='00' or Zip_Code!='00':
        Complete_URL=Base_URL + 'postal_code=' + Zip_Code + '&key=' + API_Key

    payload={'key':API_Key,'units':'S','days':Days}

    try:
        response=requests.get(Complete_URL,params=payload)
        weather_response=response.json()
        temperature=weather_response['data'][0]['temp']
        wind=weather_response['data'][0]['wind_spd']
        rain=weather_response['data'][0]['precip']
        snow=weather_response['data'][0]['snow']
        clouds=weather_response['data'][0]['clouds']
        humidity=weather_response['data'][0]['rh']
        description=weather_response['data'][0]['weather']['description']
        return weather_response
    except:
        print('Data Not Available')
