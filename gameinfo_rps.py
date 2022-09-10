import pygame.font

class GameInfo:
	"""A class to show the gameplay info"""

	def __init__(self, rps):
		"""Create the game info"""

		# Settings
		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()

		# Font settings
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 24)

		self._prep_quit()
		self.prep_game()
		self.prep_round()
		self.prep_players()

	def _prep_quit(self):
		"""Prep the q for quit instruction"""
		self.quit_img = self.font.render('Press Q to quit', True, self.text_color, self.settings.bg_color)
		self.quit_rect = self.quit_img.get_rect()
		self.quit_rect.right = self.screen_rect.right - 10
		self.quit_rect.bottom = self.screen_rect.bottom - 10

	def prep_game(self):
		"""Prep the game mode & game style displays"""
		self.mode = self.settings.game_mode
		self.style = self.settings.game_style
		mode = f'Game Mode: {self.mode}'
		style = f'Style: {self.style}'

		self.style_img = self.font.render(style, True, self.text_color, self.settings.bg_color)
		self.style_rect = self.style_img.get_rect()
		self.style_rect.left = self.screen_rect.left + 10
		self.style_rect.bottom = self.screen_rect.bottom - 10

		self.mode_img = self.font.render(mode, True, self.text_color, self.settings.bg_color)
		self.mode_rect = self.mode_img.get_rect()
		self.mode_rect.left = self.screen_rect.left + 10
		self.mode_rect.bottom = self.style_rect.top - 5

	def prep_round(self):
		"""Prep the current round"""
		self.round = self.settings.round_number
		round = f'Round #: {self.round}'
		self.round_img = self.font.render(round, True, self.text_color, self.settings.bg_color)
		self.round_rect = self.round_img.get_rect()
		self.round_rect.left = self.screen_rect.left + 10
		self.round_rect.bottom = self.mode_rect.top - 5

	def prep_players(self):
		"""Prep the current # of players"""
		self.players = self.settings.remaining_players
		players = f'Players Remaining: {self.players}'
		self.players_img = self.font.render(players, True, self.text_color, self.settings.bg_color)
		self.players_rect = self.players_img.get_rect()
		self.players_rect.left = self.screen_rect.left + 10
		self.players_rect.bottom = self.round_rect.top - 5

	def show_info(self):
		"""Display all of the game info"""
		self.screen.blit(self.mode_img, self.mode_rect)
		self.screen.blit(self.style_img, self.style_rect)
		self.screen.blit(self.quit_img, self.quit_rect)
		if self.settings.game_mode == 'King of the Hill':
			self.screen.blit(self.round_img, self.round_rect)
			self.screen.blit(self.players_img, self.players_rect)
