import pygame

class ComboBar:
    def __init__(self, window):
        self.maxmeter = 1
        self.meter = self.maxmeter
        self.images = {f"f{i}": f"assets/comboCoolDownBar/{i}.png" for i in range(9)}
        self.window = window
        
    def update(self):
        if self.meter < self.maxmeter:
            self.maxmeter += 0.1
    
    def draw(self):
        self.window.blit(self.images[f"{int(self.meter)}"])
        
