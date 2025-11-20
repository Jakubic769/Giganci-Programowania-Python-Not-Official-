import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pierwsza gra")

clock = pygame.time.Clock()

game_status = True
while game_status:
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()