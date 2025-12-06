from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
       super().__init__(x, y, SHOT_RADIUS) 

    def draw(self, screen):
        pygame.draw.circle(screen, color, center, radius, width)
        screen = self.screen
        color = self.color
        center = self.position
        radius = self.radius
        width = self.width
        # Use pygame.draw.circle
        pass
    
    def update(self, dt):
        # Move the shot based on its velocity
        # Similar to how asteroid moves
        return super().update(dt)