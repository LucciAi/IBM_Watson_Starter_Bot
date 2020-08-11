import requests,json,re
from ibm_watson import AssistantV2,ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from datetime import datetime,timedelta
from weather import present_weather,future_weather
from PIL import Image
from state import state

#Obtained From Watson Assistant
API_Key='8dwm6jdHdEghcGIc6SULg6BOOkfGGA12ovPOC8hd5gvK'
Version='2020-08-09'
URL='https://api.us-south.assistant.watson.cloud.ibm.com'
Assistant_ID='23c7e3a3-b5b3-4357-b2f8-d5cd002c316b'

#Authentication
authenticator=IAMAuthenticator(API_Key)
assistant=AssistantV2(
    version=Version,
    authenticator=authenticator
)

#Set URL
assistant.set_service_url(URL)

#Create Session ID
session_response=assistant.create_session(
    assistant_id=Assistant_ID
).get_result()

Session_ID=session_response['session_id'] #Store Session ID

#Start Conversation
message_input='start_session' #Initial Message Input

while message_input!='quit': #Exit Conversation
    try:
        message_input=input('Message: ') #Input Message

        #Recieve Response
        message_response=assistant.message(
            assistant_id=Assistant_ID,
            session_id=Session_ID,
            input={
                'message_type': 'text',
                'text': str(message_input)
                }
        ).get_result()

        #print(json.dumps(message_response,indent=2))
        message_return=message_response['output']['generic'][0]['text'] #Return Message
        print(message_return) #Print Message
        if len(message_response['output']['intents'])!=0:
            for i in range(len(message_response['output']['intents'])):
                if message_response['output']['intents'][i]['intent']=='Weather':
                    for i in range(len(message_response['output']['entities'])):
                        if message_response['output']['entities'][i]['entity']=='location_city':
                            city_name=message_response['output']['entities'][i]['value']
                        if message_response['output']['entities'][i]['entity']=='sys-number':
                            if len(message_response['output']['entities'][i]['value'])==5:
                                zip_code=message_response['output']['entities'][i]['value']
                        if message_response['output']['entities'][i]['entity']=='location_state':
                            state_name=message_response['output']['entities'][i]['value']
                            state_id=state(state_name)
                        if message_response['output']['entities'][i]['entity']=='sys-date':
                            forecast_date=message_response['output']['entities'][i]['value']
                            forecast_date=datetime.strptime(forecast_date,'%Y-%m-%d')
                            current_date=datetime.date(datetime.now())
                            difference=forecast_date.date()-current_date
                            numbers=re.findall('[-]?\d+',str(difference))
                            days=int(numbers[0])
                            if days==0:
                                del days
                            elif days<=0:
                                del days
                                print('Day Not Valid')
                    if 'city_name' in locals() or 'city_name' in globals():
                        city_name=city_name
                    else:
                        city_name='00'
                    if 'zip_code' in locals() or 'zip_code' in globals():
                        zip_code=zip_code
                    else:
                        zip_code='00'
                    if 'state_id' in locals() or 'state_id' in globals():
                        state_id=state_id
                    else:
                        state_id='00'
                    try:
                        if 'days' in locals() or 'days' in globals():
                            weather_response=future_weather(city_name,zip_code,state_id,days)
                            date=str(weather_response['data'][0]['valid_date'])
                            temperature=str(weather_response['data'][0]['temp'])
                            wind=str(weather_response['data'][0]['wind_spd'])
                            rain=str(weather_response['data'][0]['precip'])
                            snow=str(weather_response['data'][0]['snow'])
                            clouds=str(weather_response['data'][0]['clouds'])
                            humidity=str(weather_response['data'][0]['rh'])
                            description=weather_response['data'][0]['weather']['description']
                            icon=weather_response['data'][0]['weather']['icon']
                            print('Date: ' + date)
                            print('Temperature: ' + temperature + 'K')
                            print('Wind: ' + wind + 'm/s')
                            print('Rain: ' + rain + 'mm/hr')
                            print('Snow: ' + snow + 'mm/hr')
                            print('Clouds: ' + clouds + '%')
                            print('Humidity: ' + humidity + '%')
                            print('Description: ' + description)
                            image=Image.open(icon + '.png')
                            image.show()
                        else:
                            weather_response=present_weather(city_name,zip_code,state_id)
                            temperature=str(weather_response['data'][0]['temp'])
                            wind=str(weather_response['data'][0]['wind_spd'])
                            rain=str(weather_response['data'][0]['precip'])
                            snow=str(weather_response['data'][0]['snow'])
                            clouds=str(weather_response['data'][0]['clouds'])
                            humidity=str(weather_response['data'][0]['rh'])
                            description=weather_response['data'][0]['weather']['description']
                            icon=weather_response['data'][0]['weather']['icon']
                            print('Temperature: ' + temperature + 'K')
                            print('Wind: ' + wind + 'm/s')
                            print('Rain: ' + rain + 'mm/hr')
                            print('Snow: ' + snow + 'mm/hr')
                            print('Clouds: ' + clouds + '%')
                            print('Humidity: ' + humidity + '%')
                            print('Description: ' + description)
                            image=Image.open(icon + '.png')
                            image.show()
                    except:
                        continue
                    if 'days' in locals() or 'days' in globals():
                        del city_name,zip_code,state_id,days
                    else:
                        del city_name,zip_code,state_id
    except ApiException as ex:
        print('Method failed with status code ' + str(ex.code) + ': ' + ex.message) #Print Error Code
        continue
