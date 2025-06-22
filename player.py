from circleshape import *
from constants import *
from bullet import *

class Player(CircleShape):
    timer = 0.0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, position, rotation):
        new_shot = Bullet(position.x, position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOT_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return self.rotate(-dt)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        
        if keys[pygame.K_s]:
            return self.move(-dt)
        if keys[pygame.K_w]:
            return self.move(dt)
        
        if keys[pygame.K_SPACE]:
            if Player.timer > 0:
                Player.timer -= dt
                return None
            Player.timer += PLAYER_SHOOT_COOLDOWN
            return self.shoot(self.position, self.rotation)
            