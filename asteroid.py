import random
from circleshape import *
from explosions import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self, position, velocity, radius):
        self.kill()
        Explosion(position.x, position.y, 2*radius)
        if radius < ASTEROID_MIN_RADIUS:
            return
        return self.spawn(position, velocity, radius)
    
    def spawn(self, position, velocity, radius):
        angle = random.uniform(20,50)
        new_radius = radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(position.x, position.y, new_radius)
        asteroid_2 = Asteroid(position.x, position.y, new_radius)
        asteroid_1.velocity = velocity.rotate(angle) * 1.2
        asteroid_2.velocity = velocity.rotate(-angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)