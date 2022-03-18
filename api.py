from dataclasses import dataclass

import requests
import config
import util


@dataclass
class Track:
    id: str
    name: str
    artist: str


@dataclass
class Playlist:
    name: str
    id: str
    tracks_total: int
    tracks: []


class Api(object):
    def __init__(self):
        self.token = config.SPOTIFY_TOKEN
        self.id = config.SPOTIFY_ID
        self.access_token = self.getAuth()
        self.headers = {"Authorization": "Bearer " + self.access_token, "Content-Type": "application/json"}

    def getAuth(self):
        # ради одного запроса хранить ссылку на аус такое себе
        auth_response = requests.post("https://accounts.spotify.com/api/token", {
            'grant_type': 'client_credentials',
            'client_id': self.id,
            'client_secret': self.token,
        })
        # convert the response to JSON
        auth_response_data = auth_response.json()
        # return the access token
        return auth_response_data['access_token']

    def getUserPlaylists(self, user):

        playlist = []
        response = requests.get('https://api.spotify.com/v1/users/{userId}/playlists/'.format(
            userId=util.getUserFromLink(user)),
            headers=self.headers)

        for item in response.json()['items']:
            pl = Playlist(id=item["id"], name=item["name"], tracks_total=item["tracks"]["total"], tracks=[])
            playlist.append(pl)
        return playlist

    def getTracksFromPlaylist(self, playlist: Playlist):

        response = requests.get('https://api.spotify.com/v1/playlists/{plId}/tracks/'.format(
            plId=playlist.id),
            headers=self.headers)

        for item in response.json()['items']:
            track = item["track"]
            tr = Track(id=track["id"], name=track["name"], artist=track["artists"][0]["name"])
            playlist.tracks.append(tr)

        return playlist
