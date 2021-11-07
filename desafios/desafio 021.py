import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('/home/jaab/Música/bach_1.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()
pygame.mixer.stop()
