import pygame
import random

from pygame import image

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bike Racing Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load images
bike_img = pygame.image.load("C:\\Users\\Fleek\\Downloads\\New folder\\bike.png")
bike_img = pygame.transform.scale(bike_img, (50, 100))
obstacle_img = pygame.Surface((50, 50))
obstacle_img.fill(RED)

# Game variables
bike_width = 50
bike_height = 100
bike_x = (screen_width - bike_width) // 2
bike_y = screen_height - bike_height - 20
bike_speed = 5
obstacle_speed = 7
obstacle_width = 50
obstacle_height = 50
obstacle_frequency = 25
obstacles = []

clock = pygame.time.Clock()
score = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bike_x > 0:
        bike_x -= bike_speed
    if keys[pygame.K_RIGHT] and bike_x < screen_width - bike_width:
        bike_x += bike_speed

    # Spawn obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randrange(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

    # Move obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        screen.blit(obstacle_img, (obstacle[0], obstacle[1]))

        # Collision detection
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)
            score += 1

    # Draw bike
    screen.blit(bike_img, (bike_x, bike_y))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
