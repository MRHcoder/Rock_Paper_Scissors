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
		if self.settings.cpu_players == 1:
			number_cpus = '2'
		else:
			number_cpus = str(self.settings.cpu_players)
		self.display_image = self.font.render(number_cpus, True, self.text_color, self.settings.bg_color)
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
		self._play_again()

	def prep_results(self):
		"""Showing the results"""
		self.display_image = self.font.render(self.settings.results, True, self.text_color, self.settings.bg_color)
		self.display_rect = self.display_image.get_rect()
		self.display_rect.center = self.screen_rect.center

	def _play_again(self):
		"""Asks to play again if game is over"""
		self.play_image = self.font.render('Press Y to play again!', True, self.text_color, self.settings.bg_color)
		self.play_rect = self.play_image.get_rect()
		self.play_rect.top = self.display_rect.bottom + 10
		self.play_rect.centerx = self.screen_rect.centerx

	def show_results(self):
		"""Draw the display to the screen"""
		self.screen.blit(self.display_image, self.display_rect)
		if self.settings.results != 'Tie! Go again':
			self.screen.blit(self.play_image, self.play_rect)


class StyleRules(DisplayBox):
	"""Class for the rules of the different game styles"""

	def __init__(self, rps):
		"""Initialize the settings for the rules displays"""
		super().__init__(rps)

		self.font = pygame.font.SysFont(None, 36)

		# Importing the buttons to use their rects as alignment for the rules to display underneath them
		from start_buttons_rps import ClassicButton, AdvancedButton
		self.classic_button = ClassicButton(self)
		self.advanced_button = AdvancedButton(self)

		self.classic_rules = 'Original Version: \n' \
			'Rock, Paper, Scissors\n\n\n' \
			'Rock beats Scissors\n' \
			'Scissors beats Paper\n' \
			'Paper beats Rock'
		self.advanced_rules = 'Advanced Version:\n ' \
			'Rock, Paper, Scissors, Lizard, Spock\n\n' \
			'Rock beats Scissors & Lizard\n' \
			'Scissors beats Paper & Lizard\n' \
			'Paper beats Rock & Spock\n' \
			'Lizard beats Paper & Spock\n' \
			'Spock beats Scissors & Rock'

	def show_style_rules(self):
		"""Draw the display to the screen"""

		# Blit the classic rules
		classic_words = self.classic_rules.splitlines()
		y = self.classic_button.rect.bottom + 15
		for line in classic_words:
			line_surface = self.font.render(line, True, self.text_color, self.settings.bg_color)
			line_width, line_height = line_surface.get_size()
			line_surface_rect = line_surface.get_rect()
			line_surface_rect.centerx = self.classic_button.rect.centerx
			self.screen.blit(line_surface, (line_surface_rect.x, y))
			y += line_height  # Move to the next line

		# Blit the advanced rules
		advanced_words = self.advanced_rules.splitlines()
		y = self.advanced_button.rect.bottom + 15
		for line in advanced_words:
			line_surface = self.font.render(line, True, self.text_color, self.settings.bg_color)
			line_width, line_height = line_surface.get_size()
			line_surface_rect = line_surface.get_rect()
			line_surface_rect.centerx = self.advanced_button.rect.centerx
			self.screen.blit(line_surface, (line_surface_rect.x, y))
			y += line_height  # Move to the next line


class ModeRules(DisplayBox):
	"""Class for the rules of the different game styles"""

	def __init__(self, rps):
		"""Initialize the settings for the rules displays"""
		super().__init__(rps)

		self.font = pygame.font.SysFont(None, 36)

		# Importing the buttons to use their rects as alignment for the rules to display underneath them
		from start_buttons_rps import OneVsOneButton, KothButton
		self.ovo_button = OneVsOneButton(self)
		self.koth_button = KothButton(self)

		self.ovo_rules = 'One vs. One against the CPU!'
		self.koth_rules = 'Tournament vs. multiple CPUs!'

	def show_mode_rules(self):
		"""Draw the display to the screen"""
		# Blit the 1v1 rules
		y = self.ovo_button.rect.bottom + 15
		line_surface = self.font.render(self.ovo_rules, True, self.text_color, self.settings.bg_color)
		line_surface_rect = line_surface.get_rect()
		line_surface_rect.centerx = self.ovo_button.rect.centerx
		self.screen.blit(line_surface, (line_surface_rect.x, y))

		# Blit the KOTH rules
		y = self.koth_button.rect.bottom + 15
		line_surface = self.font.render(self.koth_rules, True, self.text_color, self.settings.bg_color)
		line_surface_rect = line_surface.get_rect()
		line_surface_rect.centerx = self.koth_button.rect.centerx
		self.screen.blit(line_surface, (line_surface_rect.x, y))


class KothInstructions(DisplayBox):
	"""Class for the instructions to play the King of the Hill game mode"""

	def __init__(self, rps):
		"""Initialize the settings for the instructions displays"""
		super().__init__(rps)

		self.font = pygame.font.SysFont(None, 48)

		self.instructions = 'Choose between 2 to 5 Computer players to be in the tournament!\n\n ' \
			'Press "enter" to continue'

	def show_instructions(self):
		"""Draw the display to the screen"""

		# Blit the instructions
		instructions = self.instructions.splitlines()
		y = self.screen_rect.centery / 2.2
		for line in instructions:
			line_surface = self.font.render(line, True, self.text_color, self.settings.bg_color)
			line_width, line_height = line_surface.get_size()
			line_surface_rect = line_surface.get_rect()
			line_surface_rect.centerx = self.screen_rect.centerx
			self.screen.blit(line_surface, (line_surface_rect.x, y))
			y += line_height  # Move to the next line
