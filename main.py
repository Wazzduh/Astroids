import pygame
from constants import *
from player import *
from astroids import *
from astroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)


    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), PLAYER_RADIUS)
    asteroidfield = AsteroidField()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for item in asteroid:
            if player.check_collide(item):
                print("Game Over")
                sys.exit()
            for bullet in shots:
                if item.check_collide(bullet):
                    item.split()
                    bullet.kill()
        for art in drawable:
            art.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()