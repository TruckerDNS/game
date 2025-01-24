import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Video Game')

# Set up the player
player_size = 50
player_color = (0, 128, 255)
player_pos = [width // 2, height - 2 * player_size]

# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < width - player_size:
        player_pos[0] += 5

    window.fill((0, 0, 0))
    pygame.draw.rect(window, player_color, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.flip()

    clock.tick(30)