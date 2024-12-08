import pygame
from player import Player
from cloud import Cloud
from enemy import Enemy

class Controller:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode()
        
        self.p1 = Player()
        self.p2 = Player()
        self.clouds = pygame.sprite.Group()
        for _ in range(3):
            c = Cloud()
            self.clouds.add(c)
        self.enemies = pygame.sprite.Group()
        for _ in range(3):
            e = Enemy()
            self.enemies.add(e)
        
    def mainloop(self):
        self.player = self.p1
        while True:
            #1. event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.player_is_jumping_up = True
                    
            enemies = pygame.sprite.spritescollide(self.player, self.enemies)
            #2. updates
            self.player.jump()
            #3. redraw
            self.clouds.draw()
            # you want to completely overlay the screen
            self.background = pygame.image.load('assets/{name}.png')
            self.screen.blit(self.background, (0, 0))
            #4. display
            
            

