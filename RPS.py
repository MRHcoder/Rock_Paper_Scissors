import sys
from time import sleep

import pygame

from settings_rps import Settings
from cpu_rps import CPU
from start_buttons_rps import PlayButton, ModeStyleButtons, PlusMinusButtons, OneVsOneButton, KothButton, \
    ClassicButton, AdvancedButton
from user_rps import User
from input_box_rps import InputBox
from choice_buttons_rps import Choices
from display_box_rps import DisplayBox, CpuCount, Results, StyleRules, ModeRules, KothInstructions, NamePrompt
from show_choice_rps import ShowChoice
from gameinfo_rps import GameInfo


class RockPaperScissors:
    """Overall class to manage the game and behaviors"""

    def __init__(self):
        """initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Rock, Paper, Scissors')

        # Computer players
        self.cpu = CPU(self)

        # User player
        self.user = User(self)

        # The play button
        self.play_button = PlayButton(self)

        # The game mode and style buttons
        self.mode_style_buttons = ModeStyleButtons(self)
        self.classic_button = ClassicButton(self)
        self.advanced_button = AdvancedButton(self)
        self.one_v_one_button = OneVsOneButton(self)
        self.koth_button = KothButton(self)

        # The +/- buttons
        self.plus_button = PlusMinusButtons(self, '+')
        self.minus_button = PlusMinusButtons(self, '-')
        self.display_box = DisplayBox(self)
        self.cpu_count = CpuCount(self)

        # Results of a round
        self.round_results = Results(self)

        # Username input box
        self.input = InputBox(self)
        # group = pygame.sprite.Group(self.input)

        # Game mode & style rules
        self.style_rules = StyleRules(self)
        self.mode_rules = ModeRules(self)

        # Other texts
        self.instructions = KothInstructions(self)
        self.gi = GameInfo(self)
        self.name_prompt = NamePrompt(self)

    def run_game(self):
        """Main game loop"""
        while True:  # Watch for keyboard and mouse events
            self._check_events()

            if self.settings.ongoing_turn:
                self._computer_choice()
                self._compare_choices()
                self.settings.ongoing_turn = False

            self._update_screen()

            if self.settings.next_round:
                sleep(2)
                self._new_round()
                self.settings.next_round = False

    def _check_events(self):
        """Check for mouse & keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.input.active:
                    self._get_name(event)
                else:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        self._create_cpus()
                        self.settings.cpu_options = True
                    elif event.key == pygame.K_y:
                        self._new_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.settings.game_active:
                    self._check_play_button(mouse_pos)
                elif not self.input.name:
                    self._check_input(mouse_pos)
                elif not self.settings.game_mode:
                    self._check_game_mode(mouse_pos)
                elif not self.settings.game_style:
                    self._check_game_style(mouse_pos)
                elif not self.settings.cpu_options:
                    self._number_of_cpus(mouse_pos)
                elif not self.settings.ongoing_turn:
                    self._check_choice(mouse_pos)
                    pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """starts the game if the play button is clicked"""
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if play_button_clicked:
            self.settings.game_active = True

    def _check_input(self, mouse_pos):
        """allows user to type in their name"""
        text_box_clicked = self.input.rect.collidepoint(mouse_pos)
        if text_box_clicked:
            self.input.active = True

    def _get_name(self, event):
        if event.key == pygame.K_RETURN:
            self.input.active = False
            self.input.name = True
            self.user.save_name(self.input.text)
        elif event.key == pygame.K_BACKSPACE:
            self.input.text = self.input.text[:-1]
            self.input.render_text()
        else:
            self.input.text += event.unicode
            self.input.render_text()

    def _check_game_mode(self, mouse_pos):
        """chooses the game mode the user clicks on - either 1v1 or king of the hill"""
        one_v_one_button_clicked = self.one_v_one_button.rect.collidepoint(mouse_pos)
        koth_button_clicked = self.koth_button.rect.collidepoint(mouse_pos)

        if one_v_one_button_clicked:
            self.settings.game_mode = '1 vs 1'
            self.one_v_one_button.clicked = True
        elif koth_button_clicked:
            self.settings.game_mode = 'King of the Hill'
            self.settings.game_style = 'Classic'
            self.choice_buttons = Choices(self)
            self.settings.cpu_players = 2
            self.settings.player_count += 1
            self.settings.remaining_players = self.settings.player_count
            self.gi.prep_game()

    def _check_game_style(self, mouse_pos):
        """Chooses the game style the user clicks on - either classic or advanced"""
        classic_button_clicked = self.classic_button.rect.collidepoint(mouse_pos)
        advanced_button_clicked = self.advanced_button.rect.collidepoint(mouse_pos)

        if classic_button_clicked:
            self._create_cpus()
            self.settings.game_style = 'Classic'
            self.choice_buttons = Choices(self)
        elif advanced_button_clicked:
            self._create_cpus()
            self.settings.game_style = 'Advanced'
            self.choice_buttons = Choices(self)

        self.settings.cpu_options = True
        self.gi.prep_game()

    def _number_of_cpus(self, mouse_pos):
        """Collects the # of CPUs the user chooses"""
        plus_button_clicked = self.plus_button.rect.collidepoint(mouse_pos)
        minus_button_clicked = self.minus_button.rect.collidepoint(mouse_pos)
        if self.settings.cpu_players == 2:
            if plus_button_clicked:
                self.settings.cpu_players += 1
                self.cpu_count.prep_count()
        elif self.settings.cpu_players == 5:
            if minus_button_clicked:
                self.settings.cpu_players -= 1
                self.cpu_count.prep_count()
        else:
            if plus_button_clicked:
                self.settings.cpu_players += 1
                self.cpu_count.prep_count()
            elif minus_button_clicked:
                self.settings.cpu_players -= 1
                self.cpu_count.prep_count()

        self.settings.player_count = self.settings.cpu_players + 1
        self.settings.remaining_players = self.settings.player_count

    def _create_cpus(self):
        """Instantiates the # of CPUs to start the game"""
        for i in range(1, self.settings.cpu_players + 1):
            self.cpu.number = i
            self.cpu.prep_cpu()
            self.cpu.count += 1
            self.cpu.choice[i] = ''

        self.gi.prep_players()

    def _check_choice(self, mouse_pos):
        """chooses the option the user clicks on"""
        for option, location in self.choice_buttons.position.items():
            for surface in location:
                if location[surface].collidepoint(mouse_pos):
                    self.user.choice = option
                    self.settings.ongoing_turn = True

    def _computer_choice(self):
        """Makes the CPU choose an option for the round"""
        for i in range(1, self.settings.player_count):
            self.cpu.number = i
            if self.cpu.choice[i] is None:
                continue
            else:
                self.cpu.cpu_choice()

    def _compare_choices(self):
        """Compares the player's choice to the CPU's choice to determine winner(s)"""
        if self.settings.game_mode == '1 vs 1':
            round_choices = self.cpu.choice.copy()
            round_choices[self.settings.player_count] = self.user.choice
            self.show = ShowChoice(self, round_choices)
            if self.user.choice == self.cpu.choice[1]:
                self.settings.results = 'Tie! Go again'
                self.settings.next_round = True
            elif self.cpu.choice[1] in self.settings.rules_advanced[self.user.choice]:
                self.settings.results = 'You won!'
            else:
                self.settings.results = 'You lost!'
        elif self.settings.game_mode == 'King of the Hill':
            round_choices = self.cpu.choice.copy()
            # round_choices = {k:v for (k,v) in self.cpu.choice.items() if v is not None}
            round_choices[self.settings.player_count] = self.user.choice
            self.show = ShowChoice(self, round_choices)
            if all(choice in round_choices.values() for choice in self.settings.rules_classic):  # If all the
                # possible options are chosen
                self.settings.results = f'No winners! Go again'
                self.settings.next_round = True
            elif all(choice == round_choices[1] for choice in round_choices.values()):  # If
                # every player picked the same thing (by comparing choices to CPU 1)
                self.settings.results = f'{self.settings.remaining_players}-way Tie! Go again'
                self.settings.next_round = True
            else:
                try:
                    winner, loser = set([choice for choice in round_choices.values() if choice is not None])  # find
                # the winning choice
                except ValueError:  # Catches instances where the set only contains 1 value
                    self.settings.results = f'{self.settings.remaining_players}-way Tie! Go again'
                    self.settings.next_round = True
                else:
                    if winner in self.settings.rules_classic and loser == self.settings.rules_classic[winner]:
                        winner = winner
                    else:
                        winner = loser
                    if len([choice for choice in round_choices.values() if choice == winner]) == 1:  # If only 1 winner
                        # announce it and end the game
                        if round_choices[self.settings.player_count] == winner:
                            self.settings.results = 'You won!'
                        else:
                            winning_cpu = [player for player, choice in round_choices.items() if choice == winner]  #
                            # WASTE OF MEMORY LOOPING AND SAVING THIS TO LIST. LOOK FOR WAY TO REFACTOR AND MAKE IT JUST
                            # PART OF THE RESULTS BELOW*****************************************************************
                            self.settings.results = f'You lost! CPU#: {winning_cpu[0]} won!'
                    elif not round_choices[self.settings.player_count] == winner:
                        self.settings.results = 'You lost!'
                    else:  # Find out which players made it to the next round
                        for player_number in self.cpu.choice:
                            if not self.cpu.choice[player_number] == winner:
                                self.cpu.choice[player_number] = None  # Change losing answers to None to get skipped
                                # next round
                        self.settings.results = f'You made it to the next round!'
                        self.settings.next_round = True
                        self.settings.remaining_players = len([cpu for cpu in self.cpu.choice.values() if cpu is not
                                                               None]) + 1
                        self.gi.prep_players()

        self.round_results.prep_results()

    def _new_round(self):
        """Sets up the next round based on the last results"""
        pygame.mouse.set_visible(True)
        self.settings.new_round()
        self.gi.prep_round()

    def _new_game(self):
        """Starts the game over if the player wants to play again"""
        pygame.mouse.set_visible(True)
        self.settings.new_game()
        self.cpu.reset_cpu()
        self.cpu_count.prep_count()
        self.gi.prep_round()

    def _update_screen(self):
        """Update screen after events occur"""
        self.screen.fill(self.settings.bg_color)

        # Drawing the buttons at the beginning of a game or new round
        if not self.settings.game_active:
            self.play_button.draw_button()
        elif not self.input.name:
            self.name_prompt.show_instructions()
            self.input.show_text()
        elif not self.settings.game_mode:
            self.one_v_one_button.draw_button()
            self.koth_button.draw_button()
            self.mode_rules.show_mode_rules()
        elif self.settings.game_mode == '1 vs 1' and not self.settings.cpu_options:
            self.classic_button.draw_button()
            self.advanced_button.draw_button()
            self.style_rules.show_style_rules()
        elif self.settings.game_mode == 'King of the Hill' and not self.settings.cpu_options:
            self.plus_button.draw_button()
            self.minus_button.draw_button()
            self.cpu_count.show_count()
            self.instructions.show_instructions()
        elif not self.settings.ongoing_turn and not self.settings.results:
            self.choice_buttons.draw_user_choices()
            self.gi.show_info()
        elif self.settings.results:
            self.cpu.blitme()
            self.user.blitme()
            self.show.show_choices()
            self.round_results.show_results()
            self.gi.show_info()

        pygame.display.flip()


if __name__ == '__main__':
    rps = RockPaperScissors()
    rps.run_game()
