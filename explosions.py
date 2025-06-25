import random
from lineshape import *
from asteroid import *
from constants import *

class Explosion(LineShape):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale)
        self.timer = 0.0

    def explosion(self):
        top = self.position + pygame.Vector2(1, 0) * self.scale
        upper_right = self.position + pygame.Vector2(1, 0).rotate(-72) * self.scale
        upper_left = self.position + pygame.Vector2(1, 0).rotate(72) * self.scale
        lower_right = self.position + pygame.Vector2(1, 0).rotate(-144) * self.scale
        lower_left = self.position + pygame.Vector2(1, 0).rotate(144) * self.scale
        return [top, lower_left, upper_right, upper_left, lower_right]

    def draw(self, screen):
        pygame.draw.lines(screen, "white", True, self.explosion(), width = 2)

    def update(self, dt):
        self.timer += dt
        if self.timer > EXPLOSION_LIFETIME:
            self.kill()
        
