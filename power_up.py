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

        self.rect.x = random.choice([285, 466, 643, 825])
        self.rect.y = random.randint(-1500, -100)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y 

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

    def remove_from_screen(self):
        self.kill()
        self.rect.x = 400
        self.rect.y = -40000
    
    def move_down(self, pixels):
        pixels = self.base_speed + pixels
        self.rect.y += pixels

    def add_speed(self, speed):
        self.base_speed += speed
    
    def add_cooldown(self, cooldown):
        self.cooldown *= cooldown
    
    def add_duration(self, duration):
        self.duration *= duration
    

    @abstractmethod
    def affect_player(self, player):
        pass
    
    @abstractmethod
    def affect_traffic(self, traffic):
        pass

    @abstractmethod
    def affect_both_players(self, lolly, bestie):
        pass

class BestiesInHarmony(PowerUp):
    def __init__(self):
        super().__init__("images/power_ups/besties_in_harmony.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        player.collide_with_player = False

    def affect_traffic(self, traffic):
        pass  # BestiesInHarmony doesn't affect traffic, so this method can be empty

    def affect_both_players(self, lolly, bestie):
        lolly.collide_with_player = False
        bestie.collide_with_player = False
        
class DivaDefiance(PowerUp): # The player can pass through traffic cars
    def __init__(self):
        super().__init__("images/power_ups/diva_defiance.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):    
        pass 
    
    def affect_traffic(self, traffic):
        for car in traffic:
            car.collide_with_player = False

    def affect_both_players(self, lolly, bestie):
        pass
        
class FrostyFrenzy(PowerUp): # incoming cars get slower
    def __init__(self):
        super().__init__("images/power_ups/frosty_frenzy.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        for car in traffic:
            car.speed = 1
    
    def affect_both_players(self, lolly, bestie):
        pass

class GalPalRebirth(PowerUp): # Player gets revived
    def __init__(self):
        super().__init__("images/power_ups/gal_pal_rebirth.png", 80, 80, 3, 120, 120)
    
    def affect_player(self, player):
        pass
        
    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        if lolly.health == 0:
            lolly.health = 1
        if bestie.health == 0:
            bestie.health = 1

class TangledTwist(PowerUp): # the player gets the other player's controls
    def __init__(self):
        super().__init__("images/power_ups/tangled_twist.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        pass

class GlamorousGrowth(PowerUp): # the player gets bigger and gains hp (+2 if it's the tank car, +1 if it's one of the others)
    def __init__(self):
        super().__init__("images/power_ups/glamorous_growth.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        player.width = 100
        player.height = 100
        player.image = pygame.image.load("images/cars/glamorous_growth.png").convert_alpha()
        player.image = pygame.transform.scale(player.image, (player.width, player.height))

    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        pass

class SissyThatWalk(PowerUp): # the player gets a speed boost
    def __init__(self):
        super().__init__("images/power_ups/sissy_that_walk.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        player.speed = 10        

    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        pass

class ToyTransforminator(PowerUp): # the traffic cars get smaller
    def __init__(self):
        super().__init__("images/power_ups/toy_transforminator.png", 80, 80, 3, 120, 120)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        for car in traffic:
            car.width = 50
            car.height = 50
            car.image = pygame.image.load("images/cars/toy_car.png").convert_alpha()
            car.image = pygame.transform.scale(car.image, (car.width, car.height))

    def affect_both_players(self, lolly, bestie):
        pass