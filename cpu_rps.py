import pygame
import random


class CPU:
	"""A class to represent a computer player"""

	def __init__(self, rps):
		"""Initialize a computer player name & position"""
		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_width = self.screen.get_width()
		self.screen_rect = rps.screen.get_rect()
		self.game_style_classic = list(self.settings.classic())
		self.game_style_advanced = list(self.settings.advanced())

		# Initial settings and counters used to place CPUs
		self.number_text_color = (0, 0, 0)
		self.number_font = pygame.font.SysFont(None, 55)

		self.reset_cpu()
		self.prep_cpu()
		self.cpu_choice()

	def reset_cpu(self):
		self.number = 0
		self.count = 0
		self.position = {}
		self.choice = {}

	def prep_cpu(self):
		"""Numbers and places the cpu"""
		if self.number > 0:
			self.cpu_image = pygame.image.load('images/computer.bmp').convert()
			self.cpu_rect = self.cpu_image.get_rect()
			self.cpu_rect.midtop = ((self.screen_width * (self.number + self.count)) / (2 * self.settings.cpu_players),
									self.cpu_rect.height * .85)
			number = f'CPU#: {self.number}'
			self.cpu_number = self.number_font.render(number, True, self.number_text_color)
			self.cpu_number_rect = self.cpu_number.get_rect()
			self.cpu_number_rect.midtop = self.cpu_rect.midbottom
			self.position[self.number] = {(self.cpu_image, self.cpu_number): (self.cpu_rect, self.cpu_number_rect)}

	def blitme(self):
		"""Draw the computer's pic"""
		for num, imgs in self.position.items():
			for surface, rectangle in imgs.items():
				self.screen.blit(surface[0], rectangle[0])
				self.screen.blit(surface[1], rectangle[1])

	def cpu_choice(self):
		"""Makes the computer choose an option based on the game mode"""
		if self.settings.game_style == 'Classic':
			self.choice[self.number] = random.choice(self.game_style_classic)
		elif self.settings.game_style == 'Advanced':
			self.choice[self.number] = random.choice(self.game_style_advanced)
