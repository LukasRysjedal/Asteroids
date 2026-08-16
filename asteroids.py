from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self):
        #Kills the original asteroid and checks if its large enough to split
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        #Create two new asteroids in a random angle in opposite directions
        random_angle = random.uniform(20, 50)
        asteroid1_new_angle_vector = self.velocity.rotate(random_angle)
        asteroid2_new_angle_vector = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        #Set the velocity for the new asteroids and scaling it with 1.2
        asteroid1.velocity = asteroid1_new_angle_vector * 1.2
        asteroid2.velocity = asteroid2_new_angle_vector * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)