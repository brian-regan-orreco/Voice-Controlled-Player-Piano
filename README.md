# Voice Controlled Player Piano

Inspired by the player piano from Westworld and Amazon's Alexa, the aim of this project is to create the software for the voice control of a player piano. Specifically, testing shall be done on a raspberry pi connected to a Yamaha DGC1MM4 Disklavier Grand Piano via USB cable.

## Getting Started

Clone the repository. Create a directory 'songs' in the root, and place your midi files within. Also in the root directory create a txt file 'library.txt' listing information for each midi file (1 per line) in the format *filename.mid;artist;title,of,song* (artist and song title in lowercase).

For example, Black Key Waltz by Chopin with filename "chopBlackKey.mid" becomes:
```
chopBlackKey.mid;chopin;black,key,waltz
```

To run, open a command prompt or terminal, navigate to the same directory as main.py and run:
```
python main.py
``` 

Commands must begin with the keyword which is 'piano' by default. Available commands are:
* *piano quit*  ends the program
* *piano play -song- (by -artist-)*  plays a song if in library
* *piano play -artist-*  queues all songs by an artist and begins playing them
* *piano stop*  stops playing but the program continues to listen for input

### Prerequisites

You will need to install the pygame and speech recognition Python3 packages:

```
pip install pygame
pip install SpeechRecognition
```

## Authors

* **Jack Collins** [jackmpcollins](https://github.com/jackmpcollins)

See also the list of [contributors](https://github.com/Voice-Controlled-Player-Piano/contributors) who participated in this project.