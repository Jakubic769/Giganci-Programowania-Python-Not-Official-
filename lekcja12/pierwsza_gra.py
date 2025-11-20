import pygame

pygame.init()


def calculate_player_movement(keys):
    step = 10
    delta_x = 0
    delta_y = 0
    
    if keys[pygame.K_a] == True:
        delta_x -= step
    if keys[pygame.K_w] == True:
        delta_y -= step
    if keys[pygame.K_s] == True:
        delta_y += step
    if keys[pygame.K_d] == True:
        delta_x += step
    
    return [delta_x, delta_y]

def set_player_position(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    image = pygame.transform.scale(image, (24, 24))
    surface = image.convert()
    
    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)
    
    rect = surface.get_rect(center=position)
    
    return [image, surface, rect]

def print_image(img_list) -> None:
    # [image, surface, rect]
    image, surface, rect = img_list # img = img_list[0], surface = img_list[1], rect = img_list[2]
    screen_surface.blit(surface, rect)
    
def limit_position(position):
    x, y = position
    x = max(0, min(x, SCREEN_WIDTH))
    y = min(SCREEN_HEIGHT, max(y, 0))
        
    return [x, y]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = [5, 225, 25]

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
player = load_image("lekcja12/player.jpg", player_pos)

pygame.display.set_caption("Pierwsza gra")

clock = pygame.time.Clock()

game_status = True
while game_status:
    screen_surface.fill(BACKGROUND_COLOR)
    
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
            
    key_pressed = pygame.key.get_pressed()
    przesuniecie = calculate_player_movement(key_pressed)
    
    player_pos[0] += przesuniecie[0]
    player_pos[1] += przesuniecie[1]
    
    player_pos = limit_position(player_pos)
    
    player = set_player_position(player, player_pos)
    print_image(player)

    pygame.display.update()
    clock.tick(240)
    
pygame.quit()
quit()