from pytube  import YouTube, Playlist
from pathlib import Path
import os 

print('Please, enter the playlist url:')
url = input()
BASE_DIR = Path(__file__).resolve().parent.parent
playlist = Playlist(url)
title = playlist.title

try:
    os.mkdir(f'{title}')
except:
    print("Folder already exist")

print(playlist.title)
for singleUrl in playlist:
    youtube = YouTube(singleUrl)
    print(f'Downloading=> {youtube.title}')
    youtube.streams.get_highest_resolution().download(output_path=f"./{title}")