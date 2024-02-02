import pygame

from GameLogic.GameUtilities import colors
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import SCREEN, INPUT, BORDER, FPS
from GameLogic.GameUtilities.utility import write_to_screen


class Game:
    """
    Game class
    """
    def __init__(self):
        self.game_objects = []
        self.game_clock = 0

    def run_game(self):
        """
        Runs Game
        """
        clock = pygame.time.Clock()
        # Screen window loop
        running = True
        while running:
            # Set the frame rates
            clock.tick(FPS)
            # Check for closure
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
            # Fill the background
            SCREEN.fill(colors.DARK_GREEN)
            # Get user inputs
            INPUT.keys = pygame.key.get_pressed()
            # Run a game iteration
            self.run_iteration()
            # *** Temp *** Show FPS to screen
            fps = str(int(clock.get_fps()))
            write_to_screen(f"FPS: {fps}", [BORDER.width - 120, 10], WHITE)
            # Display to screen
            pygame.display.update()
        # End pygame
        pygame.quit()

    def run_iteration(self):
        """
        Performs one iteration of the game
        """
        # Fill the background
        SCREEN.fill(colors.DARK_GREEN)

        # Get user inputs
        INPUT.keys = pygame.key.get_pressed()

        # All game object actions
        for game_obj in self.game_objects:
            game_obj.act(self.game_objects)
            game_obj.draw()

        # Handle object removal
        for game_obj in self.game_objects:
            game_obj.end_life_if_dead(self.game_objects)
