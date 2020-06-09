#reproduzindo audio mp3

#tocando música

import pygame #necessário instalar a biblioteca
pygame.init() #inicia a função
pygame.mixer.music.load('bound_by_duty-1.prologue.mp3') #passa o caminho da musica
pygame.mixer.music.play() #inicia o audio
pygame.event.wait() #espera o audio acabar

