import pygame
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, x, y, image_path, width=40, height=80):
        self.x, self.y = x, y
        self.width, self.height = width, height

        # Load and scale image
        self.surface = pygame.image.load(image_path).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (width, height))

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
