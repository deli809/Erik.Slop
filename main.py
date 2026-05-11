import pygame
import pathlib
import random

pygame.init()

ERIJ_SOUND = pygame.mixer.Sound(pathlib.Path("./assets/pot_noddle.ogg"))
FONT = pygame.font.Font(None, 24)
ERIJ = pygame.image.load(pathlib.Path("./assets/erij.jpg"))
ERIJ_SIZE = pygame.Vector2(100, 200)
DOG = pygame.image.load(pathlib.Path("./assets/dogg.png"))
DOG_SIZE = pygame.Vector2(100, 200)

def main():
    character = pygame.transform.scale(DOG, DOG_SIZE)
    enemy = pygame.transform.scale(ERIJ, ERIJ_SIZE)
    window = pygame.display.set_mode(size=pygame.Vector2(800, 600))
    clock = pygame.time.Clock()
    position = pygame.Vector2(800 / 2, 600 / 2)
    enemy_position = pygame.Vector2(800, 600)
    score = 0
    speed = 20
    running = True

    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.unicode == "w":
                    position = pygame.Vector2(0, -speed) + position  
                elif event.unicode == "a":
                    position = pygame.Vector2(-speed, 0) + position
                elif event.unicode == "s":
                    position = pygame.Vector2(0, speed) + position
                elif event.unicode == "d":
                    position = pygame.Vector2(speed, 0) + position

                if pygame.Rect(position, DOG_SIZE).clip(pygame.Rect(enemy_position, ERIJ_SIZE)):
                    score += 1
                    ERIJ_SOUND.play()
                    enemy_position = pygame.Vector2(random.randint(0, 800), random.randint(0, 600))

        window.fill(pygame.Color(100, 0, 100, 255))      
        window.blit(character, position - DOG_SIZE / 2) 
        window.blit(enemy, enemy_position - ERIJ_SIZE / 2)
        window.blit(FONT.render(f"Score: {score}", True, pygame.Color(18, 212, 89, 255)), pygame.Vector2(0, 0)) 


     

        pygame.display.flip()
        clock.tick(60.0)





if __name__ == "__main__":
    main()
