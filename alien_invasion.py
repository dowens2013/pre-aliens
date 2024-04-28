import sys
import pygame
from settings import Settings


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()
