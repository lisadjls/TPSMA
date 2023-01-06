import random

from pygame.math import Vector2

import core
from Fustrum import Fustrum


class Body:
    def __init__(self, position, size, statut, v=Vector2(0, 0), vmax=5, a=Vector2(0, 0), amax=5):
        self.position = position
        self.size = size
        self.v = v
        self.vmax = vmax
        self.a = a
        self.amax = amax
        self.fustrum = Fustrum(200, self)
        self.statut= statut
        self.infection_time = 0
        self.is_contagious = False

    def update(self, params):
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
        if self.a != Vector2(0, 0):
            self.v = self.a
        if self.v.length() > self.vmax:
            self.v.scale_to_length(self.vmax)
        self.position += self.v
        self.a=Vector2(0,0)

        if self.statut == "S":
            if random.random() < params["contagion_probability"]:
                self.statut = "I"
                self.infection_time = 0
            elif self.statut == "I":
                if self.infection_time > params["incubation_duration"]:
                    self.is_contagious = True
                if self.infection_time >params["death_duration"]:
                    if random.random() < params["mortality_probability"]:
                        self.statut = "D"
                    else:
                        self.statut = "R"
                self.infection_time += 1


    def show(self, color):
        core.Draw.circle((color), self.position, self.size)

