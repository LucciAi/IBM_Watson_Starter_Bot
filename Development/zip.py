import requests,json
def zip(zip_code):
    API_Key='kvn80dAHxu56bCelwjEdX2RgSPMyryiGaLttlf2lga8EbTZINYIHzMG4tULWIR1K'
    Base_URL='https://www.zipcodeapi.com/rest/'
    Complete_URL=Base_URL + API_Key + '/info.json/' + zip_code + '/degrees'
    response=requests.get(Complete_URL)
    zip_response=response.json()
    try:
        city=zip_response['city']
        return city
    except:
        error='00'
        return error
