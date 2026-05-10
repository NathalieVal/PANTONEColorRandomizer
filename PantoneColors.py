"""DAILY GAME PLAN:
    MAY 2nd: 
    Initialize pygame window
    Potentially figure out custom window sizing if it doesn't take too long just between fullscreen & windowed (https://www.youtube.com/watch?v=edJZOQwrMKw)
    BASIC windows & menus. Get buttons working.

    MAY 3RD:
    Figur out color randomizer system ( I have an idea in my head w/ a CSV file)"""

import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() # Initiates program
pygame.display.set_caption("Color Randomizer")

screen  = pygame.display.set_mode((1920, 1080)) # Initiates window

# Game Variables
game_menu = False

# Font(s)
font = pygame.font.SysFont("arialblack", 40)

# Font color(s)
text_col = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Load Button Images
play_img = pygame.image.load('Buttons/Play.png').convert_alpha()
about_img = pygame.image.load('Buttons/About.png').convert_alpha()
exit_img = pygame.image.load('Buttons/Exit.png').convert_alpha()

# Button Class
class Button():
    def __init__(self, x , y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        # Draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Create Button Instances
play_button = Button(100, 200, play_img)
about_button = Button(100, 400, about_img)
exit_button = Button(100, 600, exit_img)


# Game Loop
run = True
while run:

    screen.fill((0, 0, 0))

    play_button.draw()
    about_button.draw()
    exit_button.draw()


    # Check if menu button has been pressed
    if game_menu == True:
        pass
        # Display menu
    else: 
        draw_text("Press ESC to return to menu", font, text_col, 160, 250)

    # Event Handler
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            run = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_menu = True
                print("Game Menu")

    pygame.display.update()
    clock.tick(60)