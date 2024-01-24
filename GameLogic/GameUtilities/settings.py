import pygame

from GameLogic.GameUtilities.input import Input

# Set up pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("SOFTprot2")

# Screen/window settings
WIDTH, HEIGHT = 1435, 800
FPS = 50
BORDER = pygame.Rect(0, 0, WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
FONT = pygame.font.Font('freesansbold.ttf', 20)

# Game settings
ANIMAL_AMOUNT = 100

CHARACTER_RADIUS = 8

PLANT_AMOUNT = 25
PLANT_RADIUS = 15
PLANT_NUTRIENTS = 10

# User Input *** Move *** ???
INPUT = Input()
