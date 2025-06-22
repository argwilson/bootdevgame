from circleshape import *
from constants import *
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self, radius, position, velocity):
        self.kill()
        if radius <= ASTEROID_MIN_RADIUS:
            return
        return self.spawn(radius, position, velocity)
        
    def spawn(self, radius, position, velocity):
        random_angle = uniform(20, 50)
        vel_1 = velocity.rotate(random_angle)
        vel_2 = velocity.rotate(-random_angle)
        new_radius = radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(position.x, position.y, new_radius)
        asteroid_2 = Asteroid(position.x, position.y, new_radius)
        asteroid_1.velocity = vel_1 * 1.2
        asteroid_2.velocity = vel_2 * 1.2

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        return self.position