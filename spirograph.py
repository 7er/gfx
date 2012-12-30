
import pygame, sys, math, time
from pygame.locals import *

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

def floatrange(start, stop, step):
    liste = []
    i = 0
    while start + step*i <= stop:
        liste.append(start + step*i)
        i += 1
    return liste


class Spirograph(object):
    @classmethod
    def wolfram(cls, R, r, a):
        k = r / R
        return cls(R, k, a / k)

    def __init__(self, R, k, l):
        self._R = R
        self._k = k
        self._l = l
        self._lk = self._l * self._k
        self._flipped_k = (1 - self._k)
        self._flipped_k_div_k = self._flipped_k / self._k

    def spiro_x(self, t):
        return self._R * (
            self._flipped_k * math.cos(t) + 
            self._lk * math.cos(self._flipped_k_div_k * t))

    def spiro_y(self, t):
        return self._R * (
            self._flipped_k * math.sin(t) - 
            self._lk * math.sin(self._flipped_k_div_k * t))


def put_pixel(x, y):
    screen.set_at((int(round(x)), int(round(height - y))), (0, 0, 0))

spirographs = [
    Spirograph.wolfram(each, each / 3.0, 0.45 + (index * 3 / 100.0))
    for index, each in enumerate(range(210, 100, -10))
    ]

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((255, 255, 255))
        begin = time.time()
        for t in floatrange(0, 8*math.pi, 0.005):
            for each in spirographs:
                put_pixel(each.spiro_x(t) + width / 2, each.spiro_y(t) + height / 2)
        print time.time() - begin
        pygame.display.flip()

main()

pygame.display.quit()

