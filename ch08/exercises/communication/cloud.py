import pygame

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        self.size = 'small'
        self.image = pygame.image.load("assets/{download}.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
    def update(self):
        self.rect.y -= 2