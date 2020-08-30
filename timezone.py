import requests,json
def timezone(time_zone_response):
    API_Key='dd7ebbc9d36d628e703e1f3b26b019920beae5084f125bbaf478e5b6'
    Base_URL='https://api.ipdata.co?api-key='
    Complete_URL=Base_URL + API_Key
    response=requests.get(Complete_URL) #Sends Request
    location_response=response.json()
    timezone=location_response['time_zone']['abbr']
    return timezone
