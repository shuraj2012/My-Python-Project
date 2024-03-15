import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Dinosaur Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
dinosaur_img = pygame.image.load("\\Users\\Fleek\\Downloads\\New folder\\din.png")
dinosaur_width, dinosaur_height = 50, 50
dinosaur_img = pygame.transform.scale(dinosaur_img, (dinosaur_width, dinosaur_height))

# Define constants for the game
dinosaur_x = 50
dinosaur_y = screen_height - dinosaur_height - 50
dinosaur_jump = False
jump_count = 10
dinosaur_speed = 5

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dinosaur_jump:
                    dinosaur_jump = True

    # Move dinosaur
    if dinosaur_jump:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dinosaur_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            dinosaur_jump = False
            jump_count = 10
    else:
        if dinosaur_y < screen_height - dinosaur_height - 50:
            dinosaur_y += dinosaur_speed

    # Draw dinosaur
    screen.blit(dinosaur_img, (dinosaur_x, dinosaur_y))

    # Generate obstacles
    if random.randint(1, obstacle_frequency) == 1:
        obstacles.append(generate_obstacle())

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.x -= dinosaur_speed
        draw_obstacles(obstacles)

        # Collision detection
        if obstacle.colliderect((dinosaur_x, dinosaur_y, dinosaur_width, dinosaur_height)):
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
