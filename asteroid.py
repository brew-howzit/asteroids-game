import pygame
import constants
from circleshape import CircleShape # Specific import

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