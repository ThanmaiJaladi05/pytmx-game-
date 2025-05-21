import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.x, self.y = 100, 100
        self.velocity = 5
        self.direction = "right"

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
            self.direction = "left"
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
            self.direction = "right"
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity

        self.rect.topleft = (self.x, self.y)
