import pygame
import circleshape
import constants
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        new_asteroids_spawn_angle = random.uniform(20, 50)
        new_asteroid_velocity_1 = self.velocity.rotate(new_asteroids_spawn_angle)
        new_asteroid_velocity_2 = self.velocity.rotate(-new_asteroids_spawn_angle)
        new_asteroids_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        asteroid1.velocity = new_asteroid_velocity_1 * 1.2
        asteroid2.velocity = new_asteroid_velocity_2 * 1.2