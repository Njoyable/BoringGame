import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SQUARE_SIZE = 50
CIRCLE_RADIUS = 20
SQUARE_COLOR = (255, 0, 0)
CIRCLE_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square")

# Initial square position
x, y = WIDTH // 2 - SQUARE_SIZE // 2, HEIGHT // 2 - SQUARE_SIZE // 2

# Initial movement direction
dx, dy = 0, 0

# List to store the circles
circles = []

# Counter for collected circles
collected = 0

# Create a font for the counter
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -0.5
            elif event.key == pygame.K_RIGHT:
                dx = 0.5
            elif event.key == pygame.K_UP:
                dy = -0.5
            elif event.key == pygame.K_DOWN:
                dy = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0

    # Update square position
    x += dx
    y += dy

    # Bound checking to keep the square within the screen
    x = max(0, min(x, WIDTH - SQUARE_SIZE))
    y = max(0, min(y, HEIGHT - SQUARE_SIZE))

    # Randomly add circles to the list
    if random.randint(1, 100) == 1:
        circle_x = random.randint(0, WIDTH - CIRCLE_RADIUS * 2)
        circle_y = random.randint(0, HEIGHT - CIRCLE_RADIUS * 2)
        circles.append((circle_x, circle_y))

    # Check for collision with circles
    for circle in circles:
        circle_x, circle_y = circle
        if x < circle_x + CIRCLE_RADIUS and x + SQUARE_SIZE > circle_x and y < circle_y + CIRCLE_RADIUS and y + SQUARE_SIZE > circle_y:
            circles.remove(circle)
            collected += 1

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the circles
    for circle in circles:
        pygame.draw.circle(screen, CIRCLE_COLOR, circle, CIRCLE_RADIUS)

    # Draw the square
    pygame.draw.rect(screen, SQUARE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Display the collected count
    text = font.render(f"Collected: {collected}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
