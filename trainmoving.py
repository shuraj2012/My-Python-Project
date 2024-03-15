import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Train")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Train parameters
train_width = 900
train_height = 50
train_x = 0
train_y = screen_height - train_height
train_speed = 20

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the train horizontally
    train_x += train_speed

    # If the train goes off the screen, reset its position
    if train_x > screen_width:
        train_x = -train_width

    # Clear the screen
    screen.fill(WHITE)

    # Draw the train
    pygame.draw.rect(screen, BLACK, (train_x, train_y, train_width, train_height))
    pygame.draw.circle(screen, RED, (train_x + 20, train_y + train_height), 10)
    pygame.draw.circle(screen, RED, (train_x + train_width - 20, train_y + train_height), 10)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
