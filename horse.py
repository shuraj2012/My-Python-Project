import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Running Horse Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
horse_img = pygame.image.load("\\Users\\Fleek\\Downloads\\New folder\\horse.png")
horse_width, horse_height = 100, 100
horse_img = pygame.transform.scale(horse_img, (horse_width, horse_height))

# Define constants for the game
horse_x = 50
horse_y = screen_height - horse_height - 50
horse_speed = 1

# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

# Function to generate random obstacles
def generate_obstacle():
    obstacle_width = random.randint(20, 50)
    obstacle_height = random.randint(20, 50)
    obstacle_x = screen_width
    obstacle_y = screen_height - obstacle_height - 50
    return pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

# Game variables
obstacles = []
obstacle_frequency = 50
score = 0

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move horse
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        horse_y -= horse_speed * 2
    else:
        horse_y += horse_speed

    # Draw horse
    screen.blit(horse_img, (horse_x, horse_y))

    # Generate obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacles.append(generate_obstacle())

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.x -= horse_speed
        draw_obstacles(obstacles)

        # Collision detection
        if obstacle.colliderect((horse_x, horse_y, horse_width, horse_height)):
            running = False

        if obstacle.x + obstacle.width < 0:
            obstacles.remove(obstacle)
            score += 1

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
