import pygame
import constants
import player
import asteroid
import asteroidfield
import shot


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0

    updatables_container = pygame.sprite.Group()
    drawables_container = pygame.sprite.Group()
    asteroids_container = pygame.sprite.Group()
    shots_container = pygame.sprite.Group()

    player.Player.containers = (updatables_container, drawables_container)
    asteroid.Asteroid.containers = (
        asteroids_container,
        updatables_container,
        drawables_container,
    )
    asteroidfield.AsteroidField.containers = updatables_container
    shot.Shot.containers = (shots_container, updatables_container, drawables_container)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    # This is the variable that holds the player object
    player_variable = player.Player(
        constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2
    )
    # This is the variable that holds the asteroid field object which itself holds the logic to spawn asteroids
    asteroid_field_variable = asteroidfield.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatables_container.update(delta_time)

        for asteroid_item in asteroids_container:
            if asteroid_item.collision_detected(player_variable):
                print("Game over!")
                exit(0)

        for asteroid_item in asteroids_container:
            for shot_item in shots_container:
                if asteroid_item.collision_detected(shot_item):
                    asteroid_item.kill()
                    shot_item.kill()

        for item in drawables_container:
            item.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
