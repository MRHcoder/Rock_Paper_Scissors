import sys
from time import sleep

import pygame

from settings_rps import Settings
from cpu_rps import CPU
from start_buttons_rps import PlayButton, ModeButtons, PlusMinusButtons  # , StyleButtons
from user_rps import User
from input_box_rps import InputBox
from choice_buttons_rps import Choices
from display_box_rps import DisplayBox, CpuCount, Results


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

        # The mode buttons
        self.classic_mode_button = ModeButtons(self, 'Classic')
        self.advanced_mode_button = ModeButtons(self, 'Advanced')
        self.one_v_one_button = ModeButtons(self, '1 vs 1')
        self.koth_button = ModeButtons(self, 'King of the Hill')

        # The +/- buttons
        self.plus_button = PlusMinusButtons(self, '+')
        self.minus_button = PlusMinusButtons(self, '-')
        self.display_box = DisplayBox(self)
        self.cpu_count = CpuCount(self)

        # Results of a round
        self.round_results = Results(self)

        # Username input box
        self.input = InputBox(self)
        group = pygame.sprite.Group(self.input)

    def run_game(self):
        """Main game loop"""
        while True:  # Watch for keyboard and mouse events
            self._check_events()

            if self.settings.ongoing_turn:
                self._computer_choice()
                self._compare_choices()
                self.settings.ongoing_turn = False

            self._update_screen()

            if self.settings.next_round:  # self.user.status:
                sleep(1.5)
                self._new_round()
                self.settings.next_round = False

    def _check_events(self):
        """Check for mouse & keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_n:
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
                elif not self.settings.game_mode or not self.settings.game_style:
                    self._check_game_mode(mouse_pos)
                elif not self.settings.cpu_options:
                    self._number_of_cpus(mouse_pos)
                elif not self.settings.ongoing_turn:
                    self._check_choice(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """starts the game if the play button is clicked"""
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if play_button_clicked:
            self.settings.game_active = True

    # def _check_input(self, mouse_pos, event):
    #     """allows user to type in their name"""
    #     text_box_clicked = self.input.rect.collidepoint(mouse_pos)
    #     if text_box_clicked and self.settings.game_active:
    #         self.active = True
    #         if event.type == pygame.KEYDOWN and self.active:
    #             if event.key == pygame.K_RETURN:
    #                 self.active = False
    #             elif event.key == pygame.K_BACKSPACE:
    #                 self.text = self.text[:-1]
    #             else:
    #                 self.text += event.unicode
    #             self.input.render_text()

    def _check_game_mode(self, mouse_pos):
        """chooses the game mode the user clicks on"""
        classic_mode_button_clicked = self.classic_mode_button.rect.collidepoint(mouse_pos)
        advanced_mode_button_clicked = self.advanced_mode_button.rect.collidepoint(mouse_pos)
        one_v_one_button_clicked = self.one_v_one_button.rect.collidepoint(mouse_pos)
        koth_button_clicked = self.koth_button.rect.collidepoint(mouse_pos)
        if classic_mode_button_clicked:
            self.settings.game_mode = 'Classic'
            self.choice_buttons = Choices(self)
        elif advanced_mode_button_clicked:
            self.settings.game_mode = 'Advanced'
            self.choice_buttons = Choices(self)

        if one_v_one_button_clicked:
            self.settings.game_style = '1 vs 1'
        elif koth_button_clicked:
            self.settings.game_style = 'King of the Hill'

    def _number_of_cpus(self, mouse_pos):
        """Instantiates the # of CPUs the user chooses"""
        plus_button_clicked = self.plus_button.rect.collidepoint(mouse_pos)
        minus_button_clicked = self.minus_button.rect.collidepoint(mouse_pos)
        if self.settings.cpu_players == 1:
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
        for i in range(1, self.settings.cpu_players + 1):
            self.cpu.number = i
            self.cpu.prep_cpu()
            self.cpu.count += 1
            self.cpu.choice[i] = ''

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
        if self.settings.game_style == '1 vs 1':
            if self.user.choice == self.cpu.choice[1]:
                self.settings.results = 'Tie! Go again'
                self.settings.next_round = True
            elif self.cpu.choice[1] in self.settings.rules_advanced[self.user.choice]:
                self.settings.results = 'You won!'
                self.user.status = False
            else:
                self.settings.results = 'You lost!'
                self.user.status = False
        elif self.settings.game_style == 'King of the Hill':
            round_choices = self.cpu.choice.copy()
            # round_choices = {k:v for (k,v) in self.cpu.choice.items() if v is not None}
            round_choices[self.settings.player_count] = self.user.choice
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
                        self.settings.remaining_players -= 1

        self.round_results.prep_results()

    def _new_round(self):
        """Sets up the next round based on the last results"""
        self.settings.new_round()

    def _new_game(self):
        """Starts the game over if the player wants to play again"""
        self.settings.new_game()
        self.cpu.reset_cpu()
        self.cpu_count.prep_count()

    def _update_screen(self):
        """Update screen after events occur"""
        self.screen.fill(self.settings.bg_color)

        # Drawing the buttons at the beginning of a game or new round
        if not self.settings.game_active:
            self.play_button.draw_button()
        elif not self.settings.game_mode or not self.settings.game_style:
            self.classic_mode_button.draw_button()
            self.advanced_mode_button.draw_button()
            self.one_v_one_button.draw_button()
            self.koth_button.draw_button()
        elif not self.settings.cpu_options:
            self.plus_button.draw_button()
            self.minus_button.draw_button()
            self.cpu_count.show_count()
        elif not self.settings.ongoing_turn and not self.settings.results:
            self.choice_buttons.draw_user_choices()
        elif self.settings.results:
            self.cpu.blitme()
            self.user.blitme()
            self.round_results.show_results()

        pygame.display.flip()


if __name__ == '__main__':
    rps = RockPaperScissors()
    rps.run_game()
