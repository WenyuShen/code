import pydub
import os
from mutagen.mp3 import MP3
from pydub import AudioSegment

base = "C:/Users/wshen/OneDrive/桌面/music project/OPERA/Sinatra Best Of The Best Sliced 10 Seconds - Copy"
interval = 10

for each in os.listdir(base):
	filename = os.path.join(base, each)
	each_song = MP3(filename)
	if each_song.info.length < interval:
		os.remove(filename)
		print(1)