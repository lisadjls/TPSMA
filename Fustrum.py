from pygame.math import Vector2


class Fustrum:
    def __init__(self, rayon, parent):
        self.rayon = rayon
        self.parent = parent

    def inside(self, position):
        if isinstance(position, Vector2):
            return position.distance_to(self.parent.position) < self.rayon
