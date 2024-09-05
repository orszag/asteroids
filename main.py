import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    pygame.display.set_caption("Asteroids")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game closed")
                return
        
        screen.fill("black")
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("GAME OVER!")
                #asteroid.collid = True
                return
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip() #update full display
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()