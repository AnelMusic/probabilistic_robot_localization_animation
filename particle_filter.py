import numpy as np
import pygame
import time
from robot import Robot
from world import World
from wall_generator import WallGenerator

# Initialize the world and the robot
world_size = 1000
world = World(world_size)
robot = Robot(world_size / 2, world_size / 2, 0)

# Initialize the game window
pygame.init()
screen = pygame.display.set_mode((world_size, world_size))
pygame.display.set_caption('Particle Filter Localization')

# Generate walls
num_walls = 20
walls = WallGenerator(world_size).generate_walls(num_walls)

weights = np.ones(world.num_particles) / world.num_particles

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Draw particles
    world.draw_particles(screen)

    # Move the robot
    robot.move(world, walls)

    # Move the particles
    delta_x = 5 * np.cos(robot.orientation)
    delta_y = 5 * np.sin(robot.orientation)
    delta_orientation = 0.1
    world.resample_particles(weights)
    world.move_particles(delta_x, delta_y, delta_orientation, walls)

    # Get sensor measurements
    Z = robot.sense(world)

    # Update weights and resample
    weights = world.update_weights(Z, 50.0)
    world.resample_particles(weights)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    time.sleep(0.1)

    # Draw particles
    world.draw_particles(screen)

    # Draw robot
    robot.draw(screen)

    pygame.display.flip()

pygame.quit()
