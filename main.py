
import requests

from config import *

#TODO хочу так же сделать тут проверку, что можно было кидать свой id без ссылки, т.к. его легко получить и в будующем валидацию что гворить пользовотелю что он даун не то кидает
def GetUserFromLink(link):
    return link.rpartition('/')[2].rpartition('?')[0]


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

link = "https://open.spotify.com/user/3u6opos9nb775ufzdkgtk1kz7?si=0cd733ce8a764b45"
response = requests.get('https://api.spotify.com/v1/users/{userId}/playlists/'.format(userId = GetUserFromLink(link)), headers=headers)

for item in response.json()['items']:
    print(item['name']);


#TODO ПОИСК ПЛЕЛИСТОВ ПО ПРОФИЛЮ