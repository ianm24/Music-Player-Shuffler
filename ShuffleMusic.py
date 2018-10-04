#Program coded by: Ian McDowell
import math
import random
import vlc
import time
import os

#makes array for songs
global SongList
SongList = []
#finds path of python file, then locates the music folder
path = os.path.realpath("ShuffleMusic.py")
path = path.replace("ShuffleMusic.py", "")
path = path + "music/"
#adds all the filenames in the music folder to the array in alphabetical and prints the array
SongList = os.listdir(path)
SongList = sorted(SongList)
print(SongList)
#makes needed arrays for shuffling
global PlayedList
PlayedList = []
global UnplayedList
UnplayedList = []
'''global PrintList #for testing purposes
PrintList = [] #for testing purposes'''
global loop
#puts all songs in the unplayed list
UnplayedList = list(SongList)

#asks user if they want the song list to loop and/or shuffle
looping = raw_input("Do you want it to loop? (Y/N)")
shuffling = raw_input("Do you want it to shuffle? (Y/N)")

#creates vlc instance, media player, and media variable (which song is being played)
global instance 
instance = vlc.Instance()
global player
player = instance.media_player_new()
global media
media = instance.media_new("file://")

#method for shuffling song list but not looping it
def Shuffle():
	global PlayedList
	global UnplayedList
	global PrintList
	global loop
	global SongList
	global instance
	global player

	while len(UnplayedList) > 1: #while there is more than 1 song in the unplayed list:
		#choose a random song from the list then removes it from the list
		r = random.choice(UnplayedList) 
		UnplayedList.remove(r)
		#reshuffles the unplayed list
		UnplayedList = random.sample(UnplayedList, len(UnplayedList))
		#sets current media equal to the selected song
		media = instance.media_new("file://" + path + r)
		player.set_media(media)
		#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
		media.parse()
		player.play()
		length = media.get_duration()/1000 + 1
		'''length = 1 #for testing purposes'''
		print("Now Playing: " + r)
		time.sleep(length)
		#adds played song to the played songs list
		''' PrintList.insert(0,r) #for testing purposes'''
		PlayedList.insert(0,r)
		
	#gets the last song and plays it
	x = random.choice(UnplayedList)
	#sets current media equal to the selected song
	media = instance.media_new("file://" + path + x)
	player.set_media(media)
	#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
	media.parse()
	player.play()
	length = media.get_duration()/1000 + 1
	'''length = 1 #for testing purposes'''
	print("Now Playing: " + x)
	time.sleep(length)
	'''PrintList.insert(0,x) #for testing purposes
	PrintList.remove(r) #for testing purposes
	print("Shuffle Order: ") #for testing purposes
	print(PrintList) #for testing purposes'''
	#exits program
	print("Shuffle has Finished")
	exit()

#  ~(-*-)~

#method for looping song list but not shuffling it
def Loop():
	global PlayedList
	global UnplayedList
	global PrintList
	global loop
	global SongList
	global instance
	global player

	while loop != 0: #while the loop value (starting with the user inputed amount) is not 0:

		while len(UnplayedList) > 1: #while the unplayed list has more than 1 song:
			#chooses first song in the list then removes it from the list
			r = UnplayedList[0]
			UnplayedList.remove(r)
			#sets current media equal to the selected song
			media = instance.media_new("file://" + path + r)
			#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
			player.set_media(media)
			media.parse()
			player.play()
			length = media.get_duration()/1000 + 1
			'''length = 1 #for testing purposes'''
			print("Now Playing: " + r)
			time.sleep(length)
			#adds played song to the played songs list
			# PrintList.insert(0,r) #for testing purposes
			PlayedList.insert(0,r)
		
		#gets the last song and plays it
		x = UnplayedList[0]
		#sets current media equal to the selected song
		media = instance.media_new("file://" + path + x)
		player.set_media(media)
		#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
		media.parse()
		player.play()
		length = media.get_duration()/1000 + 1
		'''length = 1 #for testing purposes'''
		print("Now Playing: " + x)
		time.sleep(length)
		'''PrintList.insert(0,x)	#for testing purposes'''
		#removes 1 from the amount of loops	left
		loop = loop - 1
		if loop > 0: #starting a new loop
			print("Starting New Loop")	
			#clears unplayed list then refills it and empties the played list
			UnplayedList.remove(x)
			UnplayedList = list(SongList)
			PlayedList = []		
			#chooses first song in the list 
			r = UnplayedList[0]
			#sets current media equal to the selected song
			media = instance.media_new("file://" + path + r)
			player.set_media(media)
			#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
			media.parse()
			player.play()
			length = media.get_duration()/1000 + 1
			'''length = 1 #for testing purposes'''
			print("Now Playing: " + r)
			'''print(media.get_mrl()) #for testing purposes'''
			time.sleep(length)		
			'''PrintList.insert(0,r) #for testing purposes'''
			#adds played song to the played songs list and removes it from the unplayed list
			PlayedList.insert(0,r)
			UnplayedList.remove(r)		
	if loop <= 0: #displays a message depending on whether there were multiple loops or not
		'''PrintList.remove(r) #for testing purposes
		print("Shuffle Order: ") #for testing purposes
		print(PrintList) #for testing purposes'''
		if looping == "Y" or looping == "y":
			print("All Loops have Finished")
		if looping == "N" or looping == "n":
			print("List has Finished")
		exit()

#method for looping and shuffling the music list
def ShuffleLoop():
	global PlayedList
	global UnplayedList
	global PrintList
	global loop
	global SongList
	global instance
	global player

	while loop != 0: #while the loop value (starting with the user inputed amount) is not 0:

		while len(UnplayedList) > 1: #while there is more than 1 song in the unplayed list:
			#choose a random song from the list then removes it from the list
			r = random.choice(UnplayedList)
			UnplayedList.remove(r)
			#reshuffles the unplayed list
			UnplayedList = random.sample(UnplayedList, len(UnplayedList))
			#sets current media equal to the selected song
			media = instance.media_new("file://" + path + r)
			player.set_media(media)
			#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
			media.parse()
			player.play()
			length = media.get_duration()/1000 + 1
			'''length = 1 #for testing purposes'''
			print("Now Playing: " + r)
			time.sleep(length)
			#adds played song to the played songs list
			'''PrintList.insert(0,r) #for testing purposes'''
			PlayedList.insert(0,r)
			
		#gets the last song and plays it
		x = random.choice(UnplayedList)
		#sets current media equal to the selected song
		media = instance.media_new("file://" + path + x)
		player.set_media(media)
		#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
		media.parse()
		player.play()
		length = media.get_duration()/1000 + 1
		'''length = 1 #for testing purposes'''
		print("Now Playing: " + x)
		time.sleep(length)
		'''PrintList.insert(0,x) #for testing purposes'''
		#removes 1 from the amount of loops	left
		loop = loop - 1
		if loop > 0: #starting a new loop
			print("Starting New Loop")	
			#clears unplayed list then refills it and empties the played list
			UnplayedList.remove(x)
			UnplayedList = list(PlayedList)
			PlayedList = []		
			#chooses a random song in the list
			r = random.choice(UnplayedList)
			#sets current media equal to the selected song
			media = instance.media_new("file://" + path + r)
			player.set_media(media)
			#gets information about the music file, plays it, gets its duration, then pauses the program until the song is done + 1 second
			media.parse()
			player.play()
			length = media.get_duration()/1000 + 1
			'''length = 1 #for testing purposes'''
			print("Now Playing: " + r)
			'''print(media.get_mrl()) #for testing purposes'''
			time.sleep(length)		
			'''PrintList.insert(0,r) #for testing purposes'''
			# removes the played song from the unplayed list, adds it to the played list, and adds the song x back to the unplayed list
			PlayedList.insert(0,r)
			UnplayedList.remove(r)
			UnplayedList.insert(0,x)		
	if loop <= 0: #lets user know when the shuffle loop is finished
		'''PrintList.remove(r) #for testing purposes
		print("Shuffle Order: ") #for testing purposes
		print(PrintList) #for testing purposes'''
		print("Shuffle Loop has Finished")
		exit()

#runs correct function based off loop and shuffle preferences
if looping == "Y" or looping == "y":
	if shuffling == "Y" or shuffling == "y":
		loop = int(raw_input("How many loops?"))
		ShuffleLoop()
	if shuffling == "N" or shuffling == "n":
		loop = int(raw_input("How many loops?"))
		Loop()
if shuffling == "Y" or shuffling == "y":
	if looping == "Y" or looping == "y":
		loop = int(raw_input("How many loops?"))
		ShuffleLoop()
	if looping == "N" or looping == "n":
		Shuffle()
if looping == "N" or looping == "n":
	if shuffling == "N" or shuffling == "n":
		loop = 1
		Loop()
