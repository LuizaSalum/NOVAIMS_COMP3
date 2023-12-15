import pygame
import random
from abc import ABC, abstractmethod


class PowerUp(ABC, pygame.sprite.Sprite):

    """
    Represents a power-up in the game.

    Parameters
    ----------
    image_path : str
        The path to the image file of the power-up.
    difficulty : int
        The difficulty level of the power-up.
    speed : int, optional
        The speed of the power-up. Defaults to 10.
    duration : int, optional
        The duration of the power-up. Defaults to 0.
    cooldown : int, optional
        The cooldown of the power-up. Defaults to 0.

    Attributes
    ----------
    image : pygame.Surface
        The image of the power-up.
    rect : pygame.Rect
        The rectangle that encloses the power-up.
    mask : pygame.Mask
        The mask of the power-up.
    speed : int
        The speed of the power-up.
    duration : int
        The duration of the power-up.
    cooldown : int
        The cooldown of the power-up.
    max_duration : int
        The maximum duration of the power-up.
    active : bool
        Whether the power-up is active.
    on_cooldown : bool
        Whether the power-up is on cooldown.
    can_move : bool
        Whether the power-up can move.

    Methods
    -------
    move_down()
        Moves the power-up down.
    add_speed(speed)
        Adds the given speed to the power-up.
    add_cooldown(cooldown)
        Adds the given cooldown to the power-up.
    add_duration(duration)
        Adds the given duration to the power-up.
    set_position(x, y)
        Sets the position of the power-up to the given coordinates.
    hide()
        Hides the power-up.
    collision()
        Handles the collision of the power-up.
    add_cooldown_prob()
        Adds a random cooldown to the power-up.
    affect_both_players(lolly, bestie)
        Affects both players.
    affect_player(player)
        Affects the given player.
    affect_traffic(traffic_group)
        Affects the given traffic group.
    """

    def __init__(self, image_path, difficulty, speed=10, duration=0, cooldown=0):
        super().__init__()

        self.difficulty = difficulty

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed
        self.duration = duration
        self.cooldown = cooldown
        self.max_duration = duration

        self.active = False
        self.on_cooldown = True  # if the power up is on cooldown
        self.can_move = True  # if the power up can move
        
    def move_down(self):
        if self.can_move:  # if the power up can move, it will move down
            self.rect.y += self.speed
            
    def add_speed(self, speed):
        self.speed += speed

    def add_cooldown(self, cooldown):
        self.cooldown += cooldown

    def add_duration(self, duration):
        self.duration += duration

    def set_position(self, x, y):
        self.can_move = True  # if the power up is set in a new position, it can move
        self.rect.x = x
        self.rect.y = y
       
    def hide(self):
        self.can_move = False  # if the power up is hidden, it can't move
        self.rect.x = -1000  # the power up will be hidden outside the screen

    @abstractmethod
    def collision(self):  # this method will be called when the power up collides with a player car
        self.active = True  # the power up will be active after the collision
        # self.on_cooldown = False # the power up will be off cooldown after the collision

        if self.active or self.on_cooldown:  # if the power up is on cooldown, it will be hidden
            self.hide()
        else:  # if the power up is not on cooldown, it will be placed in a random lane
            self.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))

        '''
        We will do customised cooldowns and durations according to the player car
        The car 1 has different cooldowns and durations than the car 2 and 3
        This will be done in the child classes, because some are buffs and others are debuffs
        '''

    @abstractmethod
    def add_cooldown_prob(self):
        self.on_cooldown = True  # the power up is on cooldown

    @abstractmethod
    def affect_both_players(self, lolly, bestie):
        pass

    @abstractmethod
    def affect_player(self, player):
        pass

    @abstractmethod
    def affect_traffic(self, traffic_group):
        pass

''' Power Ups that affect both players '''

class BestiesInHarmony(PowerUp):  # Players can't collide with each other

    def __init__(self, difficulty):
        super().__init__('images/power_ups/besties_in_harmony.png', difficulty, 10, 120, random.randint(100, 500))  # speed, duration and cooldown of the power up. for the last two, 60 = 1 second because of the FPS

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)  # - 1 second
            self.add_duration(120)  # + 2 seconds

    def deactivate(self, lolly, bestie):
        self.active = False
        self.duration = self.max_duration # Reset duration to ensure it starts from the beginning
        lolly.can_collide = True
        bestie.can_collide = True

    def collision(self, lolly, bestie):
        super().collision()  # calling the parent class' collision method

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':  # if the player has the car with the power ups buff
            self.add_duration(60)
            self.add_cooldown(-40)

        self.affect_both_players(lolly, bestie)  # calling the method that will affect both players

    def add_cooldown_prob(self): 
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method
        
        self.cooldown = random.randint(300, 500)  # the cooldown will be a random value between 50 and 100
    
    def affect_both_players(self, lolly, bestie):
        lolly.can_collide = False
        bestie.can_collide = False

    def affect_player(self):
        pass

    def affect_traffic(self):
        pass

class GalPalRebirth(PowerUp):  # Eliminated player gets revived

    def __init__(self, difficulty):
        super().__init__('images/power_ups/gal_pal_rebirth.png', difficulty, 10, 0, 60)

        if difficulty == 'easy':
            self.add_cooldown(-60)
    
    def add_cooldown_prob(self): 
        self.cooldown = random.randint(50, 100)  # the cooldown will be a random value between 50 and 100
    
    def collision(self, lolly, bestie):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(-12)

        self.affect_both_players(lolly, bestie)
    
    def add_cooldown_prob(self):
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method

        self.cooldown = random.randint(50, 100)  # the cooldown will be a random value between 50 and 100

    def affect_both_players(self, lolly, bestie):  # if the players are eliminated, they will be revived
        if lolly.eliminated:
            lolly.respawn()
        elif bestie.eliminated:
            bestie.respawn()

    def affect_player(self):
        pass

    def affect_traffic(self):
        pass

class TangledTwist(PowerUp):  # Players get tangled and their controls are inverted, this is done in the game file

    def __init__(self, difficulty):
        super().__init__('images/power_ups/tangled_twist.png', difficulty, 10, 100, random.randint(100, 500))

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(60)
            self.add_duration(-40)

    def deactivate(self, lolly, bestie):
        self.active = False
        self.duration = self.max_duration # Reset duration to ensure it starts fresh
        lolly.controls_inverted = False
        bestie.controls_inverted = False

    def collision(self, lolly, bestie):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(120)
            self.add_duration(-20)

        self.affect_both_players(lolly, bestie)   

    def add_cooldown_prob(self): 
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method

        self.cooldown = random.randint(50, 100)  # the cooldown will be a random value between 50 and 100

    def add_cooldown_prob(self):
        self.on_cooldown = True  # the power up is on cooldown 
        self.cooldown = random.randint(300, 500)  # the cooldown will be a random value between 50 and 100

    def affect_both_players(self, lolly, bestie):
        lolly.controls_inverted = True
        bestie.controls_inverted = True

    def affect_player(self):
        pass

    def affect_traffic(self):
        pass

class SissyThatWalk(PowerUp):  # Players get a speed buff

    def __init__(self, difficulty):
        super().__init__('images/power_ups/sissy_that_walk.png', difficulty, 10, 110, random.randint(100, 500))

        if difficulty == 'easy':
            self.add_cooldown(-60)
            self.add_duration(80)

    def deactivate(self, lolly, bestie = None):
        self.active = False
        self.duration = self.max_duration # Reset duration to ensure it starts fresh

        if bestie != None:
            lolly.add_speed(-5)
            bestie.add_speed(-5)
        else:
            lolly.add_speed(-5)

    def collision(self, lolly, bestie = None):
        super().collision()

        if bestie != None:
            if lolly.car_type == 'car1' or bestie.car_type == 'car1':  # if the player has the car with the power ups buff
                self.add_duration(120)
                self.add_cooldown(-120)
            self.affect_both_players(lolly, bestie)
        else:
            if lolly.car_type == 'car1':
                self.add_duration(120)
                self.add_cooldown(120)
            self.affect_player(lolly)
    
    def add_cooldown_prob(self): 
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method        

        self.cooldown = random.randint(200, 400)  # the cooldown will be a random value between 50 and 100

    def affect_both_players(self, lolly, bestie):
        lolly.add_speed(5)
        bestie.add_speed(5)

    def affect_player(self, player):
        player.add_speed(5)

    def affect_traffic(self):
        pass

''' Power Ups that affect only one player '''

class DivaDefiance(PowerUp):  # Player can't crash with traffic (invincibility)

    def __init__(self, difficulty):
        super().__init__('images/power_ups/diva_defiance.png', difficulty, 10, 80, random.randint(100, 500))
        self.active_lolly = False
        self.active_bestie = False

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-120)
            self.add_duration(60)
    
    def deactivate(self, name, player_that_collided):
        self.active = False

        if name == 'lolly':
            self.active_lolly = False
        elif name == 'bestie':
            self.active_bestie = False

        self.duration = self.max_duration # Reset duration to ensure it starts fresh
        player_that_collided.can_crash = True


    def collision(self, name, player_that_collided):
        super().collision()

        if name == 'lolly':
            self.active_lolly = True
        elif name == 'bestie':
            self.active_bestie = True

        if player_that_collided.car_type == 'car1':
            self.add_cooldown(-20)
            self.add_duration(20)

        self.affect_player(player_that_collided)
    
    def add_cooldown_prob(self): 
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method

        self.cooldown = random.randint(300, 500)  # the cooldown will be a random value between 50 and 100

    def affect_both_players(self):
        pass

    def affect_player(self, player):
        player.can_crash = False

    def affect_traffic(self):
        pass

class GlamorousGrowth(PowerUp):  # Player gets a health buff and grows in size

    def __init__(self, difficulty):
        super().__init__('images/power_ups/glamorous_growth.png', difficulty, 10, 80, random.randint(100, 500))
        self.active_lolly = False
        self.active_bestie = False

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(60)

    def deactivate(self, name, player_that_collided):
        self.active = False

        if name == 'lolly':
            self.active_lolly = False
        elif name == 'bestie':
            self.active_bestie = False

        self.duration = self.max_duration # Reset duration to ensure it starts fresh
        player_that_collided.resize_car(0.5)

    def collision(self, name, player_that_collided):
        super().collision()

        if name == 'lolly':
            self.active_lolly = True
        elif name == 'bestie':
            self.active_bestie = True

        if player_that_collided.car_type == 'car1':
            self.add_cooldown(-120)
            self.add_duration(60)

        self.affect_player(player_that_collided)
    
    def add_cooldown_prob(self): 
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method

        self.cooldown = random.randint(200, 400)  # the cooldown will be a random value between 50 and 10

    def affect_both_players(self):
        pass

    def affect_player(self, player):  # the player will grow in size and get an extra health point, the size growth is done in the game file
        player.add_health(1)
    
    def affect_traffic(self):
        pass

''' Power Ups that affect the traffic '''

class FrostyFrenzy(PowerUp):  # Traffic gets slowed down

    def __init__(self, difficulty):
        super().__init__('images/power_ups/frosty_frenzy.png', difficulty, 10, 90, random.randint(100, 500))

        self.difficulty = difficulty
        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(120)

    def deactivate(self, traffic_group=None, traffic_group_left=None, traffic_group_right=None):
        self.active = False
        self.duration = self.max_duration # Reset duration to ensure it starts fresh

        if self.difficulty != 'hard':
            for car in traffic_group:
                car.add_speed(2)

        elif self.difficulty == 'hard':
            for car in traffic_group_left:
                car.add_speed(2)
            for car in traffic_group_right:
                car.add_speed(2)

    def collision(self, lolly, bestie= None, traffic_group=None, traffic_group_left=None, traffic_group_right=None):
        super().collision()                        

        if bestie != None:
            if lolly.car_type == 'car1' or bestie.car_type == 'car1':  # if the player has the car with the power ups buff
                self.add_duration(60)
                self.add_cooldown(-120)
        else:
            if lolly.car_type == 'car1':
                self.add_duration(60)
                self.add_cooldown(-120)

        if self.difficulty != 'hard':
            self.affect_traffic(traffic_group)

        elif self.difficulty == 'hard':
            self.affect_traffic(traffic_group_left)
            self.affect_traffic(traffic_group_right)
        
    def add_cooldown_prob(self): 
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method

        self.cooldown = random.randint(300, 500)  # the cooldown will be a random value between 50 and 100

    def affect_both_players(self):
        pass

    def affect_player(self):
        pass

    def affect_traffic(self, traffic_group):
        for car in traffic_group:
            car.add_speed(-2)

class ToyTransforminator(PowerUp):  # Traffic decreases in size

    def __init__(self, difficulty):
        super().__init__('images/power_ups/toy_transforminator.png', difficulty, 10, 120, random.randint(100, 500))

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(120)

    def deactivate(self, traffic_group=None, traffic_group_left=None, traffic_group_right=None):
        self.active = False
        self.duration = self.max_duration # Reset duration to ensure it starts fresh

        if self.difficulty != 'hard':
            for car in traffic_group :
                car.resize_car(1)

        elif self.difficulty == 'hard':
            for car in traffic_group_left:
                car.resize_car(1)
            for car in traffic_group_right:
                car.resize_car(1)

    def collision(self, lolly, bestie= None, traffic_group=None, traffic_group_left=None, traffic_group_right=None):
        super().collision()

        if bestie != None:
            if lolly.car_type == 'car1' or bestie.car_type == 'car1':
                self.add_cooldown(-100)
                self.add_duration(120)
        else:
            if lolly.car_type == 'car1':
                self.add_cooldown(-100)
                self.add_duration(120)

        if self.difficulty != 'hard':
            self.affect_traffic(traffic_group)

        elif self.difficulty == 'hard':

            self.affect_traffic(traffic_group_left)
            self.affect_traffic(traffic_group_right)
    
    def add_cooldown_prob(self):
        super().add_cooldown_prob()  # calling the parent class' add_cooldown_prob method

        self.cooldown = random.randint(300, 400)  # the cooldown will be a random value between 50 and 100

    def affect_both_players(self):
        pass

    def affect_player(self):
        pass

    def affect_traffic(self, traffic_group):
        for car in traffic_group:
            car.resize_car(0.75)