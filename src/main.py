import pygame

from game import Game
from utils.settings import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player Animations")
    clock = pygame.time.Clock()

    game = Game()

    running = True
    while running:
        dt = clock.tick(60) / 1000  # Delta time in seconds (FPS = 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update(dt)
        game.render(screen)
        pygame.display.flip()

    pygame.quit()

main()