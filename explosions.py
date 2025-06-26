import random
from lineshape import *
from asteroid import *
from constants import *

class Explosion(LineShape):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale)
        self.timer = 0.0

    def explosion(self):
        a = self.position + pygame.Vector2(1, 0) * self.scale * random.uniform(0.8, 1.2)
        b = self.position + pygame.Vector2(1, 0).rotate(36) * (self.scale/3) * random.uniform(0.8, 1.2)
        c = self.position + pygame.Vector2(1, 0).rotate(72) * self.scale * random.uniform(0.8, 1.2)
        d = self.position + pygame.Vector2(1, 0).rotate(108) * (self.scale/3) * random.uniform(0.8, 1.2)
        e = self.position + pygame.Vector2(1, 0).rotate(144) * self.scale * random.uniform(0.8, 1.2)
        f = self.position + pygame.Vector2(-1, 0) * (self.scale/3) * random.uniform(0.8, 1.2)
        g = self.position + pygame.Vector2(1, 0).rotate(-144) * self.scale * random.uniform(0.8, 1.2)
        h = self.position + pygame.Vector2(1, 0).rotate(-108) * (self.scale/3) * random.uniform(0.8, 1.2)
        i = self.position + pygame.Vector2(1, 0).rotate(-72) * self.scale * random.uniform(0.8, 1.2)
        j = self.position + pygame.Vector2(1, 0).rotate(-36) * (self.scale/3) * random.uniform(0.8, 1.2)
        return [a, b, c, d, e, f, g, h, i ,j]

    def draw(self, screen):
        pygame.draw.lines(screen, "white", True, self.explosion(), width = 2)

    def update(self, dt):
        self.timer += dt
        if self.timer > EXPLOSION_LIFETIME:
            self.kill()
        
