# README: PyGame Basics and Space Protector Overview

## Introduction to PyGame
PyGame is a Python library designed for game development. It simplifies many tasks involved in creating games, including handling graphics, sound, and user input. Here are the key features of PyGame that you'll use while building games like Space Protector:

### Basics of PyGame
1. **Initialization:**
   - Start your game by initializing PyGame using `pygame.init()`.

2. **Game Window and Screen Setup:**
   - Create a game window using `pygame.display.set_mode()`.
   - Customize the screen dimensions and window title.

3. **Coordinate System:**
   - PyGame uses a Cartesian coordinate system where the origin (0, 0) is at the top-left corner of the screen.
   - The x-coordinate increases to the right, and the y-coordinate increases downward.

4. **Load Assets:** 
   - Load images and save in variables using `pygame.image.load`.

5. **Sprites and Sprite Groups:**
   - Use PyGame's `Sprite` class to represent objects like the player’s spaceship, bullets, and asteroids.
     - A Sprite is a dynamic object within a game environment that moves across the screen, interacts with other objects, and is typically under user control. It encapsulates various properties such as dimensions, color, behavior, and more, allowing for cleaner, more maintainable, and reusable code.
     - PyGame Sprites provide several built-in methods for managing game objects efficiently (check documentation). It makes tasks such as updating, rendering, and handling collisions much easier.
     - def update(self):updates sprite attributes, like position and velocity, during each game loop iteration.
   - Group sprites into `pygame.sprite.Group()` for efficient management, updating, and rendering. Groups serve as containers for managing multiple sprites at the same time throughout the game. 

6. **Game Loop:**
   - The game loop is where the game runs continuously. It processes user input, updates game state, and renders graphics.
   - Use `pygame.event.get()` to handle events like key presses or mouse clicks.
   - Regulate frame rates using `clock.tick(FPS)`.

7. **Drawing and Rendering:**
   - Use methods like `blit()` to draw images or `pygame.draw` for shapes and text.
   - Call `pygame.display.flip()` to update the screen.

8. **Shutdown:**
   - Properly quit the game using `pygame.quit()` to release resources.

---

## Space Protector: Game Overview

### What is Space Protector?
Space Protector is a 2D arcade-style game where players control a spaceship to shoot asteroids while avoiding collisions. The game incorporates core game development principles and demonstrates PyGame's features in action. The entire source code of this game can be found at [spaceProtector.py](SpaceProtector/spaceProtector.py).

### Key Features
- **Player Control:**
  - Move the spaceship horizontally using arrow keys.
  - Shoot bullets with the spacebar to destroy asteroids.
- **Asteroids:**
  - Asteroids spawn randomly at the top of the screen and move downward.
  - Colliding with an asteroid ends the game.
- **Score System:**
  - Earn points by destroying asteroids.
- **Quit Button:**
  - Click the quit button to exit the game.

### Game Components
1. **Spaceship Class:**
   - Represents the player’s spaceship.
   - Handles movement and positioning using the `update()` method.

2. **Asteroid Class:**
   - Represents asteroids that fall from the top of the screen.
   - Randomly spawns with varying speeds and positions.

3. **Bullet Class:**
   - Represents bullets fired by the spaceship.
   - Moves upward and removes asteroids upon collision.

4. **Sprite Groups:**
   - Groups for managing and rendering sprites (e.g., `all_sprites`, `asteroids`, `bullets`).

5. **Game Loop:**
   - Handles user input, updates game objects, checks collisions, and renders visuals.

6. **Score Tracking:**
   - Displays the player’s score on the screen using PyGame’s font rendering.

### How Everything Fits Together
The `spaceProtector.py` file is structured to demonstrate best practices in game development:
- **Initialization:**
  - The game begins with importing modules, loading assets, and setting up constants.
- **Sprites:**
  - The spaceship, asteroids, and bullets are defined as classes inheriting from `pygame.sprite.Sprite`.
  - Each sprite has its own behavior and interactions.
- **Game Loop:**
  - Updates the position of sprites and manages collisions.
  - Draws the updated state to the screen every frame.
- **Collision Detection:**
  - Uses `pygame.sprite.spritecollide()` to check for collisions between bullets and asteroids or the spaceship and asteroids.
- **Rendering:**
  - Draws the background, sprites, and score to the screen.

### Running the Game
To play Space Protector:
1. Ensure you have Python and PyGame installed (`pip install pygame`).
2. Run the `spaceProtector.py` file:
   ```bash
   python spaceProtector.py
   ```
3. Use the arrow keys to move and the spacebar to shoot.
4. Avoid asteroids and try to achieve the highest score!

---

## Resources
- [Pygame documentation](https://www.pygame.org/docs/)
- [Minimal code needed](https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html)
- [Geeksforgeeks Pygame tutorial](https://www.geeksforgeeks.org/pygame-tutorial/?ref=lbp)
- [Pygame wiki tutorials](https://www.pygame.org/wiki/tutorials)
- [Intro to sprites](http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en#section_13)
