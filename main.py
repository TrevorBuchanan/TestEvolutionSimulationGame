# By Trevor Buchanan

from GameLogic.GameObjects.Character.Animal.animal_manager import AnimalManager
from GameLogic.GameObjects.Character.Player.player_manager import PlayerManager
from GameLogic.GameObjects.Enviroment.plant_manager import PlantManager
from GameLogic.Game.game import Game
from GameLogic.GameObjects.Character.Animal.Training.epoch_manager import EpochManager
from GameLogic.GameUtilities.settings import ANIMAL_AMOUNT, PLANT_AMOUNT

if __name__ == '__main__':
    # Set up the game
    g = Game()
    for _ in range(ANIMAL_AMOUNT):
        g.game_objects.append(AnimalManager())

    for _ in range(PLANT_AMOUNT):
        g.game_objects.append(PlantManager())

    g.game_objects.append(EpochManager())
    g.game_objects.append(PlayerManager())

    g.run_game()
