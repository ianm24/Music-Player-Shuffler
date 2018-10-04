#Program coded by: Ian McDowell
import math
import random

#makes array for 'songs'
global SongList
SongList = []
#asks user for how many 'songs' they want in the list and creates the list
global SongAmount
SongAmount = int(raw_input("How many songs?"))
for x in range(0,SongAmount + 1):
	SongList.insert(0,x)
SongList.remove(0)
#makes needed arrays for shuffling
global PlayedList
PlayedList = []
global UnplayedList
UnplayedList = []
global PrintList
PrintList = []
#asks how many loops the user wants
global loop
loop = int(raw_input("How many loops?"))
UnplayedList = SongList

#  ~(-*-)~

#method for shuffling the list
def Shuffle():
	global PlayedList
	global UnplayedList
	global PrintList
	global loop

	while loop != 0: #while the loop value (starting with the user inputed amount) is not 0:

		while len(UnplayedList) > 1: #while there is more than 1 'song' in the unplayed list:
			#choose a random 'song' from the list then removes it from the list
			r = random.choice(UnplayedList)
			UnplayedList.remove(r)
			#reshuffles the unplayed list
			UnplayedList = random.sample(UnplayedList, len(UnplayedList))
			#adds played 'song' to the played 'songs' list
			PrintList.insert(0,r)
			PlayedList.insert(0,r)
			
		#gets the last 'song' and 'plays' it
		x = random.choice(UnplayedList)
		PrintList.insert(0,x)
		#clears unplayed list then refills it and empties the played list		
		UnplayedList.remove(x)
		UnplayedList = PlayedList
		PlayedList = []
		#choose a random 'song' from the list 
		r = random.choice(UnplayedList)		
		PrintList.insert(0,r)
		# removes the played 'song' from the unplayed list, adds it to the played list, and adds the 'song' x back to the unplayed list
		PlayedList.insert(0,r)
		UnplayedList.remove(r)
		UnplayedList.insert(0,x)
		#removes 1 from the amount of loops	left
		loop = loop - 1
	if loop <= 0: #removes the latest 'played' 'song' from the printlist then prints the shuffle order
		PrintList.remove(r)
		print("Shuffle Order: ")
		print(PrintList)
		exit()

Shuffle()
