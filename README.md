### Particle Filter Localization
This is an implementation of Particle Filter Localization in Python using the Pygame library. The main goal of this project is to demonstrate how a robot can localize itself within an environment based on sensor measurements.

![robot_localization](https://user-images.githubusercontent.com/32487291/235190208-dde222e4-c33b-464e-8a6f-4a8d2d2b9463.gif)


Note: The current implementation measures only the wall corners while sensing. Users can modify the code to measure actual walls if desired.

Table of Contents:
- Theory
- Dependencies
- Usage
- Customization

#### Theory
Particle Filter Localization is a technique used to estimate the position and orientation of a robot within its environment. It uses a probabilistic method based on a set of particles, each representing a possible state of the robot. The algorithm consists of the following steps:

* Initialization: Create a set of particles with random positions and orientations.
* Motion update: Move the particles according to the robot's motion model.
* Sensor update: Update the weights of the particles based on the similarity between the robot's sensor measurements and the expected measurements from the particles.
* Resampling: Resample the particles based on their weights, favoring particles with higher weights.

The final estimate of the robot's position and orientation is obtained by calculating the weighted mean of the particles.

#### Dependencies
```
pip install -r requirements.txt
```
#### Run the code
```
python particle_filter.py
```
The Pygame window will open, showing the robot (red circle), particles (blue circles), and walls (black rectangles). The robot moves around the environment, while the particles try to mimic the robot's movements based on the sensor measurements.

#### Customization
To modify the code for measuring actual walls or to adjust other settings, edit the following files:

- robot.py: 
  - Modify the sense() method to measure actual walls instead of corners.
- particle_filter.py: 
  - Adjust the number of walls, sensor noise, or other parameters as needed.

Feel free to experiment with different settings and scenarios to improve the performance of the Particle Filter Localization algorithm.
