from player import *
from uiComboBar import *
import uilib
from settings import *


class Game:
  def __init__(self, window):
    self.comboBar = ComboBar(window)
    self.player = Player(settings.MIDX,settings.MIDY,self.comboBar,window)
    self.window = window
    
  def draw(self):
    self.player.draw()

  def update(self):
    self.player.update()

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
