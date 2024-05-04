import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()
