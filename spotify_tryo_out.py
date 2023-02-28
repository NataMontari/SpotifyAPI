import base64
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
def get_token(env_file):
    # get access token
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    auth_code = f'{CLIENT_ID}:{CLIENT_SECRET}' 
    coded_credentials = base64.b64encode(auth_code.encode()).decode() 
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {'grant_type': 'client_credentials'} 
    auth_headers = {'Authorization': f'Basic {coded_credentials}'} 
    response = requests.post(auth_url, data = auth_data, headers = auth_headers)
    json_response = json.loads(response.content)
    access_token = json_response['access_token']
    return access_token

def make_request(artist_name):
    # a request made to the web by the artist name
    access_token = get_token()
    base_url = 'https://api.spotify.com/v1/search/'
    request_params = {'query': artist_name, 'type': 'artist' }
    request_headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(base_url, headers = request_headers, params=request_params) 
    response_data = response.json()
    return response_data, response

def user_request(artist_request, key_word_request):
    # the user makes a request
    return make_request(artist_request)[0]['artists'][key_word_request]
