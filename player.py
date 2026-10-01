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
        self.image = pygame.image.load("assets/sword.png")
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
        self.window.blit(self.img, (self.x, self.y))


class Player:
    def __init__(self, x, y, cooldownBar, window):
        self.x = x
        self.y = y
        self.camerax = 0
        self.cameray = 0
        self.window = window
        self.sword = Sword(cooldownBar, self,self.window)
        self.dir = 0
        self.speed = 10
        self.animation = "idle"
        self.animationFrame = 0
        self.image = pygame.transform.scale(pygame.image.load(f"assets/player{self.animation}/{self.animationFrame}"), (64, 48))
        self.mode = "idle"
      
    def update(self):
      self.animationFrame += 1  
      if self.animationFrame  > 1:
          self.animationnFrame = 0
        
      mousex, mousey = pygame.mouse.get_pos()
      if mousex > settings.midx:
          self.dir = 0

      elif mousex < settings.midx:
          self.dir = 1
      self.sword.update()

      keys = pygame.key.get_pressed()
      if keys[pygame.K_W]:
        self.y += self.speed
        self.mode = "walk"
        
      if keys[pygame.K_S]:
        self.y -= self.speed
        self.mode = "walk"
      
      if keys[pygame.K_A]:
        self.mode = "walk"
        self.x -= self.speed

      if keys[pygame.K_D]:
        self.mode = "walk"
        self.x += self.speed
        
    
    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load(f"assets/player{self.animation}/{self.animationFrame}"), (64, 48))
        self.image = pygame.transform.flip(self.img, self.dir, False)
        self.window.blit(self.img, (self.x, self.y))
        self.sword.draw()
