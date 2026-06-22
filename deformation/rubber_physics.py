import math

class RubberPhysics:
    def __init__(self, stiffness=0.1, damping=0.8):
        self.stiffness = stiffness
        self.damping = damping
        self.velocity = 0


    def update(self, current_pos, target_pos):
        """
        Spring physics for smooth deformation
        """

        force = (target_pos - current_pos) * self.stiffness
        self.velocity = (self.velocity + force) * self.damping

        new_pos = current_pos + self.velocity

        return new_pos