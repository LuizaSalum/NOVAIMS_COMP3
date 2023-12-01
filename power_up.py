import pygame
from abc import ABC, abstractmethod
import random

class PowerUp(ABC, pygame.sprite.Sprite):

    def __init__(self, powerup_image, width, height, duration=0, cooldown=0):
        super().__init__()

        self.width = width
        self.height = height
        self.duration = duration
        self.cooldown = cooldown
        self.base_speed = 3
        self.active = False
        self.timer = 0
        self.cooldown_timer = 0

        self.image = pygame.image.load(powerup_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.x = random.choice([285, 466, 643, 825])
        self.rect.y = random.randint(-1500, -100)

    def change_image(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def move_down(self, pixels):
        pixels = self.base_speed + pixels
        self.rect.y += pixels

    def add_speed(self, speed):
        self.base_speed += speed
    
    def add_cooldown(self, cooldown):
        self.cooldown += cooldown
    
    def add_duration(self, duration):
        self.duration += duration

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y 
   
    def remove_from_screen(self):
        self.rect.x = 400
        self.rect.y = -40000
        
    def collision_with_player(self):
        self.active = True
        self.remove_from_screen()

    def give_cooldown(self, cooldown):
        self.timer = 0
        self.cooldown = cooldown
    
    @abstractmethod
    def affect_player(self, player):
        pass
    
    @abstractmethod
    def affect_traffic(self, traffic):
        pass

    @abstractmethod
    def affect_both_players(self, lolly, bestie):
        pass

''' The following classes are the power ups that are available in the game. '''
class BestiesInHarmony(PowerUp):
    def __init__(self):
        super().__init__("images/power_ups/besties_in_harmony.png", 80, 80, 60,0)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        pass 

    def affect_both_players(self, lolly, bestie):
        lolly.collide_with_player = False
        bestie.collide_with_player = False
        
class DivaDefiance(PowerUp):
    def __init__(self):
        super().__init__("images/power_ups/diva_defiance.png", 80, 80, 60,0)

    def affect_player(self, player):    
        pass 

    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        lolly.collide_with_traffic = False
        bestie.collide_with_traffic = False
        
        
class FrostyFrenzy(PowerUp): # incoming cars get slower
    def __init__(self):
        super().__init__("images/power_ups/frosty_frenzy.png", 80, 80, 60,0)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        for car in traffic:
            car.speed = -6
    
    def affect_both_players(self, lolly, bestie):
        pass

class GalPalRebirth(PowerUp): # Player gets revived
    def __init__(self):
        super().__init__("images/power_ups/gal_pal_rebirth.png", 80, 80, 60,0)
    
    def affect_player(self, player):
        pass
        
    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        if lolly.health == 0:
            lolly.health = 1
            lolly.rect.x = 466
            lolly.rect.y = 800
            player_eliminated = False

        if bestie.health == 0:
            bestie.health = 1
            bestie.rect.x = 285
            bestie.rect.y = 800
            player_eliminated = False

class TangledTwist(PowerUp): # the player gets the other player's controls
    def __init__(self):
        super().__init__("images/power_ups/tangled_twist.png", 80, 80, 60,0)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie):
        pass

class GlamorousGrowth(PowerUp): # the player gets bigger and gains hp (+2 if it's the tank car, +1 if it's one of the others)
    def __init__(self):
        super().__init__("images/power_ups/glamorous_growth.png", 80, 80, 60,0)

    def affect_player(self, player):
        player.health += 1
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
        super().__init__("images/power_ups/sissy_that_walk.png", 80, 80, 60,0)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        pass

    def affect_both_players(self, lolly, bestie, speed):
        lolly.speed = speed
        bestie.speed = speed

class ToyTransforminator(PowerUp): # the traffic cars get smaller
    def __init__(self):
        super().__init__("images/power_ups/toy_transforminator.png", 80, 80, 60,0)

    def affect_player(self, player):
        pass

    def affect_traffic(self, traffic):
        for car in traffic:
            car.resize(0.8, 0.8)

    def affect_both_players(self, lolly, bestie):
        pass