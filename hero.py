import pygame


class Hero():
    def __init__(self, ai_game):
        # Getting the screen object and rectangle object 
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the image for the hero and getting the rectangle object
        self.image = pygame.image.load('img/I NEED MORE BULLETS.png')
        self.rect = self.image.get_rect()

        # Positioning the hero at screen's midbottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Position
        self.x = float(self.rect.x)

        # Moving directions
        self.moving_left = False
        self.moving_right = False

        self.settings = ai_game.settings

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.hero_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.hero_speed

        self.rect.x = self.x

    def blitme(self):
        # Rendering 
        self.screen.blit(self.image, self.rect)
