import pygame
from constants import *
from circleshape import *
import random


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		if self.radius <= ASTEROID_MIN_RADIUS:
			self.kill()
		else:
			random_angle = random.uniform(20, 50)
			velocity = self.velocity.rotate(random_angle)
			neg_velocity = self.velocity.rotate(-random_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid.velocity = velocity
			asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid.velocity = neg_velocity
			self.kill()