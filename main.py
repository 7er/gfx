import pygame
from pygame.locals import *
import math

pygame.init()

def floatrange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step


class Plane:
    def __init__(self, surface):
        self._surface = surface
        self._height = surface.get_height()
        self._width = surface.get_width()
    
    def put_pixel(self, x, y):
        x, y = int(round(x)), int(round(y))
        self._surface.set_at((x, self._height - y), [0,0,0])

    def draw(self, function):
        scale = 3.0
        for x in floatrange(0, self._width, 1/scale):
            self.put_pixel(x * scale, function(x) * scale)


def main(screen):
    plane = Plane(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or getattr(event, 'key', None) == K_ESCAPE:
                return
        screen.fill([255, 255, 255])
        plane.draw(lambda x: x)
        pygame.display.flip()


screen = pygame.display.set_mode([480, 480])
main(screen)
