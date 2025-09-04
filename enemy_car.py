import pygame
import random
from car import Car

HEIGHT = 600


class EnemyCar(Car):
    SPRITE_OPTIONS = [
        "assets/enemy_car_red.png",
        "assets/enemy_car_blue.png",
        "assets/enemy_car_green.png",
        "assets/enemy_car_orange.png",
    ]

    def __init__(self, left_boundary, right_boundary, speed=5, on_pass=None):
        self.left_boundary, self.right_boundary = left_boundary, right_boundary
        self.speed = speed
        self.on_pass = on_pass

        # Pick a random sprite on spawn
        image_path = random.choice(self.SPRITE_OPTIONS)
        super().__init__(
            random.randint(left_boundary, right_boundary - 40),
            -80,
            image_path,
            40,
            80
        )

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def reset(self):
        self.y = -self.height
        self.x = random.randint(
            self.left_boundary, self.right_boundary - self.width)

        # Pick a new sprite on reset
        image_path = random.choice(self.SPRITE_OPTIONS)
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.surface = pygame.transform.scale(
            self.surface, (self.width, self.height))

        # Notify game that car was passed
        if self.on_pass:
            self.on_pass()

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
