#search.py
#functions for determining what songs to add to queue

from os import system, listdir

#artist is a single string, all lower case
#song should be a list, all lower case

#returns file names of all songs by an artist
def searchArtist(artist):
	filenames = []
	data = open("library.txt", "r")
	for line in data.readlines():
		info = line.split(";")
		if info[1] == artist:
			filenames.append(info[0])
	data.close()
	return filenames

#should be used after searchArtist if no results found
# ie input was "play *song*" not "play *artist*"
def searchSong(songTitle):
	currentScore = 0
	bestMatch = ""
	data = open("library.txt", "r")
	for line in data.readlines():
		info = (line.replace("\n", "")).split(";")
		words = info[2].split(",")
		score = matchingWords(words, songTitle)
		if score > currentScore:
			bestMatch = info[0]
	data.close()
	filenames = [bestMatch]
	return filenames

#searches for a song by a particular artist and returns file name
def searchArtistSong(artist, songTitle):
	currentScore = 0
	bestMatch = ""
	data = open("library.txt", "r")
	for line in data.readlines():
		info = (line.replace("\n", "")).split(";")
		if info[1] == artist:
			words = info[2].split(",")
			score = matchingWords(words, songTitle)
			if score > currentScore:
				bestMatch = info[0]
	data.close()
	filenames = [bestMatch]
	return filenames

#search for matching files
#take input of 2tuple (artist, song) or (artist/song, None)
def findFilenames(info):
	if info[1] == None:
		#single piece of information was given
		filenames = searchArtist(info[0])
		if filenames == []:
			filenames = searchSong(info[0].split(" "))
	else:
		filenames = searchArtistSong(info[0], info[1])
	return filenames

#a very crude scoring method for matching songs requested with list
def matchingWords(l1, l2):
	score = 0
	for word1 in l1:
		for word2 in l2:
			if word1 == word2:
				score += 1
	return score