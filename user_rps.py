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
		self.name = ''
		self.color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		self.image = pygame.image.load('images/player.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = (self.screen_rect.centerx, self.screen_rect.bottom - 50)

	def save_name(self, name):
		"""Saves the name the user input as this User instance name"""
		self.name = name
		self.name_img = self.font.render(self.name, True, self.color)
		self.name_rect = self.name_img.get_rect()
		self.name_rect.midtop = self.rect.midbottom

	def blitme(self):
		"""Draw the user pic and name"""
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.name_img, self.name_rect)
