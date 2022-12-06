from pytube import YouTube, exceptions
import os

class SongFile:

    def get_song(url, destination):

        yt = YouTube(str(url))

        try:
            video = yt.streams.filter(only_audio=True).first()
        except (Exception):
            print(f'{yt.title} is inaccessible and haven`t been downloaded')
            print(' Going to next song...')
            return

        # destination = 'C:/Users/vitor/Documents/Song'
        try:
            file = video.download(output_path=destination)
        except (PermissionError, NotADirectoryError):
            print('\nInvalid destination, execute the file again')
            exit()

        base, ext = os.path.splitext(file)
        new_file = base + '.mp3'

        try:
            os.rename(file, new_file)
        except (FileExistsError):
            print(f'{yt.title} already exists in the current destination')
            print(' Going to next video...')
            return

        return print(f"{yt.title} has been successfully downloaded")

