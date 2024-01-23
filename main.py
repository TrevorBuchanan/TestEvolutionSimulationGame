# By Trevor Buchanan

import pygame

from GameLogic.GameObjects.Character.animal_manager import AnimalManager
from GameLogic.GameObjects.Character.player_manager import PlayerManager
from GameLogic.Game.game import Game
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import FPS, SCREEN, FONT, BORDER, ANIMAL_AMOUNT, PLANT_AMOUNT



if __name__ == '__main__':
    clock = pygame.time.Clock()

    g = Game()
    g.game_objects.append(PlayerManager())

    for _ in range(ANIMAL_AMOUNT):
        g.game_objects.append(AnimalManager())

    for _ in range(PLANT_AMOUNT):
        g.game_objects.append(PlantManager())

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

        g.run_game()

        fps = str(int(clock.get_fps()))
        text = FONT.render(f"FPS: {fps}", True, WHITE)
        SCREEN.blit(text, [BORDER.width - 100, 10])

        pygame.display.update()

pygame.quit()
