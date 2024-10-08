import pygame

from constants import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # add Player class to both groups

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # game loop
    while True:
        # allow user to close or quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # set screen color black

        for u in updatable:
            u.update(dt)
        
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()  # refresh the screen
        dt = clock.tick(60) / 1000  # convert to seconds


if __name__ == "__main__":
    main()