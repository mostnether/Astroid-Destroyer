import pygame
import random

pygame.init()

WINDOW_WIDTH = 1080
WINDOW_HEIGHT  = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH ,WINDOW_HEIGHT ))
pygame.display.set_caption("Astroid Destroyer")
sprite_sheet = pygame.image.load("resources/assets-bck.png")
#star_sheet = pygame.image.load("resources/stars.png")
star_surface = pygame.image.load("resources/star_base.png").convert_alpha()
#star_example = star_sheet.subsurface(886, 3, 223, 220)
player_sprite = sprite_sheet.subsurface(15,10,135,134).convert_alpha()


                         
star_positions = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(20)]
# expression for value in iterable if condition
running = True
#surf = pygame.Surface((100,200))
#surf.fill("azure")

x = 100
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == 256:
            running = False

    #draw the game
    display_surface.fill("black")
    #surf.fill("orange")
    for pos in star_positions: 
        display_surface.blit(star_surface,pos)
    
    display_surface.blit(player_sprite,(x,150))
    x+=0.5
    pygame.display.flip()


pygame.quit()
        
#surface = image in memory


