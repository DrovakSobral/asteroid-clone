import pygame
import constants
import player


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    player_variable = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player_variable.update(delta_time)
        player_variable.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
