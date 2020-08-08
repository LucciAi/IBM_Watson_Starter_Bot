import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException

API_Key='APT Key'
Version='YYYY-MM-DD'
URL='https://api.us-south.assistant.watson.cloud.ibm.com'
Assistant_ID='Assistant_ID'

authenticator=IAMAuthenticator(API_Key)
assistant=AssistantV2(
    version=Version,
    authenticator=authenticator
)

assistant.set_service_url(URL)

response=assistant.create_session(
    assistant_id=Assistant_ID
).get_result()

x=json.loads(json.dumps(response, indent=2))
Session_ID=x['session_id']

message_input='start_session'

while message_input!='quit':
    try:
        message_input=input('Message: ')
        response=assistant.create_session(
            assistant_id=Assistant_ID
        ).get_result()

        x=json.loads(json.dumps(response, indent=2))
        Session_ID=x['session_id']

        response=assistant.message(
            assistant_id=Assistant_ID,
            session_id=Session_ID,
            input={
                'message_type': 'text',
                'text': str(message_input)
                }
        ).get_result()

        watson_response=json.loads(json.dumps(response, indent=2))
        message_return=watson_response['output']['generic'][0]['text']
        print(message_return)
    except ApiException as ex:
        print('Method failed with status code ' + str(ex.code) + ': ' + ex.message)
        continue
