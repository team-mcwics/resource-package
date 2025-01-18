########## IMPORTS AND INITIALIZATION ##########
import pygame   # import the pygame module
import random   # import the random module

pygame.init()   # Initialize Pygame

###############################################

########## CONSTANTS ##########
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600      #screen dimension: width x height (in pixels)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 67   # dimensions for pics
ASTEROID_WIDTH, ASTEROID_HEIGHT = 50, 50
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
QUIT_WIDTH, QUIT_HEIGHT = 100, 87
FPS = 60                                    # set FPS to 60

WHITE = (255, 255, 255)     #Initialize colors to be used
RED = (255, 0, 0)

##############################

########## SCREEN/GAME WINDOW ##########
#initialize screen with dimensions from before
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Protector")       # set window title

########################################

########## LOADING IMAGES & SCALING ##########
# Load images and save in variables
#use convert_alpha to preserve the transparency in your png
earth_image = pygame.image.load('background.png').convert()
spaceship_image = pygame.image.load('spaceship.png').convert_alpha()
asteroid_image = pygame.image.load('asteroid.png').convert_alpha()
quit_image = pygame.image.load('quitBtn.png').convert_alpha()

#scale
quit_image = pygame.transform.scale(quit_image, (QUIT_WIDTH, QUIT_HEIGHT))

###############################################




########## SPRITES ##########
class Spaceship(pygame.sprite.Sprite):
    def __init__(self): #define constructor
        super().__init__() #inherit from pygame sprite class

        #scale spaceship image
        self.image = pygame.transform.scale(spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

        #contain sprite in a rectangle to represent position
        #initial position: middle bottom of screen
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 20))
        #set speed to 5 pixels per frame
        self.speed = 5

    def update(self):   #define how the sprite updates in each frame

        keys = pygame.key.get_pressed() #retrieve keys currently pressed

        #if left key and position is not past left boundary
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            #decrement position (go left)
            self.rect.x -= self.speed
        # if left key and position is not past left boundary
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            # increment position (go right)
            self.rect.x += self.speed
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(asteroid_image, (ASTEROID_WIDTH, ASTEROID_HEIGHT))

        #randomly generate initial x coord of asteroid
        self.rect = self.image.get_rect(topleft=(random.randint(0, SCREEN_WIDTH-ASTEROID_WIDTH), -ASTEROID_HEIGHT))
        # randomly generate asteroid speed
        self.speed = random.randint(1, 3)
    def update(self):
        #increment y coord by speed at each frame
        self.rect.y += self.speed
        #if asteroid moves of the screen, remove from game 
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):   #x,y represent the initial coords
        super().__init__()
        #create a new surface
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(RED)
        #create a rectangle to represent the bullet's position
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def update(self): #updates that occur per frame
        # change bullet y-coord (upwards) by speed
        self.rect.y += self.speed
        #if the bullet passes the top boundary remove from game
        if self.rect.bottom < 0:
            self.kill()




########## MAIN FUNCTION ##########
def main():
    ########## GROUPS ##########
    spaceship = Spaceship() #create instance of spaceship class

    #create sprite groups to manage and update all sprites at the same time
    all_sprites = pygame.sprite.Group(spaceship)
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    ########## INITIALIZATION PT. 2 ##########
    score = 0 #initialize score
    font = pygame.font.Font(None, 36)  # Set up font for rendering score

    running = True
    clock = pygame.time.Clock() #create clock object to control frame rate

    ########## GAME LOOP ##########
    while running:  #initiate game loop

        clock.tick(FPS)   #set how fast the game updates

        for event in pygame.event.get():    #iterate over events that happened since the last frame

            if event.type == pygame.QUIT:   #if quit event, exit game loop
                running = False

            if event.type == pygame.KEYDOWN:    #if key was pressed
                if event.key == pygame.K_SPACE:     #if key was a space

                    #create new instance of Bullet class
                    #set inital coords to x,y-coords of spaceship pos
                    bullet = Bullet(spaceship.rect.centerx, spaceship.rect.top)

                    #add to sprite groups
                    bullets.add(bullet)
                    all_sprites.add(bullet)

            # Check for mouse clicks
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            # Check if the mouse is within the boundaries of the quit button
            if 720 <= mouse_x <= 790 and 10 <= mouse_y <= 60 and mouse_click[0]:
                running = False  #set flag to false and exit game loop

        # Update
        all_sprites.update()    #call the update method for all sprites in the group
        asteroids.update()
        # Spawn asteroids
        if random.randint(1, 30) == 1:  #randomly decide to spawn asteroids (1 in 30 chance)
            asteroid = Asteroid()
            asteroids.add(asteroid)
            all_sprites.add(asteroid)
        # Check for collisions
        for bullet in bullets:  #iterate through all bullets on screen
            #check if a bullet collided with any asteroid on the screen
            #return list of collided asteroids, and removes them from asteroid group
            hit_asteroids = pygame.sprite.spritecollide(bullet, asteroids, True)
            #iterate through asteroids in collision list (incase bullet hit multiple)
            for hit in hit_asteroids:
                #explosion_sound.play()
                bullet.kill()
                score += 1  # Increase score when an asteroid is hit


        ########## DRAW AND RENDER ##########
        screen.blit(earth_image, (0, 0))    #draw background on screen
        screen.blit(quit_image, (700, -3))
        all_sprites.draw(screen)    #draw all sprites in the group

        # Render the score on the screen
        score_text = font.render(f'SCORE: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()       #display changes from draw,bilt and all logic ^^

    ########## QUIT ##########
    pygame.quit()      #quit pygame when loop exits

if __name__ == "__main__":
    main()
