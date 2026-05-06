import pygame
import constants
from circleshape import CircleShape
from logger import log_event
import random # Specific import

class Asteroid(CircleShape): # Capitalized class name
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            self.position, 
            self.radius, 
            constants.LINE_WIDTH
        )

    def update(self, dt):
    # This is what actually moves the rock across the screen
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        a = self.velocity.rotate(new_angle)
        b = self.velocity.rotate(-new_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = a * 1.2
        new_asteroid_2 = Asteroid(self.position.x,self.position.y, new_radius)
        new_asteroid_2.velocity = b * 1.2

        