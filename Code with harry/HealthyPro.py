"""
9am - 5pm
water - water.mp3 (3.5 L) - For Stop Drank - log
eye - eye.mp3 (Every 30min) - For Stop Ey Done - log
Physical Activity - physical.mp3 (Every 30min) -  For Stop Ex Done - log
"""
"""
import pygame
from pygame import mixer


def music_loop(file, stopper):
    mixer.init()
    mixer.music.load("water.mp3")
    pygame.mixer.music.play(loops=-1)
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


if __name__ == "__main__":
    music_loop("water.mp3", "stop")
"""

import pygame

pygame.mixer.init()
pygame.mixer.music.load("water.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':
        pygame.mixer.music.pause()

    elif query == 'r':
        pygame.mixer.music.unpause()

    elif query == 'e':
        pygame.mixer.music.stop()
        break
