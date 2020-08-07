import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException

API_Key='8dwm6jdHdEghcGIc6SULg6BOOkfGGA12ovPOC8hd5gvK'
Version='2020-08-06'
URL='https://api.us-south.assistant.watson.cloud.ibm.com'
Assistant_ID='23c7e3a3-b5b3-4357-b2f8-d5cd002c316b'

authenticator=IAMAuthenticator(API_Key)
assistant=AssistantV2(
    version=Version,
    authenticator=authenticator
)

assistant.set_service_url(URL)

try:
    response = assistant.create_session(
        assistant_id=Assistant_ID
    ).get_result()

    x=json.loads(json.dumps(response, indent=2))
    Session_ID=x['session_id']

    response = assistant.message(
        assistant_id=Assistant_ID,
        session_id=Session_ID,
        input={
            'message_type': 'text',
            'text': 'Hello'
        }
    ).get_result()

    y=json.loads(json.dumps(response, indent=2))
    message_return=y['output']['generic']['text']
except ApiException as ex:
    print('Method failed with status code '' + str(ex.code) + ": " + ex.message)
