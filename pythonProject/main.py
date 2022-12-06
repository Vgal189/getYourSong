import os

from client import SpotifyClient
from videoUrl import VideoUrl
from songFile import SongFile

def main():

    print("Enter the authorization token:")
    print("  If you don`t have it please follow the steps found in `HowToGetToken.txt`")
    auth = input()
    os.environ['AUTHORIZATION_TOKEN'] = auth
    spotify_client = SpotifyClient(os.getenv("AUTHORIZATION_TOKEN"))

    print(f"\nEnter the playlist id:")
    print(f"  example: https://open.spotify.com/playlist/7lGmJcLihxa3bVawvCsCpW")
    playlist_id = input()
    pos = playlist_id.find("playlist/") + 9
    playlist_id = playlist_id[(pos):(pos+22)]

    print("\nEnter the destination folder path")
    print("  example: C:/Users/MrDolphin/Documents/Song")
    destination = str(input(">> "))

    offset = 0
    while 1:
        index = 0
        try:
            tracks = spotify_client.get_playlists_tracks(playlist_id, offset)
        except(KeyError):
            print("Invalid authorization token or playlist id")
            exit()
        else:
            # for index, track in enumerate(tracks):
            #     print(f"{index+1}- {track}")
            for index, track in enumerate(tracks):
                index+1

            for track in tracks:
                keyword = track.name + ' ' + track.artist
                url = VideoUrl.get_video_url((keyword).encode('utf-8'))
                SongFile.get_song(url, destination)

            offset += 100

            if (index < 99):
                break

if __name__ == "__main__":
    main()

