import random

from pygame.math import Vector2

import epidemie


class Agent:
    def __init__(self,body,statut):
        self.uuid = random.randint(0, 1000000)
        self.body = body
        self.listPerception = []
        self.statut=statut

    def filtrePerception(self, listPerception, epidemie_params):
        infectes = []
        for p in listPerception:
            if isinstance(p, Agent):
                distance = self.body.position.distance_to(p.body.position)
                if p.statut == "I":
                    if distance < epidemie_params["min_contagion_distance"]:
                        infectes.append(p)
        return infectes

    def doDecision(self):
        att = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        self.body.a = att
        infectes= self.filtrePerception(self.listPerception, epidemie.epidemie_params)
        if infectes is not None:
            self.body.update(epidemie.epidemie_params)

    def update(self):
        if self.body.is_contagious:
            self.statut="I"
    def show(self):
        if self.statut=="S":
            self.body.show((0, 0, 255))
        if self.statut=="I":
            self.body.show((255, 0, 0))
        if self.statut=="R":
            self.body.show((0, 255, 0))
        if self.statut=="D":
            self.body.show((255, 255, 255))
