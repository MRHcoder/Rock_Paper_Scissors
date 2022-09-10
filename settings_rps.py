class Settings:
	"""Settings for Rock, Paper, Scissors game"""

	def __init__(self):
		"""setting the static settings"""
		self.bg_color = (220, 220, 220)

		# Keys of the dictionaries are winners over their values
		self.rules_classic = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
		self.rules_advanced = {'rock': ['scissors', 'lizard'], 'paper': ['rock', 'spock'], 'scissors': ['paper',
							'lizard'], 'lizard': ['spock', 'paper'], 'spock': ['scissors', 'rock']}

		self.game_active = False
		self.ongoing_turn = False
		self.next_round = False
		self.new_game()

	def new_game(self):
		"""Initial settings of a new game that can change based on user choices"""
		self.game_mode = False  # 1v1 or KOTH
		self.game_style = False  # Classic or Advanced
		self.cpu_options = False
		self.cpu_players = 1
		self.player_count = self.cpu_players + 1
		self.remaining_players = self.player_count
		self.round_number = 1
		self.results = None

	def new_round(self):
		"""Initial settings of each new round"""
		self.results = None
		self.round_number += 1

	def classic(self):
		"""Lets the player play in classic mode which is rock, paper, scissors only"""
		return self.rules_classic.keys()

	def advanced(self):
		"""Lets the player add Lizard and Spock as options to the game to make it more challenging"""
		return self.rules_advanced.keys()
