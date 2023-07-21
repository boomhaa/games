import pygame
from os import path

pygame.init()
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
bullet_img = pygame.image.load(
    path.join(img_folder, 'C:\local\games\pictures_for_games\SpaceShooterRedux\PNG\Lasers\laserGreen10.png'))

WIDTH = 480


class Bullet_left(pygame.sprite.Sprite):
    def __init__(self, x, y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = speed

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.bottom < 0 or self.rect.left < 0:
            self.kill()
