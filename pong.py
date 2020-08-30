# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

WALL_THICKNESS = 10
PADDLE_WIDTH = 100
BALL_SIZE = 50
PADDLE_SPEED = 0.5
PLAY_AREA_TOP = 40

WALL_COLOR = (255, 255, 255)
BALL_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

walls = pygame.sprite.Group()
items = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height, left, top):
       pygame.sprite.Sprite.__init__(self, walls, items)

       self.image = pygame.Surface([width, height])
       self.image.fill(WALL_COLOR)

       self.rect = self.image.get_rect()
       self.rect.x = left
       self.rect.y = top

class Ball(pygame.sprite.Sprite):

    def __init__(self, size, left, top, x_speed, y_speed):
       pygame.sprite.Sprite.__init__(self, items)

       self.image = pygame.Surface([size, size])
       self.image.fill(BALL_COLOR)

       self.rect = self.image.get_rect()
       self.rect.x = left
       self.rect.y = top
       self.x_speed = x_speed
       self.y_speed = y_speed

    def move(self, dt):
        self.rect.x += self.x_speed * dt
        self.rect.y += self.y_speed * dt
        hits = pygame.sprite.spritecollide(self, walls, False)
        for hit in hits:
            if hit == left_wall and self.x_speed < 0:
                self.x_speed *= -1
                print(self.x_speed)
            if hit == right_wall and self.x_speed > 0:
                self.x_speed *= -1
                print(self.x_speed)
            if hit == top_wall  and self.y_speed < 0:
                self.y_speed *= -1
                print(self.y_speed)
            if hit == paddle and self.y_speed > 0:
                self.y_speed *= -1
                print(self.y_speed)


class Paddle(Wall):
    def move(self, left_down, right_down, dt):
        if right_down and self.rect.x + PADDLE_WIDTH < SCREEN_WIDTH - WALL_THICKNESS - 1:
            self.rect.x += PADDLE_SPEED * dt
            print(f'Right: {PADDLE_SPEED * dt}')
        if left_down and self.rect.x > WALL_THICKNESS + 1:
            self.rect.x -= PADDLE_SPEED * dt
            print(f'Left: {PADDLE_SPEED * dt}')
    

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
paddle = Paddle(PADDLE_WIDTH, WALL_THICKNESS, (SCREEN_WIDTH / 2) - (PADDLE_WIDTH / 2), SCREEN_HEIGHT - WALL_THICKNESS - 10)
ball = Ball(BALL_SIZE, (SCREEN_WIDTH / 2) - (BALL_SIZE / 2), (SCREEN_HEIGHT - PLAY_AREA_TOP) / 2, random.randint(-10, 10) / 100, random.randint(-10, 10) / 100)

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Run until the user asks to quit
running = True

clock = pygame.time.Clock()

while running:

    dt = clock.tick(60)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    paddle.move(keys[pygame.K_LEFT], keys[pygame.K_RIGHT], dt)
    ball.move(dt)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    items.draw(background)
    display_lives(background, lives)

    screen.blit(background, (0, 0))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()