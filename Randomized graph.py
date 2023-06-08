import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set up the rectangles
rect1 = pygame.Rect(100, 100, 50, 50)
rect1_speed_x = 2
rect1_speed_y = 1

rect2 = pygame.Rect(200, 200, 50, 50)
rect2_speed_x = -1
rect2_speed_y = -2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the rectangles
    rect1.x += rect1_speed_x
    rect1.y += rect1_speed_y

    rect2.x += rect2_speed_x
    rect2.y += rect2_speed_y

    # Check for collision between rect1 and rect2
    if rect1.colliderect(rect2):
        # Respawn rect1 at a new random position
        rect1.x = random.randint(0, window_width - rect1.width)
        rect1.y = random.randint(0, window_height - rect1.height)

        # Respawn rect2 at a new random position
        rect2.x = random.randint(0, window_width - rect2.width)
        rect2.y = random.randint(0, window_height - rect2.height)

    # Check if rectangles hit the window edges and reverse their direction
    if rect1.left < 0 or rect1.right > window_width:
        rect1_speed_x *= -1
    if rect1.top < 0 or rect1.bottom > window_height:
        rect1_speed_y *= -1

    if rect2.left < 0 or rect2.right > window_width:
        rect2_speed_x *= -1
    if rect2.top < 0 or rect2.bottom > window_height:
        rect2_speed_y *= -1

    # Clear the screen
    window.fill((0, 0, 0))  # Fill with black color (RGB: 0, 0, 0)

    # Draw the rectangles
    pygame.draw.rect(window, (255, 0, 0), rect1)  # Red color for rect1
    pygame.draw.rect(window, (0, 255, 0), rect2)  # Green color for rect2

    pygame.display.update()

# Quit Pygame
pygame.quit()
