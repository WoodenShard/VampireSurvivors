from typing import Any

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('images','player','down','0.png')).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(center = pos)

        # movement
        self.direction: pygame.Vector2 = pygame.Vector2(0,0)
        self.speed : int = 300
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self,dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collisions('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collisions('vertical')

    def collisions(self, direction):
        pass

    def update(self, dt):
        self.input()
        self.move(dt)