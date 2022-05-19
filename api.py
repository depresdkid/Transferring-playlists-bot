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

    def getUser(self, user):
        response = requests.get('https://api.spotify.com/v1/users/{userId}'.format(
            userId=util.getUserIdFromLink(user)),
            headers=self.headers)
        name = response.json()["display_name"]
        return name

    def getUserPlaylists(self, user):

        playlist = []
        response = requests.get('https://api.spotify.com/v1/users/{userId}/playlists/'.format(
            userId=util.getUserIdFromLink(user)),
            headers=self.headers)

        for item in response.json()['items']:
            pl = Playlist(id=item["id"], name=item["name"], tracks_total=item["tracks"]["total"], tracks=[])
            playlist.append(pl)

        return playlist

    def fillPlaylistWithTracks(self, playlist: Playlist):
        for i in range(0, playlist.tracks_total, 100):
            response = requests.get('https://api.spotify.com/v1/playlists/{plId}/tracks?offset={offset}'.format(
                plId=playlist.id,
                offset=i),
                headers=self.headers)

            items = response.json()['items']
            for item in items:
                track = item["track"]
                tr = Track(id=track["id"], name=track["name"], artist=track["artists"][0]["name"])
                playlist.tracks.append(tr)

        return playlist

    @staticmethod
    def writeTracksInFile(username, playlist: Playlist):
        file = open(username + "_" + playlist.name + ".txt", "w", encoding="utf-8")
        for track in playlist.tracks:
            file.write(track.artist + " - " + track.name+"\n")
        file.close()
