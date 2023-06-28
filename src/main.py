import pygame, sys
from random import choice, randint

from settings import *
from player import Player
from car import Car
from sprite import SimpleSprite, LongSprite

# Class for managing all sprites in the game.
class AllSprites(pygame.sprite.Group):
  def __init__(self):
    super().__init__()  # Call the parent (Group) constructor.
    # Initialize the scrolling offset and load the background and overlay images.
    self.offset = pygame.math.Vector2()
    self.bg = pygame.image.load('./resources/graphics/main/map.png').convert()
    self.fg = pygame.image.load('./resources/graphics/main/overlay.png').convert_alpha()

  def customize_draw(self, display_surface, player):
    # Update the scrolling offset based on the player's position.
    self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
    self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

    # Draw the background and all sprites onto the screen with the scrolling offset.
    display_surface.blit(self.bg, -self.offset)

    # Sort the sprites by their vertical position and draw them one by one.
    for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
      offset_pos = sprite.rect.topleft - self.offset
      display_surface.blit(sprite.image, offset_pos)

    # Draw the overlay on top of everything else.
    display_surface.blit(self.fg, -self.offset)


class Game:
  def __init__(self):
    pygame.init()
    self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Frogger')
    self.clock = pygame.time.Clock()

    # Initialize sprite groups.
    self.all_sprites = AllSprites()
    self.obstacle_sprites = pygame.sprite.Group()
    self.car_sprites = pygame.sprite.Group()

    # Initialize the player.
    self.player = Player((2062, 3274), self.all_sprites, self.obstacle_sprites)

    # Set a timer event to create new cars.
    self.car_timer = pygame.event.custom_type()
    pygame.time.set_timer(self.car_timer, 100)
    self.pos_list = []

    # Load the font and create the victory text surface and rectangle.
    self.font = pygame.font.Font(None, 50)
    self.text_surf = self.font.render('You Won!', True, 'White')
    self.text_rect = self.text_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    # Load and play the background music.
    self.music = pygame.mixer.Sound('./resources/audio/music.mp3')
    self.music.play(loops = -1)

    # Create the simple and long objects using the positions defined in the settings.
    for file_name, pos_list in SIMPLE_OBJECTS.items():
      path = f'./resources/graphics/objects/simple/{file_name}.png'
      surf = pygame.image.load(path).convert_alpha()
      for pos in pos_list:
        SimpleSprite(surf, pos, [self.all_sprites, self.obstacle_sprites])

    for file_name, pos_list in LONG_OBJECTS.items():
      surf = pygame.image.load(f'./resources/graphics/objects/long/{file_name}.png').convert_alpha()
      for pos in pos_list:
        LongSprite(surf, pos, [self.all_sprites, self.obstacle_sprites])

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

        if event.type == self.car_timer:
          random_pos = choice(CAR_START_POSITIONS)
          if random_pos not in self.pos_list:
            self.pos_list.append(random_pos)
            pos = (random_pos[0], random_pos[1] + randint(-8, 8))
            Car(pos, [self.all_sprites, self.obstacle_sprites])
          if len(self.pos_list) > 5:
            del self.pos_list[0]

      # Calculate the time elapsed since the last frame.
      dt = self.clock.tick() / 1000

      # Clear the display.
      self.display_surface.fill('black')

      # If the player has not reached the top yet, update and draw all sprites.
      if self.player.pos.y > 1180:
        self.all_sprites.update(dt)
        self.all_sprites.customize_draw(self.display_surface, self.player)
      else:
        # If the player has reached the top, fill the screen with a solid color and draw the victory text.
        self.display_surface.fill('teal')
        self.display_surface.blit(self.text_surf, self.text_rect)

      # Update the display.
      pygame.display.update()

if __name__ == '__main__':
  game = Game()
  game.run()
