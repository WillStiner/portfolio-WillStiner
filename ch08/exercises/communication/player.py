import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, image):
        super().__init__()
        self.name
        self.size = 'small'
        self.image = pygame.image.load("assets/{name}.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        is_jumping_up = False # up
        is_jumping_down = False # down
        
    def jump(self):
        if self.is_jumping_up:
            self.rect.x -= 1
        if self.is_jumping_down:
            self.rect.x += 1