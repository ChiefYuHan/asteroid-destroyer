from circleshape import CircleShape
import pygame

from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=self.radius,
        )

    def update(self, dt):
        self.position += self.velocity * dt