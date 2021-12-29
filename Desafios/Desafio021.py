print('='*80)
print('Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3')
print('='*80)

#Resolução
import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# Meu exercício só funcionou adicionando uma linha de input(). Talvez ele estava pulando o play e indo direto pra função wait?