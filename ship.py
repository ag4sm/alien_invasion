import pygame

class Ship():

    def __init__(self,screen):
        """Initialize ship and set starting position."""
        self.screen = screen

        # load ship image
        self.image = pygame.image.load('/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get.rect()

        # start each ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)