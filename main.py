# By Trevor Buchanan

import pygame

from GameLogic.GameObjects.Character.Animal.animal_manager import AnimalManager
from GameLogic.GameObjects.Character.Player.player_manager import PlayerManager
from GameLogic.GameObjects.Enviroment.plant_manager import PlantManager
from GameLogic.Game.game import Game
from GameLogic.GameObjects.Character.Animal.Training.epoch_manager import EpochManager
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import FPS, BORDER, ANIMAL_AMOUNT, PLANT_AMOUNT
from GameLogic.GameUtilities.utility import write_to_screen

if __name__ == '__main__':
    clock = pygame.time.Clock()

    # Set up the game
    g = Game()
    for _ in range(ANIMAL_AMOUNT):
        g.game_objects.append(AnimalManager())

    for _ in range(PLANT_AMOUNT):
        g.game_objects.append(PlantManager())

    g.game_objects.append(EpochManager())
    g.game_objects.append(PlayerManager())

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

        g.run_game_iteration()

        fps = str(int(clock.get_fps()))
        write_to_screen(f"FPS: {fps}", [BORDER.width - 120, 10], WHITE)

        pygame.display.update()

pygame.quit()
