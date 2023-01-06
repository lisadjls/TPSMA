from pygame.math import Vector2

import core
from Fustrum import Fustrum


class Body:
    def __init__(self, position, size, v=Vector2(0, 0), vmax=5, a=Vector2(0, 0), amax=5):
        self.position = position
        self.size = size
        self.v = v
        self.vmax = vmax
        self.a = a
        self.amax = amax
        self.fustrum = Fustrum(100, self)

    def applyDecision(self):
        if self.position[0]-self.size <= 0:
            self.position[0] = self.size
            self.v[0] *= -1
            self.a[0] *= -1
        if self.position[0] + self.size > core.WINDOW_SIZE[0]:
            self.position[0] = core.WINDOW_SIZE[0] - self.size
            self.v[0] *= -1
            self.a[0] *= -1

        if self.position[1]-self.size <= 0:
            self.position[1] = self.size
            self.v[1] *= -1
            self.a[1] *= -1
        if self.position[1] + self.size > core.WINDOW_SIZE[1]:
            self.position[1] = core.WINDOW_SIZE[1] - self.size
            self.v[1] *= -1
            self.a[1] *= -1

        if self.a.length() > self.amax:
            self.a.scale_to_length(self.amax)
        self.v += self.a
        if self.v.length() > self.vmax:
            self.v.scale_to_length(self.vmax)
        self.position += self.v



    def show(self, color):
        core.Draw.circle((color), self.position, self.size)

