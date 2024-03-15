import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flying Balloon")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Balloon parameters
balloon_radius = 50
balloon_pos = [screen_width // 2, screen_height // 2]
balloon_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control balloon movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        balloon_pos[0] -= balloon_speed
    if keys[pygame.K_RIGHT]:
        balloon_pos[0] += balloon_speed
    if keys[pygame.K_UP]:
        balloon_pos[1] -= balloon_speed
    if keys[pygame.K_DOWN]:
        balloon_pos[1] += balloon_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the balloon
    pygame.draw.circle(screen, BLUE, balloon_pos, balloon_radius)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
