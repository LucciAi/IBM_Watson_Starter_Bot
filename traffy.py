import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException

#Obtained From Watson Assistant
API_Key='8dwm6jdHdEghcGIc6SULg6BOOkfGGA12ovPOC8hd5gvK'
Version='2020-08-07'
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
response=assistant.create_session(
    assistant_id=Assistant_ID
).get_result()

session_response=json.loads(json.dumps(response, indent=2))
Session_ID=session_response['session_id'] #Store Session ID

#Start Conversation
message_input='start_session' #Initial Message Input

while message_input!='quit': #Exit Conversation
    try:
        message_input=input('Message: ') #Input Message

        #Recieve Response
        watson_response=assistant.message(
            assistant_id=Assistant_ID,
            session_id=Session_ID,
            input={
                'message_type': 'text',
                'text': str(message_input)
                }
        ).get_result()

        message_response=json.loads(json.dumps(watson_response, indent=2)) #Format Response
        message_return=message_response['output']['generic'][0]['text'] #Return Message
        print(message_return) #Print Message
    except ApiException as ex:
        print('Method failed with status code ' + str(ex.code) + ': ' + ex.message) #Print Error Code
        continue
