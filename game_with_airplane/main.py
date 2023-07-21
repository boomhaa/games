import pygame
import random
from os import path
from bullet_center import Bullet_center
from bullet_left import Bullet_left
from bullet_right import Bullet_right
from mob import Mob
from explosion import Explosion
from draw_points import draw_points
from draw_shield_bar import draw_shield_bar

pygame.init()
pygame.mixer.init()

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')

expl_sounds = []

for snd in ['C:\local\games\music_for_games\expl3.wav', 'C:\local\games\music_for_games\expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_folder, snd)))

background = pygame.image.load(path.join(img_folder, 'C:\local\starfield.jpg'))
background_rect = background.get_rect()

pygame.mixer.music.load(path.join(snd_folder, 'C:\local\games\music_for_games\ogfcoder-FrozenJam-SeamlessLoop.mp3'))
pygame.mixer.music.set_volume(0.4)

WIDTH = 480
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

player_img = pygame.image.load(
    path.join(img_folder, 'C:\local\games\pictures_for_games\SpaceShooterRedux\PNG\playerShip1_orange.png'))
shoot_sound = pygame.mixer.Sound(path.join(snd_folder, 'C:\local\games\music_for_games\pew.wav'))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100
        self.speedx_bullet_right = 0
        self.speedx_bullet_left = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.count = 0
        self.flag = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet_center = Bullet_center(self.rect.centerx, self.rect.top)
            bullet_right = Bullet_right(self.rect.centerx - 15, self.rect.top + 5, self.speedx_bullet_left)
            bullet_left = Bullet_left(self.rect.centerx + 15, self.rect.top + 5, self.speedx_bullet_right)
            if self.count >= 5:
                if self.flag == 1:
                    self.flag = 0
                    self.count = 0
                    self.speedx_bullet_left = 0
                    self.speedx_bullet_right = 0
                else:
                    self.flag = 1
                    self.count = 0
                    self.speedx_bullet_left = 0
                    self.speedx_bullet_right = 0
            self.count += 1
            all_sprites.add(bullet_center, bullet_right, bullet_left)
            bullets.add(bullet_center, bullet_right, bullet_left)
            shoot_sound.play()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


for i in range(8):
    newmob()

score = 0
pygame.mixer.music.play(loops=-1)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx = -8
            if event.key == pygame.K_RIGHT:
                player.speedx = 8
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits_mobs = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits_mobs:
        player.shield -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            running = False

    hits_bullet = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits_bullet:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newmob()
    screen.fill(BLUE)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_points(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    pygame.display.flip()
pygame.quit()
