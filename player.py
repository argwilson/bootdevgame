from circleshape import *
from constants import *
from bullet import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0.0
        self.velocity = 0 * pygame.Vector2(0, 1).rotate(self.rotation)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt

    def move(self, dt):
        self.position += self.velocity * dt
        if self.velocity.length() >= PLAYER_SPEED:
            self.velocity *= PLAYER_SPEED/self.velocity.length()

    def shoot(self, position, rotation):
        new_shot = Bullet(position.x, position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), width = 2)
    
    def update(self, dt):
        self.move(dt)

        if self.timer > 0:
            self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return self.rotate(-dt)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        
        if keys[pygame.K_s]:
            return self.accelerate(-dt)
        if keys[pygame.K_w]:
            return self.accelerate(dt)
        
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                return
            self.timer = PLAYER_SHOOT_COOLDOWN
            return self.shoot(self.position, self.rotation)
        
        if self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT