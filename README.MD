# Frogger

This project is a clone of the classic arcade game Frogger, implemented in Python using the Pygame library. The goal is to guide a frog character through a busy road full of hazards to reach the safety of its home.

# Special Thanks

This project was inspired by the original Frogger game, developed by Konami in 1981.

# Project Structure

The project has the following file and folder structure:

## src
### This folder contains the source code files for the game:

* `main.py`: The main entry point of the game. It controls the game loop, handles events, and manages the rendering and updating of game objects.
* `player.py`: This file contains the Player class that represents the frog character the player controls. It handles the player's movement, collision detection and game progression.
* `car.py`: This file contains the Car class, representing the vehicles the player needs to avoid.
* `sprite.py`: Contains the SimpleSprite and LongSprite classes, representing various obstacles or platforms the player interacts with.
* `settings.py`: This file defines the game's settings and constants.

## Classes

* `src/main.py`: This file is the main entry point of the game and contains the Game class.
* `Game`: This class controls the game loop, handles events, and manages the rendering and updating of game objects. It also loads the game assets like images and sounds.

* `src/player.py`: This file contains the Player class.
* `Player`: This class represents the frog character the player controls. It handles the player's movement, collision detection and game progression.

* `src/car.py`: This file contains the Car class.
* `Car`: This class represents the vehicles the player needs to avoid.

* `src/sprite.py`: This file contains the SimpleSprite and LongSprite classes.
* `SimpleSprite` and `LongSprite`: These classes represent various obstacles or platforms the player interacts with.

* `src/settings.py`: While this file does not contain any classes, it defines the game's settings and constants which are used by the other classes. For example, it includes settings like the screen resolution, frame rate, scrolling speed, and various player and car parameters.

## resources
This folder contains various resources used in the game:

* `audio`: Contains the background music file `music.mp3`.
* `data`: Contains various data files including `buildings.tsx`, `extraction.py`, `floor.tsx`, `map.tmx`, `Objects.tsx` used for generating the game maps.
* `graphics`: Contains various image assets used in the game:
  * `cars`: Contains images for the different cars (`green.png`, `red.png`, `yellow.png`).
  * `main`: Contains images for the main game components (`map.png`, `overlay.png`).
  * `objects`: Contains images for different objects in the game.
    * `long`: Contains images for long objects.
    * `simple`: Contains images for simple objects.
  * `player`: Contains animation frames for the player character.
  * `tilesets`: Contains tileset images (`buildings.png`, `floor.png`).

# Instructions
To run the project, follow these steps:

1. Install Python 3 if you haven't already.
2. Install the Pygame library by running the command: `pip install pygame`.
3. Navigate to the project's src directory.
4. Run the command: `python3 src/main.py`.

Make sure you have the required resources (images, sounds, etc.) in the appropriate directories as shown in the folder structure.

Feel free to modify and explore the game to suit your needs.

Enjoy playing!
