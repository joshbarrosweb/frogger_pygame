import pygame
import os
from random import choice

# Car class, which inherits from the Sprite class in Pygame.
class Car(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)  # Call the parent (Sprite) constructor.
    self.name = 'car'

    # Initialize position, direction, and speed attributes for the car.
    self.pos = pos
    self.direction = pygame.math.Vector2(0, 0)
    self.speed = 300

    car_name = None

    # Randomly select an image file for the car from the specified directory.
    for _, _, img_list in os.walk('./resources/graphics/cars'):
      car_name = choice(img_list)

    if car_name != None:
      # Load the chosen image file and set it as the sprite image.
      self.image = pygame.image.load('./resources/graphics/cars/' + car_name).convert_alpha()
      # Create a rectangle for the image (useful for collision detection) and set its center to the given position.
      self.rect = self.image.get_rect(center = pos)

      # Initialize the position as a 2D vector (useful for movement).
      self.pos = pygame.math.Vector2(self.rect.center)

      # Set the direction of the car based on its initial position.
      if pos[0] < 200:
        self.direction = pygame.math.Vector2(1, 0)  # Move to the right.
      else:
        self.direction = pygame.math.Vector2(-1, 0)  # Move to the left.
        # Flip the car image horizontally if it's moving to the left.
        self.image = pygame.transform.flip(self.image, True, False)

      # Create a hitbox for the car for collision detection.
      self.hitbox = self.rect.inflate(0, -self.rect.height / 2)

  def update(self, dt):
    # Update the car's position based on its speed, direction, and the time elapsed since the last update.
    self.pos += self.direction * self.speed * dt
    # Update the hitbox and rectangle's center to the current position.
    self.hitbox.center = (round(self.pos.x), round(self.pos.y))
    self.rect.center = self.hitbox.center

    # Kill (remove) the car if it's no longer visible on the screen.
    if not -200 < self.rect.x < 3400:
      self.kill()
