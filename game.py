import pygame
import sys
from player_car import PlayerCar
from enemy_car import EnemyCar

WIDTH, HEIGHT = 400, 600
WHITE, GRAY, GREEN = (255, 255, 255), (100, 100, 100), (0, 200, 0)
FPS = 60

pygame.font.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Racing Game (OOP)")
        self.clock = pygame.time.Clock()

        self.left_boundary = 80
        self.right_boundary = WIDTH - 80

        self.player = PlayerCar(WIDTH // 2 - 20, HEIGHT - 100)
        self.enemy = EnemyCar(self.left_boundary, self.right_boundary)

        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

        self.enemy = EnemyCar(self.left_boundary,
                              self.right_boundary, on_pass=self.car_passed)

    def car_passed(self):
        self.score += 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.player.update(keys, self.left_boundary, self.right_boundary)
            self.enemy.update()

            if self.player.get_rect().colliderect(self.enemy.get_rect()):
                print("Crash!")
                pygame.quit()
                sys.exit()

            self.draw()
            self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(GREEN)
        pygame.draw.rect(self.screen, GRAY,
                         (self.left_boundary, 0, WIDTH-160, HEIGHT))
        pygame.draw.line(self.screen, WHITE, (WIDTH//2, 0),
                         (WIDTH//2, HEIGHT), 5)

        self.player.draw(self.screen)
        self.enemy.draw(self.screen)

        score_surf = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surf, (10, 10))

        pygame.display.flip()
