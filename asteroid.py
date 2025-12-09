import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.is_alive = True
    self.velocity = pygame.Vector2(0, 0)
  
  def draw(self, screen):
      pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
  
  def update(self, dt):
      self.position += self.velocity * dt

  def kill(self):
     if self.is_alive:
        self.is_alive = False
        super().kill()
        print(f"Asteroid at {self.position} has been destroyed!")

  def split(self):
      self.kill()

      if self.radius <= ASTEROID_MIN_RADIUS:
         return
      
      log_event("asteroid_split")

      angle = random.uniform(20, 50)

      new_velocity_1 = self.velocity.rotate(angle)
      new_velocity_2 = self.velocity.rotate(-angle)

      new_radius = self.radius - ASTEROID_MIN_RADIUS

      new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
      new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

      new_asteroid_1.velocity = new_velocity_1 * 1.2
      new_asteroid_2.velocity = new_velocity_2 * 1.2


      return new_asteroid_1, new_asteroid_2
