import random

from pygame.math import Vector2

import core
import epidemie
from Agent import Agent
from Body import Body



class Environnement:
    def __init__(self):
        self.L = core.WINDOW_SIZE[0]
        self.H = core.WINDOW_SIZE[1]
        self.listAgent = []


    def computePerception(self):
        for agent in self.listAgent:
            agent.listPerception = []
            for a in self.listAgent:
                if agent.body.fustrum.inside(a.body.position) and a.uuid != agent.uuid:
                    agent.listPerception.append(a)

    def computeDecision(self):
        for agent in self.listAgent:
            agent.doDecision()

    def applyDecision(self):
        for agent in self.listAgent:
            agent.body.update(epidemie.epidemie_params)
            agent.update()


    def show(self):
        for agent in self.listAgent:
            agent.show()


    def addAgent(self, agent):
        self.listAgent.append(agent)



    def addRandomAgents(self, n):
        size = 10
        for i in range(n):
            a = Agent(Body(Vector2(random.randint(size, self.L-size), random.randint(size, self.H-size)), size,"S"), "S")
            self.listAgent.append(a)
        i=Agent(Body(Vector2(random.randint(size, self.L-size), random.randint(size, self.H-size)), size,"I"), "I")
        self.listAgent.append(i)

    def delAgent(self, agent):
        self.listAgent.remove(agent)

