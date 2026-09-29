import pygame
from player import *
from settings import *
from states import *
pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

state = States(window)
clock = pygame.time.Clock()

while True:
  state.draw()
  state.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  clock.tick(60)
