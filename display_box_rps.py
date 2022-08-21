import pygame.font


class DisplayBox:
	"""Class for a display box"""

	def __init__(self, rps):
		"""Initialize the display box settings"""
		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()

		# Font settings
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 72)


class CpuCount(DisplayBox):
	"""Class for the CPU count box"""

	def __init__(self, rps):
		"""Initialize the settings for the CPU count display box"""
		super().__init__(rps)

		# Display prompt
		self.prep_count()

	def prep_count(self):
		"""Showing the numbers of CPUs"""
		number_cpus = str(self.settings.cpu_players)
		self.display_image = self.font.render(number_cpus, True, self.text_color,
											  self.settings.bg_color)
		self.display_rect = self.display_image.get_rect()
		self.display_rect.center = self.screen_rect.center

	def show_count(self):
		"""Draw the display to the screen"""
		self.screen.blit(self.display_image, self.display_rect)


class Results(DisplayBox):
	"""Class for the results display box"""

	def __init__(self, rps):
		"""Initialize the settings for the results display box"""
		super().__init__(rps)

		# Display prompt
		self.prep_results()

	def prep_results(self):
		"""Showing the results"""
		self.display_image = self.font.render(self.settings.results, True, self.text_color,
											  self.settings.bg_color)
		self.display_rect = self.display_image.get_rect()
		self.display_rect.center = self.screen_rect.center

	def show_results(self):
		"""Draw the display to the screen"""
		self.screen.blit(self.display_image, self.display_rect)
