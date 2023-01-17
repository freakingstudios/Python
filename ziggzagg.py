import pygame

# Initialize pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Zigzag Animation")

# Set the initial position of the zigzag
x1, y1 = 0, 250
x2, y2 = 50, 300

# Run the animation loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the zigzag
    pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2))

    # Update the position of the zigzag
    x1 += 5
    y1 -= 5
    x2 += 5
    y2 += 5

    # Update the display
    pygame.display.flip()

    # Wait for a short time
    pygame.time.wait(50)

# Exit pygame
pygame.quit()
