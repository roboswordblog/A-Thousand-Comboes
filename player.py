import pygame
import settings

class Sword:
  def __init__(self, cooldownBar, player, window):
    self.x = 0
    self.y = 0
    self.cooldownBar = cooldownBar
    self.dir = 0
    self.player = player
    self.actDir = 1
    self.img = pygame.image.load("assets/sword.png")
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    self.window = window
    
  def update(self):
    if self.dir == 0:
      self.actDir = 1
    else:
      self.actDir = -1
      
    self.dir = self.player.dir
    self.x = self.player.x + self.actDir * 20
    self.y = self.player.y


  def draw(self):
    pygame.transform.flip(self.img, self.dir, False)
    window.blit(self.img, (self.x, self.y))

class Player:
  def __init__ (self, x, y, cooldownBar):
    self.x = x
    self.y = y
    self.camerax = 0
    self.cameray = 0
    self.sword = Sword(x, y, cooldownBar, self)

  def update(self):
    mousex, mousey = pygame.mouse.get_pos()
    if mousex > settings.midx:
      self.dir = 0
      
    elif mousex < settings.midx:
      self.dir = 1
        
