import pygame

def run(screen):                   
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Título do jogo - pressione enter para começar', False, (255, 0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return {"sair":True}

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                
        screen.fill((0,0,0))

        screen.blit(text_surface, (0,0))


        pygame.display.flip()
    return {
        "volume":1,
        # outras configs
    }

