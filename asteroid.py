import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.collid = False

    def draw(self, screen):
        if self.collid:
            pygame.draw.circle(screen, "red", self.position, self.radius, 2)
        else:
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            asteroid1 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
            asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroid2 = Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
            asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2

    