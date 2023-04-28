import numpy as np
import pygame

class WallGenerator:
    def __init__(self, world_size):
        self.world_size = world_size

    def generate_walls(self, num_walls):
        walls = []

        # Add top and bottom walls
        for i in range(num_walls // 2):
            x = np.random.randint(0, self.world_size - 100)
            y_top = np.random.randint(0, self.world_size // 2 - 50)
            y_bottom = np.random.randint(self.world_size // 2 + 50, self.world_size - 50)
            wall_top = pygame.Rect(x, y_top, 100, 10)
            wall_bottom = pygame.Rect(x, y_bottom, 100, 10)
            walls.extend([wall_top, wall_bottom])

        # Add left and right walls
        for i in range(num_walls // 2):
            x_left = np.random.randint(0, self.world_size // 2 - 50)
            x_right = np.random.randint(self.world_size // 2 + 50, self.world_size - 50)
            y = np.random.randint(0, self.world_size - 100)
            wall_left = pygame.Rect(x_left, y, 10, 100)
            wall_right = pygame.Rect(x_right, y, 10, 100)
            walls.extend([wall_left, wall_right])

        # Add random corner walls
        num_corner_walls = 4
        for i in range(num_corner_walls):
            x = np.random.randint(100, self.world_size - 100)
            y = np.random.randint(100, self.world_size - 100)
            if np.random.rand() < 0.5:  # top or bottom corner wall
                if np.random.rand() < 0.5:  # top corner wall
                    walls.append(pygame.Rect(x - 50, y - 10, 100, 10))
                    walls.append(pygame.Rect(x - 50, y, 10, 100))
                else:  # bottom corner wall
                    walls.append(pygame.Rect(x - 50, y, 100, 10))
                    walls.append(pygame.Rect(x + 40, y, 10, 100))
            else:  # left or right corner wall
                if np.random.rand() < 0.5:  # left corner wall
                    walls.append(pygame.Rect(x - 10, y - 50, 10, 100))
                    walls.append(pygame.Rect(x, y - 50, 100, 10))
                else:  # right corner wall
                    walls.append(pygame.Rect(x, y - 50, 10, 100))
                    walls.append(pygame.Rect(x, y + 40, 100, 10))

        return walls
