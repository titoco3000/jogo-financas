from .gameobject import GameObject
import pygame


class Text(GameObject):
    def __init__(
        self,
        rect: pygame.rect.Rect,
        text: str,
        color=(255, 255, 255),
        font=None,
    ):
        super().__init__("text")
        self.rect = rect
        self.text = text
        self.color = color

        if font is None:
            self.font = pygame.font.SysFont(None, 24)  # fonte e tamanho default
        else:
            self.font = font

        self._render_text_lines()

    def _render_text_lines(self):
        """Prepara text surfaces para cada linha"""
        self.text_surfaces = []
        lines = self.text.split("\n")
        for line in lines:
            surface = self.font.render(line, True, self.color)
            self.text_surfaces.append(surface)

    def draw(self, screen):
        total_text_height = sum(surface.get_height() for surface in self.text_surfaces)
        current_y = self.rect.centery - total_text_height // 2
        for surface in self.text_surfaces:
            text_x = self.rect.centerx - surface.get_width() // 2
            screen.blit(surface, (text_x, current_y))
            current_y += surface.get_height()

    def set_text(self, new_text):
        """Muda texto dinamicamente e re-renderiza"""
        self.text = new_text
        self._render_text_lines()
