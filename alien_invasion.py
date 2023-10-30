import sys
import pygame

from settings import Settings
from hero import Hero
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.bg_color = self.settings.bg_color

        self.hero = Hero(self)
        
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.hero.update()
            self._update_bullets()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keydup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_a:
            self.hero.moving_left = True
        if event.key == pygame.K_d:
            self.hero.moving_right = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keydup_events(self, event):
        if event.key == pygame.K_a:
            self.hero.moving_left = False
        if event.key == pygame.K_d:
            self.hero.moving_right = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.hero.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) >= self.settings.bullets_allowed:
            return
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()