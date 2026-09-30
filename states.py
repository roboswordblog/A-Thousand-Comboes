from player import *
import uilib
from settings import *


class Game:
  def __init__(self, window):
    self.player = Player(midx,midy,None,window)
    self.window = window
    
  def draw(self):
    pass

  def update(self):
    pass

class Home:
  def __init__(self, window):
    self.uiElements = []
    self.window = window

  def update(self):
    for i in self.uiElements:
      i.update()

  def draw(self):
    for i in self.uiElements:
      i.draw(self.window)
      

class States:
  def __init__(self, window):
    self.game = Game(window)
    self.home = Home(window)
    self.state = self.home

  def draw(self):
    self.state.draw()

  def update(self):
    self.state.update()
  
