import pygame
import random
from abc import ABC, abstractmethod


class PowerUp(ABC, pygame.sprite.Sprite):

    def __init__(self, image_path, speed=1, duration=0, cooldown=0):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed
        self.duration = duration
        self.cooldown = cooldown

        self.active = False
        self.on_cooldown = False
        self.unavailable = False
        self.can_move = True

        if self.on_cooldown or self.unavailable:
            self.hide()
        else:
            self.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))

    def move_down(self, speed_modifier=0):
        if self.can_move:
            self.rect.y += (self.speed + speed_modifier)

    def add_speed(self, speed):
        self.speed += speed

    def add_cooldown(self, cooldown):
        self.cooldown += cooldown

    def add_duration(self, duration):
        self.duration += duration

    def set_position(self, x, y):
        self.can_move = True
        self.rect.x = x
        self.rect.y = y

    def duration_timer(self):
        for duration_timer in range(self.duration, -1, -1):  # this is a countdown timer that will run for the duration of the power up
            if duration_timer == 0:
                self.active = False
                break
        
    def cooldown_timer(self):
        for cooldown_timer in range(self.cooldown, -1, -1):  # this is a countdown timer that will run for the cooldown of the power up
            if cooldown_timer == 0:
                self.on_cooldown = False
                break

    def hide(self):
        self.can_move = False
        self.rect.x = -1000

    @abstractmethod
    def collision(self):
        self.active = True
        self.on_cooldown = True

        '''
        We will do customised cooldowns and durations according to the player car
        The car 1 has different cooldowns and durations than the car 2 and 3
        This will be done in the child classes, because some are buffs and others are debuffs
        '''

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
        super().__init__('images/power_ups/besties_in_harmony.png', 1, 360, 600)  # speed, duration and cooldown of the power up. for the last two, 60 frames = 1 second

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)  # - 1 second
            self.add_duration(120)  # + 2 seconds

    def collision(self, lolly, bestie):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_duration(60)
            self.add_cooldown(-120)

        self.affect_both_players(lolly, bestie)
        self.duration_timer()
        if not self.active:
            lolly.can_collide = True
            bestie.can_collide = True
        self.cooldown_timer()

    def affect_both_players(self, lolly, bestie):
        lolly.can_collide = False
        bestie.can_collide = False

    def affect_player(self):
        pass

    def affect_traffic(self):
        pass

class GalPalRebirth(PowerUp):  # Eliminated player gets revived

    def __init__(self, difficulty):
        super().__init__('images/power_ups/gal_pal_rebirth.png', 1, 0, 1200)

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)

    def collision(self, lolly, bestie):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(-120)

        self.affect_both_players(lolly, bestie)
        self.duration_timer()
        self.cooldown_timer()

    def affect_both_players(self, lolly, bestie):
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
        super().__init__('images/power_ups/tangled_twist.png', 1, 360, 900)

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(60)
            self.add_duration(-120)

    def collision(self, lolly, bestie):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(120)
            self.add_duration(-60)

        self.affect_both_players(lolly, bestie)
        self.duration_timer()
        if not self.active:
            lolly.controls_inverted = False
            bestie.controls_inverted = False
        self.cooldown_timer()

    def affect_both_players(self, lolly, bestie):
        lolly.controls_inverted = True
        bestie.controls_inverted = True

    def affect_player(self):
        pass

    def affect_traffic(self):
        pass

class SissyThatWalk(PowerUp):  # Players get a speed buff

    def __init__(self, difficulty):
        super().__init__('images/power_ups/sissy_that_walk.png', 1, 300, 600)

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(120)

    def collision(self, lolly, bestie):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(-120)
            self.add_duration(120)

        self.affect_both_players(lolly, bestie)
        self.duration_timer()
        if not self.active:
            lolly.add_speed(-2)
            bestie.add_speed(-2)
        self.cooldown_timer()

    def affect_both_players(self, lolly, bestie):
        lolly.add_speed(2)
        bestie.add_speed(2)

    def affect_player(self):
        pass

    def affect_traffic(self):
        pass

''' Power Ups that affect only one player '''

class DivaDefiance(PowerUp):  # Player can't crash with traffic (invincibility)

    def __init__(self, difficulty):
        super().__init__('images/power_ups/diva_defiance.png', 1, 180, 900)

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-120)
            self.add_duration(60)

    def collision(self, player_that_collided):
        super().collision()

        if player_that_collided.car_type == 'car1':
            self.add_cooldown(-60)
            self.add_duration(60)

        self.affect_player(player_that_collided)
        self.duration_timer()
        if not self.active:
            player_that_collided.can_crash = True
        self.cooldown_timer()

    def affect_both_players(self):
        pass

    def affect_player(self, player):
        player.can_crash = False

    def affect_traffic(self):
        pass

class GlamorousGrowth(PowerUp):  # Player gets a health buff and grows in size

    def __init__(self, difficulty):
        super().__init__('images/power_ups/glamorous_growth.png', 1, 300, 600)

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(60)

    def collision(self, player_that_collided):
        super().collision()

        if player_that_collided.car_type == 'car1':
            self.add_cooldown(-120)
            self.add_duration(60)

        self.affect_player(player_that_collided)
        self.duration_timer()
        if not self.active:
            player_that_collided.size_increased = False
        self.cooldown_timer()

    def affect_both_players(self):
        pass

    def affect_player(self, player):
        player.add_health(1)
        player.size_increased = True

    def affect_traffic(self):
        pass

''' Power Ups that affect the traffic '''

class FrostyFrenzy(PowerUp):  # Traffic gets slowed down

    def __init__(self, difficulty):
        super().__init__('images/power_ups/frosty_frenzy.png', 1, 240, 600)

        self.difficulty = difficulty
        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(120)

    def collision(self, lolly, bestie, traffic_group=None, traffic_group_left=None, traffic_group_right=None):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(-120)
            self.add_duration(60)

        if self.difficulty != 'hard':
            self.affect_traffic(traffic_group)
            self.duration_timer()
            if not self.active:
                for car in traffic_group:
                    car.add_speed(2)
            self.cooldown_timer()

        elif self.difficulty == 'hard':

            self.affect_traffic(traffic_group_left)
            self.affect_traffic(traffic_group_right)
            self.duration_timer()
            if not self.active:
                for car in traffic_group_left:
                    car.add_speed(2)
                for car in traffic_group_right:
                    car.add_speed(2)
            self.cooldown_timer()

    def affect_both_players(self):
        pass

    def affect_player(self):
        pass

    def affect_traffic(self, traffic_group):
        for car in traffic_group:
            car.add_speed(-2)

class ToyTransforminator(PowerUp):  # Traffic decreases in size

    def __init__(self, difficulty):
        super().__init__('images/power_ups/toy_transforminator.png', 1, 300, 600)

        if difficulty == 'easy':
            self.add_speed(-1)
            self.add_cooldown(-60)
            self.add_duration(120)

    def collision(self, lolly, bestie, traffic_group=None, traffic_group_left=None, traffic_group_right=None):
        super().collision()

        if lolly.car_type == 'car1' or bestie.car_type == 'car1':
            self.add_cooldown(-120)
            self.add_duration(120)

        if self.difficulty != 'hard':
            self.affect_traffic(traffic_group)
            self.duration_timer()
            if not self.active:
                for car in traffic_group:
                    car.resize_car(2)
            self.cooldown_timer()

        elif self.difficulty == 'hard':

            self.affect_traffic(traffic_group_left)
            self.affect_traffic(traffic_group_right)
            self.duration_timer()
            if not self.active:
                for car in traffic_group_left:
                    car.resize_car(2)
                for car in traffic_group_right:
                    car.resize_car(2)
            self.cooldown_timer()

    def affect_both_players(self):
        pass

    def affect_player(self):
        pass

    def affect_traffic(self, traffic_group):
        for car in traffic_group:
            car.resize_car(0.5)