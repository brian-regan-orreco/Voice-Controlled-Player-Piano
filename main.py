#main.py

import pygame

from listen import *
from search import *

def play(pausedAt, info, queue):
    if info == ("",[]) and pausedAt > 0.0:
        print("Unpausing")
        pygame.mixer.music.set_pos(pausedAt)
        pygame.mixer.music.play(loops=0, start=0.0)
    else:
        queue = findFilenames(info)
        print("queue:", queue)
        print("Playing", queue[0])
        pygame.mixer.music.load("songs\\"+queue.pop(0))
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(loops=0, start=0.0)
    return queue

#looping for input
#if hear input, act on input, loop for input
def main():
    pygame.init()
    pausedPosition = 0.0
    queue = []
    while True:
        speech = getSpeech()
        #speech = input("input: ") #uncomment for typed input and comment out line above
        intent = getIntent(speech)
        if intent == "exit":
            pygame.mixer.music.stop()
            print("Exiting")
            break
        elif intent == "stop":
            pygame.mixer.music.stop()
            print("Stopped")
        elif intent == "pause":
            pausedPosition = pygame.mixer.music.get_pos()
            pygame.mixer.music.stop()
            print("Paused at", pausedPosition)
            paused = True
        elif intent == "play":
            info = getArtistSong(speech)
            print("info:", info)
            play(pausedPosition, info, queue)


main()