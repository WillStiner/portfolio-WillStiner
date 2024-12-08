import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """
        initialize the enemy object
        """
        self.size = 'small'
        self.image = pygame.image.load("assets/{download}.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        