import pygame


class Choices:
	"""Class for the different choices of Rock, Paper, Scissors, Lizard, Spock"""

	def __init__(self, rps):
		"""Initialize the choice buttons for the game"""

		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()
		self.screen_width = self.screen.get_width()
		self.screen_middle = self.screen_rect.centerx
		self.game_style = self.settings.game_style
		self.game_style_classic = self.settings.classic()
		self.game_style_advanced = self.settings.advanced()
		self.position = {}

		self._button_positions()

	def _button_positions(self):
		"""Sets the choice button location based on game mode"""
		count = 1
		if self.game_style == 'Classic':
			for option in self.game_style_classic:
				self.option = pygame.image.load(f'images/{option}.bmp')
				self.option_rect = self.option.get_rect()
				self.option_rect.centerx = self.screen_width * (count / 6)
				self.option_rect.centery = self.screen_rect.centery
				self.position[option] = {self.option: self.option_rect}  # saves the choice as key and surface and
				# rect as key:value pair
				count += 2
		elif self.game_style == 'Advanced':
			for option in self.game_style_advanced:
				self.option = pygame.image.load(f'images/{option}.bmp')
				self.option_rect = self.option.get_rect()
				self.option_rect.centerx = self.screen_width * (count / 10)
				self.option_rect.centery = self.screen_rect.centery
				self.position[option] = {self.option: self.option_rect}  # saves the choice as key and surface and
				# rect as key:value pair
				count += 2

	def draw_user_choices(self):
		"""Draws the choice buttons"""
		for option, location in self.position.items():
			for surface in location:
				self.screen.blit(surface, location[surface])
