import numpy as np
import pygame
from robot import Robot

class World:
    def __init__(self, world_size, num_particles=10000):
        self.world_size = world_size
        self.num_particles = num_particles
        self.points = np.array([[0, 0], [0, world_size], [world_size, world_size], [world_size, 0]])
        x = np.random.uniform(0, world_size, size=self.num_particles)
        y = np.random.uniform(0, world_size, size=self.num_particles)
        orientations = np.random.uniform(0, 2 * np.pi, size=self.num_particles)
        self.particles = [Robot(x[i], y[i], orientations[i]) for i in range(self.num_particles)]

    def update_weights(self, Z, sensor_noise):
        weights = []
        for particle in self.particles:
            z = particle.sense(self)
            weight = np.sum(-0.5 * ((z - Z) ** 2) / (sensor_noise ** 2))
            weights.append(weight)
        weights = np.array(weights)
        max_weight = np.max(weights)
        weights = np.exp(weights - max_weight)
        weights = np.clip(weights, 1e-10, 1.0)  # Clip the weights to avoid numerical issues
        weights /= weights.sum()
        return weights

    def resample_particles(self, weights):
        indices = np.random.choice(len(self.particles), size=len(self.particles), p=weights, replace=True)
        self.particles = [Robot(self.particles[i].x, self.particles[i].y, self.particles[i].orientation) for i in indices]

    def move_particles(self, delta_x, delta_y, delta_orientation, walls):
        for p in self.particles:
            new_x = p.x + delta_x + np.random.normal(0, 0.5)
            new_y = p.y + delta_y + np.random.normal(0, 0.5)
            collision = False
            if not (0 <= new_x <= self.world_size and 0 <= new_y <= self.world_size):
                collision = True
            else:
                for wall in walls:
                    if wall.collidepoint(new_x, new_y):
                        collision = True
                        break

            if not collision:
                p.x = new_x
                p.y = new_y
            p.orientation += delta_orientation + np.random.normal(0, 0.1)

    def draw_particles(self, screen):
        for p in self.particles:
            pygame.draw.circle(screen, (11, 0, 255), (int(p.x), int(p.y)), 2)
