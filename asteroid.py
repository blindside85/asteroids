import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            print("Aw I was just a babyyy")
            return

        # else spawn 2 new asteroids
        print("Oohh I'm a big boi")
        trajectory = random.uniform(20, 50)
        new_vector = self.velocity.rotate(trajectory)
        new_vector2 = self.velocity.rotate(-trajectory)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_vector

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2

