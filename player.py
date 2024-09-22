import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_IN_SECONDS, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.shoot_cool_down = 0

    def move(self, dt):
        # self.position += self.velocity * self.speed * dt
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # def update(self, dt):
    #     self.position += self.velocity * self.speed * dt
    def update(self, dt):
        if self.shoot_cool_down > 0:
            self.shoot_cool_down -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()


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

    def shoot(self):
        if self.shoot_cool_down > 0:
            return
        shoot = Shot(self.position.x, self.position.y)
        shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * 500
        self.shoot_cool_down = PLAYER_SHOOT_COOLDOWN_IN_SECONDS
