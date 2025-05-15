import pygame

# Contagem de quantos objetos pediram para mudar o cursor para pointer.
# Se houver ao menos um, deve renderizar como pointer
pointer_count = 0


def set_pointer():
    global pointer_count
    pointer_count += 1
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


def reset_pointer():
    global pointer_count
    pointer_count = max(0, pointer_count - 1)
    if not pointer_count:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
