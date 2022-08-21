import pygame


class User:
	"""A class to represent the user"""

	def __init__(self, rps):
		"""Initialize the user to get their name and define the settings"""

		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_rect = rps.screen.get_rect()

		# Initial state of a user. Choice is RPSLS
		self.choice = None

		self.image = pygame.image.load('images/player.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""Draw the user pic"""
		self.screen.blit(self.image, self.rect)
