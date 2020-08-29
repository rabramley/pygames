# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import math
pygame.init()

SPARK_SPREAD = 8

class Spark():
    def __init__(self):
        self._r = 255
        self._g = (random.random() * 20) + 100
        self._b = self._g
        self._x = 250
        self._y = 750.0
        self._size = 2
        self._ball_fade = 1 / 10
        self._age = 0

        speed = ((random.random() * 3) + 8) / 15
        angle = ((random.random() * 10) - 95) / 360.0 * math.tau

        self._y_speed = speed * math.sin(angle)
        self._x_speed = speed * math.cos(angle)

        if random.randint(0, 100) > 95:
            self._explode_age = (random.random() * 50) + 1200
        else:
            self._explode_age = 100000000000000
    
    def get_color(self):
        return (self._r, self._g, self._b)

    def fade(self, time):
        self._r = max(self._r - self._ball_fade * time, 0)
        self._g = max(self._g - self._ball_fade * time, 0)
        self._b = max(self._b - self._ball_fade * time, 0)
    
    def is_dead(self):
        return self._r + self._g + self._b == 0

    def move(self, gravity, time):
        self._age += 1
        self.fade(time)
        self._y += self._y_speed * time
        self._x += self._x_speed * time
        self._y_speed -= gravity * time

    def draw(self, screen):
        pygame.draw.circle(screen, self.get_color(), (int(self._x), int(self._y)), self._size)

    def explodes(self, time):
        self._age += time
        if self._age > self._explode_age:
            return [Fragment(self._x, self._y) for _ in range(100)]

class Fragment(Spark):
    def __init__(self, x, y):
        self._r = random.randint(150, 200)
        self._g = self._r
        self._b = 255
        self._x = x
        self._y = y
        self._size = 1
        self._ball_fade = 1 / 3
        self._age = 0

        speed = (random.random() * 30) / 100
        angle = random.random() * math.tau

        self._y_speed = speed * math.sin(angle)
        self._x_speed = speed * math.cos(angle)
    
    def explodes(self, time):
        return None


# Set up the drawing window
screen = pygame.display.set_mode([500, 800])

# Run until the user asks to quit
running = True

BACKGROUND_COLOR = (0, 0, 0)
GRAVITY = -0.0005

sparks = []

spawn_dt = 0
spawn_limit = 10
time = 0

clock = pygame.time.Clock()

while running:

    dt = clock.tick()

    time += dt

    # convert the delta to seconds (for easier calculation)

    spawn_dt += dt
    if spawn_dt > spawn_limit:
        sparks.extend([Spark() for _ in range(spawn_dt // spawn_limit)])
        spawn_dt = int(spawn_limit * random.random() / 2)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    # Fill the background with white
    screen.fill(BACKGROUND_COLOR)

    # Draw a solid blue circle in the center
    for s in sparks:
        if s.is_dead():
            sparks.remove(s)
        
        fragments = s.explodes(dt)

        if fragments is not None:
            sparks.extend(fragments)
            sparks.remove(s)

        s.move(GRAVITY, dt)
        s.draw(background)

    screen.blit(background, (0, 0))
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()