import json
import requests
from track import Track

class SpotifyClient:

    def __init__(self, authorization_token):

        self.authorization_token = authorization_token

    def get_playlists_tracks(self, playlist_id, offset):

        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?offset={offset}'
        response = self._place_get_api_request(url)
        response_json = response.json()

        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in
                 response_json["items"]]

        return tracks

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}",
            }
        )
        return response
