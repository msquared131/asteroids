import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))

        for player in updatable:
            player.update(dt)

        for player in drawable:
            player.draw(screen)

        for asteriodObject in asteroids:
            if asteriodObject.is_colliding(player):
                print("Game over!")
                sys.exit()
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()