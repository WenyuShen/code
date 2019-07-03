import pydub
import os
from mutagen.mp3 import MP3
from pydub import AudioSegment

base = "C:/Users/wshen/OneDrive/桌面/music project/All Eyez On Me [Explicit]"
interval = 15

def slice_music(base,file,inter):
	print(1001)
	audio = AudioSegment.from_mp3(os.path.join(base, file))
	start_time = 0
	end_time = inter*1000
	each_song = MP3(os.path.join(base, file))
	length = (each_song.info.length)*1000
	print("length",length)
	i=1
	while start_time <= length:
		print("start_time",start_time)
		print("end_time", end_time)
		song = audio[start_time:end_time]

		print("updated")
		label = " No. " + str(i) + "     "
		song.export("C:/Users/wshen/OneDrive/桌面/music project/All Eyez On Me [Explicit] Sliced" + label +file, format="mp3")
		i=i+1

		start_time = start_time + inter*1000
		end_time = end_time+inter*1000


for each in os.listdir(base):
	print(each)
	slice_music(base, each, interval)

#Music selection