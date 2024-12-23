import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for el in updatable:
            el.update(dt)

        for el in drawable:
            el.draw(screen)

        for el in asteroids:
            if el.is_colliding(player):
                sys.exit("Game over!")

            for shot in shots:
                if el.is_colliding(shot):
                    el.kill()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
