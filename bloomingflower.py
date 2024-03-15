import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blooming Flower")

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Define constants for the flower
CENTER_X = screen_width // 2
CENTER_Y = screen_height // 2
PETAL_RADIUS = 150
NUM_PETALS = 12

# Game loop
running = True
angle = 0
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw petals
    for i in range(NUM_PETALS):
        angle_radians = math.radians(angle + i * (360 / NUM_PETALS))
        x = CENTER_X + PETAL_RADIUS * math.cos(angle_radians)
        y = CENTER_Y + PETAL_RADIUS * math.sin(angle_radians)
        pygame.draw.circle(screen, YELLOW, (int(x), int(y)), 20)

    # Increment angle to rotate the petals
    angle += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
