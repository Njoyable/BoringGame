import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SQUARE_SIZE = 50
SQUARE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square")

# Initial square position
x, y = WIDTH // 2 - SQUARE_SIZE // 2, HEIGHT // 2 - SQUARE_SIZE // 2

# Initial movement direction
dx, dy = 0, 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0

    # Update square position
    x += dx
    y += dy

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the square
    pygame.draw.rect(screen, SQUARE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
