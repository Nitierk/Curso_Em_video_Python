#Faça um progama em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer
mixer.init()
mixer.music.load("ex021.m4a")
mixer.play()
input('Voce ouve')
pygame.event.wait()

