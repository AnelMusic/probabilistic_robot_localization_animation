import numpy as np
import pygame

class Robot:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def sense(self, world):
        return np.sqrt((self.x - world.points[:, 0]) ** 2 + (self.y - world.points[:, 1]) ** 2)

    def move(self, world, walls):
        new_x = self.x + 5 * np.cos(self.orientation)
        new_y = self.y + 5 * np.sin(self.orientation)

        collision = False
        if not (0 <= new_x <= world.world_size and 0 <= new_y <= world.world_size):
            collision = True
        else:
            for wall in walls:
                if wall.collidepoint(new_x, new_y):
                    collision = True
                    break

        if collision:
            self.orientation = np.random.uniform(0, 2 * np.pi)
            return False
        else:
            self.x = new_x
            self.y = new_y
            return True

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 8)
