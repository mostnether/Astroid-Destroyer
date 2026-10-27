import pygame
import random

pygame.init()

WINDOW_WIDTH = 1080
WINDOW_HEIGHT  = 720
PLAYER_DIRECTION = pygame.math.Vector2(1,-1)
PLAYER_SPEED = 200
display_surface = pygame.display.set_mode((WINDOW_WIDTH ,WINDOW_HEIGHT ))
pygame.display.set_caption("Astroid Destroyer")
sprite_sheet = pygame.image.load("resources/assets-bck.png")
#star_sheet = pygame.image.load("resources/stars.png")

laser_surf = pygame.image.load("resources/laser4.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft= (20, WINDOW_HEIGHT -20))
star_surface = pygame.image.load("resources/star_base.png").convert_alpha()
astroid_surf = sprite_sheet.subsurface(13,274,200,200).convert_alpha()
astroid_rect = astroid_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
#star_example = star_sheet.subsurface(886, 3, 223, 220)
player_surf = sprite_sheet.subsurface(15,10,135,134).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2+50,WINDOW_HEIGHT/2+80))

                         
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]
# expression for value in iterable if condition
running = True
clock = pygame.time.Clock()
#surf = pygame.Surface((100,200))
#surf.fill("azure")

x = 100
while running:
    dt = clock.tick(30)/1000
    print(dt)
    print(clock.get_fps())
    #event loop
    for event in pygame.event.get():
        if event.type == 256:
            running = False

    #draw the game
    display_surface.fill("black")
    
    #draw stars
    for pos in star_positions: 
        display_surface.blit(star_surface,pos)

    display_surface.blit(astroid_surf, astroid_rect)
    display_surface.blit(laser_surf, laser_rect)

    #player movement
    player_rect.center += PLAYER_DIRECTION * PLAYER_SPEED * dt
    

    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0 :
        PLAYER_DIRECTION.x *= -1
    if player_rect.top <0 or player_rect.bottom > WINDOW_HEIGHT:
        PLAYER_DIRECTION.y *= -1

    
    
    display_surface.blit(player_surf, player_rect)
    
    pygame.display.flip()


pygame.quit()
        
#surface = image in memory


