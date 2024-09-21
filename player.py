import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 200
        self.rotation = 0

    def move(self, dt):
        # self.position += self.velocity * self.speed * dt
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # def update(self, dt):
    #     self.position += self.velocity * self.speed * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)


    def draw(self, screen):
        # pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)
        # self.triangle()
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
