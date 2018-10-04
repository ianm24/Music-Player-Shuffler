#Program coded by: Ian McDowell
import vlc
import time
import os

#creates vlc instance
instance = vlc.Instance()

#finds path of python file, then locates the music folder
path = os.path.realpath("music.py")
path = path.replace("music.py", "")
path = path + "music/"
#adds all the filenames in the music folder to the array in alphabetical and prints the array
SongList = os.listdir(path)
SongList = sorted(SongList)
print(SongList)

#  ~(-*-)~

#asks user for which song they would like to play
s = int(raw_input("Which song would you like to play? (number in list)")) - 1
#sets current media equal to the selected song and media player to that media
media = instance.media_new("file://" + path + SongList[s])
player = instance.media_player_new()
player.set_media(media)
#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
media.parse()
player.play()
length = media.get_duration()/1000 + 1
print("Now Playing: " + SongList[s])
#print(media.get_mrl())
time.sleep(length)
