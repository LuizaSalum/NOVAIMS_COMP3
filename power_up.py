import pygame

WHITE = (255, 255, 255)


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, powerup_image, width, height, speed=0, duration=0, cooldown=0):
        super().__init__()

        self.width = width
        self.height = height
        self.speed = speed
        self.duration = duration
        self.cooldown = cooldown

        self.image = pygame.image.load(powerup_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.x = 0  # Set the initial x-coordinate
        self.rect.y = 0  # Set the initial y-coordinate

    def move_down(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.y += pixels

    def add_duration(self, duration):
        self.duration += duration

    def add_cooldown(self, cooldown):
        self.cooldown += cooldown