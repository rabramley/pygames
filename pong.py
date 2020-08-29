# Simple pygame program

# Import and initialize the pygame library
import pygame

def display_lives (screen, lives):
    font = pygame.font.Font(None, 36)
    text = font.render('Hello There', 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

lives = 10

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
running = True

BACKGROUND_COLOR = (0, 0, 0)

display_items = []

clock = pygame.time.Clock()

while running:

    dt = clock.tick()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    # Draw a solid blue circle in the center
    for i in display_items:
        i.draw(background)

    display_lives(background, lives)

    screen.blit(background, (0, 0))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()