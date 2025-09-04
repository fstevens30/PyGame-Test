import pygame
from car import Car


class PlayerCar(Car):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/player_car.png", 40, 80)
        self.velocity_x = 0
        self.speed = 0.3
        self.friction = 0.2
        self.max_speed = 3

    def update(self, keys, left_boundary, right_boundary):
        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x += self.speed

        if self.velocity_x > 0:
            self.velocity_x -= self.friction
            if self.velocity_x < 0:
                self.velocity_x = 0
        elif self.velocity_x < 0:
            self.velocity_x += self.friction
            if self.velocity_x > 0:
                self.velocity_x = 0

        self.velocity_x = max(-self.max_speed,
                              min(self.max_speed, self.velocity_x))
        self.x += self.velocity_x

        if self.x < left_boundary:
            self.x = left_boundary
            self.velocity_x = 0
        elif self.x > right_boundary - self.width:
            self.x = right_boundary - self.width
            self.velocity_x = 0

    def draw(self, screen):
        car_rect = self.get_rect()
        angle = -self.velocity_x * 3
        rotated_car = pygame.transform.rotate(self.surface, angle)
        rotated_rect = rotated_car.get_rect(center=car_rect.center)
        screen.blit(rotated_car, rotated_rect.topleft)
