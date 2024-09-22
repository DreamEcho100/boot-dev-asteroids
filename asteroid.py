import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        velocity_1 = self.velocity.copy().rotate(random_angle) * 1.2
        velocity_2 = velocity_1.copy() * -1

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2

        # a = Asteroid(self.position.x, self.position.y, self.radius / 2)
        # a.velocity = self.velocity.copy().rotate(random_angle)

        # b = Asteroid(self.position.x, self.position.y, self.radius / 2)
        # b.velocity = self.velocity.copy().rotate(-random_angle)
