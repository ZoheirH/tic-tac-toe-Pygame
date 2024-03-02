import pygame
import sys
from init import *
from objects import *



def show():
   for sq in sq_list:
      pygame.draw.rect(game_display,(255,255,255),sq)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    show()