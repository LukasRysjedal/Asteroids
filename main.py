import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()

    #Clock and delta time
    clock = pygame.time.Clock()
    dt: float = 0.0

    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
