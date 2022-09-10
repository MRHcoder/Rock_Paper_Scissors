import pygame


class InputBox():
	"""A class for the input box for the user to enter their name"""

	def __init__(self, rps):
		"""create the input box and accept text"""
		self.settings = rps.settings
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()
		self.txt_color = (255, 255, 255)
		self.box_color = (0, 0, 200)
		self.width, self.height = 600, 150
		self.font = pygame.font.SysFont(None, 72)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.active = False  # Controls if the box has been clicked
		self.name = False  # Controls if the user finished entering their name
		self.text = ''
		self.render_text()

	def render_text(self):
		"""Capture text as user inputs it"""
		self.text_img = self.font.render(self.text, True, self.txt_color)
		self.text_rect = self.text_img.get_rect()
		self.text_rect.center = self.rect.center

	def show_text(self):
		"""Draw the text and box to the screen"""
		self.screen.fill(self.box_color, self.rect)
		self.screen.blit(self.text_img, self.text_rect)
