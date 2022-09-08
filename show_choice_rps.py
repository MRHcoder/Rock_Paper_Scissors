import pygame


class ShowChoice:
	"""A class that shows each player's choice/status after each round"""

	def __init__(self, rps, choices):
		"""Instantiate the choices per round"""

		# Settings
		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()

		# Font settings
		self.text_color = (250, 0, 0)
		self.font = pygame.font.SysFont(None, 72)

		# Choice of the round passed in as a dictionary
		self.choices = choices.copy()

		# Player positions
		self.user_position = rps.user.rect
		self.cpu_position = rps.cpu.position

		self._position_choices(rps)

	def _position_choices(self, rps):
		"""Position each player choice onto the screen"""
		for choice in self.choices:
			if choice == self.settings.player_count:
				if self.choices[choice] is None:
					self.choice = self.font.render('ELIMINATED', True, self.text_color, self.settings.bg_color)
				else:
					self.choice = pygame.image.load(f'images/{self.choices[choice]}.bmp')
				self.choice_rect = self.choice.get_rect()
				self.choice_rect.midbottom = rps.user.rect.midbottom
				self.choices[choice] = [self.choice, self.choice_rect]
			else:
				if self.choices[choice] is None:
					self.choice = self.font.render('ELIMINATED', True, self.text_color, self.settings.bg_color)
				else:
					self.choice = pygame.image.load(f'images/{self.choices[choice]}.bmp')
				self.choice_rect = self.choice.get_rect()

				# Get the cpu image rect for this cpu number
				self.cpu_pos = rps.cpu.position[choice]
				self.cpu_pos_rect = list(self.cpu_pos.values())[0][0]
				self.choice_rect.midbottom = self.cpu_pos_rect.midtop

				self.choices[choice] = [self.choice, self.choice_rect]

	def show_choices(self):
		"""Blit each player choice onto the screen"""
		for choice in self.choices:
			img = self.choices[choice][0]
			rct = self.choices[choice][1]
			self.screen.blit(img, rct)
