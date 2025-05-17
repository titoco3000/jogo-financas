from .gameobject import GameObject
from .text import Text

from src.globals import utils, cursor
import pygame
from typing import Callable


class Botao(GameObject):
    def __init__(
        self,
        rect: pygame.rect.Rect,
        text: str,
        on_click: Callable = None,
        radius=0,
        background=(255, 255, 255),
        border_color=(0, 0, 0),
        text_color=(0, 0, 0),
        hover_color=None,
        border_width=1,
        font=None,
    ):
        super().__init__("botao")
        self.rect = rect
        self.on_click = on_click
        self.radius = radius
        self.background = background
        self.draw_color = background
        self.border_color = border_color
        self.border_width = border_width

        if hover_color is None:
            self.hover_color = utils.lerp(background, border_color, 0.1)
        else:
            self.hover_color = hover_color

        self.text_element = Text(rect, text, text_color, font)

        self._mouse_inside = False  # <- controla se o mouse está dentro

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mouse_is_inside = self.rect.collidepoint(mouse_pos)

        if mouse_is_inside and not self._mouse_inside:
            cursor.set_pointer()
            self._mouse_inside = True
        elif not mouse_is_inside and self._mouse_inside:
            cursor.reset_pointer()
            self._mouse_inside = False

        if mouse_is_inside:
            if self.hover_color:
                self.draw_color = utils.lerp(self.draw_color, self.hover_color, 0.02)

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.on_click:
                        self.on_click()
        elif self.hover_color:
            self.draw_color = utils.lerp(self.draw_color, self.background, 0.05)

    def draw(self, screen):
        # Desenha background
        pygame.draw.rect(screen, self.draw_color, self.rect, border_radius=self.radius)
        if self.border_width > 0:
            pygame.draw.rect(
                screen,
                self.border_color,
                self.rect,
                width=self.border_width,
                border_radius=self.radius,
            )

    def set_text(self, new_text):
        self.text_element.set_text(new_text)

    def __del__(self):
        if self._mouse_inside:
            cursor.reset_pointer()
        super().__del__()
