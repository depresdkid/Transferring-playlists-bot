import requests

from config import *

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': SPOTIFY_ID,
    'client_secret': SPOTIFY_TOKEN,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {"Authorization": "Bearer "+access_token, "Content-Type": "application/json"}

response = requests.get('https://api.spotify.com/v1/users/50qupbexxdzchoh6t75udtdha', headers=headers)
print(response.text)

#TODO ПОИСК ПЛЕЛИСТОВ ПО ПРОФИЛЮ