from circleshape import CircleShape
from constants import *
import pygame

# Create a new Shot class to represent a bullet. It should also inherit from CircleShape so that it can use our collision detection code. If you need inspiration, it should look very similar to our Asteroid class. Use a new SHOT_RADIUS constant and set it to 5.
class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # self.velocity = pygame.Vector2(0, 1).rotate(pygame.Vector2(x, y)) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
