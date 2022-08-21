import pygame.font


class PlayButton:
	"""Class for the play button"""

	def __init__(self, rps, msg='Play'):
		"""Initialize the play button"""
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()

		# Buttons settings
		self.width, self.height = 300, 150
		self.button_color = (0, 0, 200)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Position the button
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Button message
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Creating the message to display"""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw the button to the screen"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class ModeButtons:
	"""Class for the game mode buttons"""

	def __init__(self, rps, msg):
		"""Initialize the mode buttons"""
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()

		# Button settings
		self.width, self.height = 300, 150
		self.button_color = (0, 0, 200)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Position the buttons
		if msg == 'Classic':
			self.rect = pygame.Rect(0, 0, self.width, self.height)
			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx - self.width), (self.screen_rect.centery
																							 - self.height)
		elif msg == 'Advanced':
			self.rect = pygame.Rect(0, 0, self.width, self.height)
			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx + self.width), (self.screen_rect.centery
																							 - self.height)
		elif msg == '1 vs 1':
			self.rect = pygame.Rect(0, 0, self.width, self.height)
			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx - self.width), (self.screen_rect.centery
																							 + self.height)
		elif msg == 'King of the Hill':
			self.rect = pygame.Rect(0, 0, self.width, self.height)
			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx + self.width), (self.screen_rect.centery
																							 + self.height)

		# Button message
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Creating the message to display"""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw the button to the screen"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


# class StyleButtons:
# 	"""Class for the game style buttons"""
#
# 	def __init__(self, rps, msg):
# 		"""Initialize the style buttons"""
# 		self.screen = rps.screen
# 		self.screen_rect = self.screen.get_rect()
#
# 		# Button settings
# 		self.width, self.height = 300, 150
# 		self.button_color = (0, 0, 200)
# 		self.text_color = (255, 255, 255)
# 		self.font = pygame.font.SysFont(None, 48)
#
# 		# Position the buttons
# 		if msg == '1 vs 1':
# 			self.rect = pygame.Rect(0, 0, self.width, self.height)
# 			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx - self.width), (self.screen_rect.centery
# 																							 - self.height/2)
# 		elif msg == 'King of the Hill':
# 			self.rect = pygame.Rect(0, 0, self.width, self.height)
# 			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx + self.width), (self.screen_rect.centery
# 																							 - self.height/2)
#
# 		# Button message
# 		self._prep_msg(msg)
#
# 	def _prep_msg(self, msg):
# 		"""Creating the message to display"""
# 		self.msg_image = self.font.render(msg, True, self.text_color,
# 				self.button_color)
# 		self.msg_image_rect = self.msg_image.get_rect()
# 		self.msg_image_rect.center = self.rect.center
#
# 	def draw_button(self):
# 		"""Draw the button to the screen"""
# 		self.screen.fill(self.button_color, self.rect)
# 		self.screen.blit(self.msg_image, self.msg_image_rect)


class PlusMinusButtons:
	"""Class for +/- buttons used to change # of CPU players"""

	def __init__(self, rps, msg):
		"""Initialize the mode buttons"""
		self.screen = rps.screen
		self.screen_rect = self.screen.get_rect()

		# Button settings
		self.width, self.height = 300, 150
		self.button_color = (0, 0, 200)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 72)

		# Position the buttons
		if msg == '+':
			self.rect = pygame.Rect(0, 0, self.width, self.height)
			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx + self.width), self.screen_rect.centery
		elif msg == '-':
			self.rect = pygame.Rect(0, 0, self.width, self.height)
			self.rect.centerx, self.rect.centery = (self.screen_rect.centerx - self.width), self.screen_rect.centery

		# Button message
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Creating the message to display"""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw the button to the screen"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
