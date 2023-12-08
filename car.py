import pygame


class Car(pygame.sprite.Sprite):

    def __init__(self, image_path, speed=0, health=0):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()  # loading the image
        self.rect = self.image.get_rect()  # getting the rectangle of the image
        self.mask = pygame.mask.from_surface(self.image)  # creating a mask for collision detection
        
        self.speed = speed
        self.health = health

    def add_speed(self, speed):
        self.speed += speed

    def change_image(self, image_path):
        current_position = [self.rect.x, self.rect.y]  # storing the current position of the player car
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = current_position[0]  # replacing the player car in the stored position
        self.rect.y = current_position[1]

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

class PlayerCar(Car):

    def __init__(self, car_type, difficulty):

        if car_type == 'car1':
            image_path = 'images/players_cars/car1.png'
            speed = 13
            health = 3
            max_health = 4
        elif car_type == 'car2':
            image_path = 'images/players_cars/car2.png'
            speed = 16
            health = 2
            max_health = 3
        elif car_type == 'car3':
            image_path = 'images/players_cars/car3.png'
            speed = 10
            health = 4
            max_health = 5

        super().__init__(image_path, speed, health)

        self.car_type = car_type
        self.max_health = max_health

        self.can_collide = True  # this variable is used to check if the player car can collide with the other player (used for the Besties in Harmony Power Up)
        self.can_crash = True  # if the player car can crash with the traffic cars (used for the Diva Defiance Power Up)
        self.eliminated = False  # if the player car has been eliminated (used for the Gal Pal Rebirth Power Up)
        self.can_move = True  # if the player car can move (an eliminated player car can't move)
        self.controls_inverted = False  # if the controls are inverted (used for the Tangled Twist Power Up)

        if difficulty == 'easy':  # if the difficulty is easy, the player car will have an extra health point
            self.add_health(1)
        elif difficulty == 'hard':
            self.add_health(-1)

    # Movement functions for the player car

    def move_up(self):
        if self.can_move:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0

    def move_down(self):
        if self.can_move:
            self.rect.y += self.speed
            if self.rect.y > 950 - self.rect.height:
                self.rect.y = 950 - self.rect.height

    def move_left(self):
        if self.can_move:
            self.rect.x -= self.speed
            if self.rect.x < 272:
                self.rect.x = 272

    def move_right(self):
        if self.can_move:
            self.rect.x += self.speed
            if self.rect.x > 980 - self.rect.width:
                self.rect.x = 980 - self.rect.width

    # Other functions

    def add_health(self, health):
        if self.health < self.max_health:  # if the player car has not reached the maximum health points
            self.health += health

    def check_health(self):
        if self.health <= 0:  # if the player car has no health points left, we only added "less than" to make sure
            self.eliminated = True
            self.die()  # the die function will return the position of the player car so we can respawn it later

    def change_image(self, active_power_ups):  # this function will change the image of the player car according to the active power ups

        current_position = [self.rect.x, self.rect.y]  # storing the current position of the player car

        power_ups_images_paths = {
            'normal': f'images/players_cars/{self.car_type}.png',
            'besties': f'images/power_ups_visuals/besties/{self.car_type}_besties.png',
            'besties_tangled': f'images/power_ups_visuals/besties_tangled/{self.car_type}_besties_tangled.png',
            'besties_growth': f'images/power_ups_visuals/besties_growth/{self.car_type}_besties.png',
            'besties_tangled_growth': f'images/power_ups_visuals/besties_tangled_growth/{self.car_type}_besties_tangled.png',
            'besties_diva': f'images/power_ups_visuals/besties_diva/{self.car_type}_besties_diva.png',
            'besties_diva_tangled': f'images/power_ups_visuals/besties_diva_tangled/{self.car_type}_besties_diva_tangled.png',
            'besties_diva_growth': f'images/power_ups_visuals/besties_diva_growth/{self.car_type}_besties_diva.png',
            'besties_diva_tangled_growth': f'images/power_ups_visuals/besties_diva_tangled_growth/{self.car_type}_besties_diva_tangled.png',
            'tangled': f'images/power_ups_visuals/tangled/{self.car_type}_tangled.png',
            'growth': f'images/power_ups_visuals/growth/{self.car_type}.png',
            'tangled_growth': f'images/power_ups_visuals/tangled_growth/{self.car_type}_tangled.png',
            'diva': f'images/power_ups_visuals/diva/{self.car_type}_diva.png',
            'diva_tangled': f'images/power_ups_visuals/diva_tangled/{self.car_type}_diva_tangled.png',
            'diva_growth': f'images/power_ups_visuals/diva_growth/{self.car_type}_diva.png',
            'diva_tangled_growth': f'images/power_ups_visuals/diva_tangled_growth/{self.car_type}_diva_tangled.png'
        }

        image_path = power_ups_images_paths[active_power_ups]  # getting the image path from the dictionary
        super().change_image(image_path)  # changing the image using the parent class' function

        self.rect.x = current_position[0]  # replacing the player car in the stored position
        self.rect.y = current_position[1]
        
    def die(self):  # this function will be called when the player car dies
        stored_position = [self.rect.x, self.rect.y]  # storing the position of the player car
        self.can_move = False  # the player car can't move anymore
        self.rect.x = -2000  # moving the player car out of the screen
        return stored_position  # returning the stored position
    
    def respawn(self, stored_position):  # this function will be called when the player car respawns (used for the Gal Pal Rebirth Power Up)
        self.health = self.max_health - 1  # the player car will have one less health point than the maximum
        self.can_move = True  # the player car can move again
        self.rect.x = stored_position[0]  # replacing the player car in the stored position
        self.rect.y = stored_position[1]
    
    def resize_car(self, multiplier):
        # Function that resizes the traffic car according to the multiplier, used for the Toy Transforminator Power Up
        current_position = [self.rect.x, self.rect.y]  # storing the current position of the traffic car
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * multiplier), int(self.image.get_height() * multiplier)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = current_position[0]
        self.rect.y = current_position[1]


class TrafficCar(Car):

    def __init__(self, car_type_number, direction, difficulty):

        if 1 <= car_type_number <= 6:  # we have cars with equal shape but different colors, so we will use the same speed and health for them
            speed = 14
            health = 1
        elif 7 <= car_type_number <= 12:
            speed = 11
            health = 2
        elif 13 <= car_type_number <= 18:
            speed = 12
            health = 1
        elif 19 <= car_type_number <= 26:
            speed = 10
            health = 2
        elif 27 <= car_type_number <= 32:
            speed = 13
            health = 1

        image_path = f'images/cars_{direction}/car{car_type_number}.png'  # getting the image path according to the car type number and the direction (if the car is going up or down)

        super().__init__(image_path, speed, health)  # calling the parent class' constructor

        if difficulty == 'hard':  # if the difficulty is hard, the traffic cars will move faster
            self.speed += 2

    # Movement functions for the traffic cars

    def move_up(self):
        self.rect.y -= (self.speed)

    def move_down(self):
        self.rect.y += (self.speed)

    # Other functions

    def change_car(self, car_type_number, direction):

        # This function will receive a number, change the speed and health of the traffic car according to that number, and return the new image path to the parent class to change it

        if 1 <= car_type_number <= 6:
            speed = 14
            health = 1
        elif 7 <= car_type_number <= 12:
            speed = 11
            health = 2
        elif 13 <= car_type_number <= 18:
            speed = 12
            health = 1
        elif 19 <= car_type_number <= 26:
            speed = 10
            health = 2
        elif 27 <= car_type_number <= 32:
            speed = 13
            health = 1

        image_path = f'images/cars_{direction}/car{car_type_number}.png'

        super().change_image(image_path)

        self.speed = speed
        self.health = health

    def resize_car(self, multiplier):

        # Function that resizes the traffic car according to the multiplier, used for the Toy Transforminator Power Up
        current_position = [self.rect.x, self.rect.y]  # storing the current position of the traffic car
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * multiplier), int(self.image.get_height() * multiplier)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = current_position[0]
        self.rect.y = current_position[1]
          # replacing the traffic car in the stored position
        