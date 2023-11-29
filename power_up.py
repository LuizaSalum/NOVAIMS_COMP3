import pygame
from abc import ABC, abstractmethod
import random

class PowerUp(ABC, pygame.sprite.Sprite):

    def __init__(self, powerup_image, width, height, base_speed=0, duration=0, cooldown=0):
        super().__init__()

        self.width = width
        self.height = height
        self.duration = duration
        self.cooldown = cooldown
        self.base_speed = base_speed
        self.active = False
        self.timer = 0
        self.cooldown_timer = 0

        self.image = pygame.image.load(powerup_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.x = 0  # Set the initial x-coordinate
        self.rect.y = 0  # Set the initial y-coordinate

    def deactivate(self):
        self.active = False
        self.cooldown_timer = self.cooldown

    def update(self, all_sprites_list):
        if self.active:
            self.timer += 1
            if self.timer == self.duration:
                self.deactivate()

        elif self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            if self.cooldown_timer == 0:
                self.rect.x = random.choice([285, 466, 643, 825])
                self.rect.y = random.randint(-1500, -100)
                all_sprites_list.add(self)
    
    def move_down(self, pixels):
        pixels = self.base_speed + pixels
        self.rect.y += pixels

    @abstractmethod
    def affect_player(self, player):
        pass
    
    @abstractmethod
    def affect_traffic(self, traffic):
        pass

    @abstractmethod
    def affect_both_players(self, lolly, bestie):
        pass

class BestiesInHarmony(PowerUp): # the player can pass through the other player
    def __init__(self):
        super().__init__("images/power_ups/besties_in_harmony.png", 80, 80, 3, 120, 120) # since the game is set to 60 fps, 120 frames = 2 seconds

    def affect_both_players(self, lolly, bestie): # the player can pass through the other player
        lolly.collide_with_player = False
        bestie.collide_with_player = False
        
class DivaDefiance(PowerUp): # The player can pass through traffic cars
    def __init__(self):
        super().__init__("images/power_ups/diva_defiance.png", 80, 80, 3, 120, 120)

    def affect_traffic(self, traffic):
        for car in traffic:
            car.collide_with_player = False

class FrostyFrenzy(PowerUp): # incoming cars get slower
    def __init__(self):
        super().__init__("images/power_ups/frosty_frenzy.png", 80, 80, 3, 120, 120)

    def affect_traffic(self, traffic):
        for car in traffic:
            car.speed = 1

class GalPalRebirth(PowerUp): # Player gets revived
    def __init__(self):
        super().__init__("images/powerups/gal_pal_rebirth.png", 80, 80, 3, 120, 120)

    def affect_both_players(self, lolly, bestie):
        if lolly.health == 0:
            lolly.health = 1
        if bestie.health == 0:
            bestie.health = 1

class TangledTwist(PowerUp): # the player gets the other player's controls
    def __init__(self):
        super().__init__("images/power_ups/tangled_twist.png", 80, 80, 3, 120, 120)

    def affect_both_players(self, lolly, bestie):
        lolly.left = bestie.left
        lolly.right = bestie.right
        lolly.up = bestie.up
        lolly.down = bestie.down

        bestie.left = lolly.left
        bestie.right = lolly.right
        bestie.up = lolly.up
        bestie.down = lolly.down

class GlamorousGrowth(PowerUp): # the player gets bigger and gains hp (+2 if it's the tank car, +1 if it's one of the others)
    def __init__(self):
        super().__init__("images/power_ups/glamorous_growth.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        player.width = 100
        player.height = 100
        player.image = pygame.image.load("images/cars/glamorous_growth.png").convert_alpha()
        player.image = pygame.transform.scale(player.image, (player.width, player.height))

class SissyThatWalk(PowerUp): # the player gets a speed boost
    def __init__(self):
        super().__init__("images/power_ups/sissy_that_walk.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        player.speed = 10        

class ToyTransforminator(PowerUp): # the traffic cars get smaller
    def __init__(self):
        super().__init__("images/power_ups/toy_transforminator.png", 80, 80, 3, 120, 120)

    def affect_traffic(self, traffic):
        for car in traffic:
            car.width = 50
            car.height = 50
            car.image = pygame.image.load("images/cars/toy_car.png").convert_alpha()
            car.image = pygame.transform.scale(car.image, (car.width, car.height))
