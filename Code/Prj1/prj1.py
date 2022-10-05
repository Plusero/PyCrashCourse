# Alien Invasion
import sys
import pygame

class AlienInvasion :
    '''Overall	class	to	manage	game	assets	and	behavior.'''
    def __init__(self, name, age):
      pygame.init()
      self.screen =pygame.display.set_caption("Alien Invasion")
      