import core
from Environnement import Environnement


def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    env = Environnement()
    core.memory("env", env)

    env.addRandomAgents(10)



def run():
    core.cleanScreen()

    env: Environnement = core.memory("env")
    env.show()

    env.computePerception()
    env.computeDecision()
    env.applyDecision()


core.main(setup, run)
