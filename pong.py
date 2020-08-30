# Simple pygame program

# Import and initialize the pygame library
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

WALL_THICKNESS = 10
PADDLE_WIDTH = 100
PADDLE_SPEED = 0.5
PLAY_AREA_TOP = 40

WALL_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

walls = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height, left, top):
       pygame.sprite.Sprite.__init__(self, walls)

       self.image = pygame.Surface([width, height])
       self.image.fill(WALL_COLOR)

       self.rect = self.image.get_rect()
       self.rect.x = left
       self.rect.y = top


def display_lives (screen, lives):
    font = pygame.font.Font(None, 36)
    text = font.render(f'Lives: {lives}', 1, TEXT_COLOR)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.y = 10
    screen.blit(text, textpos)


pygame.init()


lives = 10
top_wall = Wall(SCREEN_WIDTH, WALL_THICKNESS, 0, PLAY_AREA_TOP)
left_wall = Wall(WALL_THICKNESS, SCREEN_HEIGHT - PLAY_AREA_TOP, 0, PLAY_AREA_TOP)
right_wall = Wall(WALL_THICKNESS, SCREEN_HEIGHT - PLAY_AREA_TOP, SCREEN_WIDTH - WALL_THICKNESS, PLAY_AREA_TOP)
paddle = Wall(PADDLE_WIDTH, WALL_THICKNESS, (SCREEN_WIDTH / 2) - (PADDLE_WIDTH / 2), SCREEN_HEIGHT - WALL_THICKNESS - 10)

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
running = True

clock = pygame.time.Clock()

while running:

    dt = clock.tick()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        paddle.rect.x += PADDLE_SPEED * dt
        print('Right')
    if keys[pygame.K_LEFT]:
        paddle.rect.x -= PADDLE_SPEED * dt
        print('Left')
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    walls.draw(background)
    display_lives(background, lives)

    screen.blit(background, (0, 0))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()