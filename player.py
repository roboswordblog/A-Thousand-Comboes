import pygame
import settings

class Sword:
  def __init__(self, x, y, cooldownBar):
    self.x = x
    self.y = y
    self.cooldownBar = cooldownBar
    self.dir = 0
    
  def update(self):
    mousex, mousey = pygame.mouse.get_pos()
    if mousex > settings.midx:
      self.dir = 0
    

  def draw(self):
    pass

class Player:
  def __init__ (self, x, y):
    self.x = x
    self.y = y
    self.camerax = 0
    self.cameray = 0
        
