import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tile Array Example")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define tile class
class Tile:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = black

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Create a 2D array of tiles
tile_size = 50
num_rows = height // tile_size
num_cols = width // tile_size

tile_array = [[Tile(x * tile_size, y * tile_size, tile_size) for x in range(num_cols)] for y in range(num_rows)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw tiles
    for row in tile_array:
        for tile in row:
            tile.draw()

    pygame.display.flip()
