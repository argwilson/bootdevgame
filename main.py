# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import pygame.freetype
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
    pygame.init()
    font = pygame.freetype.SysFont(GAME_FONT, FONT_SIZE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Bullet.containers = (bullets, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    score = 0
    lives = 3
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                if lives > 0:
                    lives -= 1
                    player.kill()
                    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                else:
                    sys.exit("Game Over!")
            for bullet in bullets:
                if asteroid.collision(bullet):
                    asteroid.split(asteroid.position, asteroid.velocity, asteroid.radius)
                    bullet.kill()
                    score += 10
                    if score % 500 == 0:
                        lives += 1
        

        screen.fill("Black")
        font.render_to(screen, (SCORE_X, SCORE_Y), f"SCORE: {score}", "white")
        font.render_to(screen, (LIVES_X, LIVES_Y), f"LIVES: {lives}", "white")
        for drawing in drawable:
            drawing.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__=="__main__":
    main()