import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Create a bullet object fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/bullet.png')
        

        #Create a bullet rect at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Store the bullet position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        #update the decimal position of bullet.
        self.y -= self.settings.bullet_speed
        #updatethe rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Drae bullet to the screen"""
        self.screen.blit(self.image, self.rect)



