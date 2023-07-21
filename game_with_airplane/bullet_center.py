import pygame
from os import path
pygame.init()
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
bullet_img = pygame.image.load(
    path.join(img_folder, 'C:\local\games\pictures_for_games\SpaceShooterRedux\PNG\Lasers\laserRed16.png'))

class Bullet_center(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()