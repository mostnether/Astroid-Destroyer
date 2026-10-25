import pygame

pygame.init()
display_surface = pygame.display.set_mode((640,640))
pygame.display.set_caption("Astroid Destroyer")
running = True
surf = pygame.Surface((100,200))
surf.fill("azure")

x = 100
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == 256:
            running = False

    #draw the game
    display_surface.fill("darkgray")
    surf.fill("orange")
    display_surface.blit(surf,(x,150))
    x+=0.5
    pygame.display.flip()


pygame.quit()
        
#surface = image in memory

