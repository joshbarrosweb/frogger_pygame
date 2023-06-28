import pygame

# This is a class for simple sprites
class SimpleSprite(pygame.sprite.Sprite):
  def __init__(self, surf, pos, groups):
    # Call the parent class (Sprite) constructor
    super().__init__(groups)
    # The image/surface of the sprite
    self.image = surf
    # The rectangular area of the sprite
    self.rect = self.image.get_rect(topleft = pos)
    # The hitbox of the sprite - a smaller rectangle for more precise collisions
    self.hitbox = self.rect.inflate(0, -self.rect.height / 2)

# This is a class for longer sprites
class LongSprite(pygame.sprite.Sprite):
  def __init__(self, surf, pos, groups):
    # Call the parent class (Sprite) constructor
    super().__init__(groups)
    # The image/surface of the sprite
    self.image = surf
    # The rectangular area of the sprite
    self.rect = self.image.get_rect(topleft = pos)
    # The hitbox of the sprite - a smaller rectangle for more precise collisions
    self.hitbox = self.rect.inflate(-self.rect.width * 0.8, -self.rect.height / 2)
    # Adjust the bottom of the hitbox
    self.hitbox.bottom = self.rect.bottom - 10
