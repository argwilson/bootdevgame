import pygame

# Base class for game objects
class LineShape(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y) # center of object
        self.velocity = pygame.Vector2(0, 0)
        self.scale = scale # scale factor

    #def collision(self, target):
        #if self.position.distance_to(target.position) <= self.radius + target.radius:
            #return True
        #return False

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass