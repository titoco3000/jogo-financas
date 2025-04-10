import pygame

def run(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {"sair":True}
                
        screen.fill((0,0,0))

        pygame.display.flip()

