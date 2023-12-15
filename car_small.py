import pygame


class Car(pygame.sprite.Sprite):

    """
    A class representing a car in the game.

    Attributes
    ----------
        image : pygame.Surface
            The image of the car.
        rect : pygame.Rect
            The rectangle of the car's image.
        mask : pygame.Mask
            The mask for collision detection.
        speed : int
            The speed of the car.
        health : int
            The health points of the car.

    Methods
    -------
        add_speed
            Add speed to the car.
        change_image
            Change the image of the car.
        set_position
            Set the position of the car.
    """

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

    """
    A class representing a player's car in the game.

    Attributes
    ----------
    car_type : str
        The type of the car.
    max_health : int
        The maximum health points of the car.
    can_collide : bool
        If the car can collide with other players.
    can_crash : bool
        If the car can crash with traffic cars.
    eliminated : bool
        If the car has been eliminated.
    can_move : bool
        If the car can move.
    controls_inverted : bool
        If the controls are inverted.

    Methods
    -------
    move_up()
        Move the car up.
    move_down()
        Move the car down.
    move_left()
        Move the car left.
    move_right()
        Move the car right.
    add_health()
        Add health points to the car.
    change_image()
        Change the image of the car based on active power-ups.
    die()
        Perform actions when the car dies.
    respawn()
        Perform actions when the car respawns.
    resize_car()
        Resize the car based on a multiplier.
    """

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
            if self.rect.y < 80:
                self.rect.y = 80

    def move_down(self):
        if self.can_move:
            self.rect.y += self.speed
            if self.rect.y > 938 - self.rect.height:
                self.rect.y = 938 - self.rect.height

    def move_left(self):
        if self.can_move:
            self.rect.x -= self.speed
            if self.rect.x < 218:
                self.rect.x = 218

    def move_right(self):
        if self.can_move:
            self.rect.x += self.speed
            if self.rect.x > 784 - self.rect.width:
                self.rect.x = 784 - self.rect.width

    # Other functions

    def add_health(self, health):
        if health > 0:  # if the health points to be added are negative, we will subtract them instead
            if self.health < self.max_health:  # if the player car has not reached the maximum health points
                self.health += health
        elif health < 0:
            self.health += health

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

        self.set_position(current_position[0], current_position[1])
        
    def die(self):  # this function will be called when the player car dies
        stored_position = [self.rect.x, self.rect.y]  # storing the position of the player car
        self.can_move = False  # the player car can't move anymore
        self.rect.x = -2000  # moving the player car out of the screen
        self.eliminated = True  # the player car has been eliminated
        return stored_position  # returning the stored position
    
    def respawn(self):  # this function will be called when the player car respawns (used for the Gal Pal Rebirth Power Up)
        self.health = self.max_health - 1  # the player car will have one less health point than the maximum
        self.can_move = True  # the player car can move again
        self.set_position(228, (938 - self.rect.height))
        self.eliminated = False  # the player car has not been eliminated anymore
    
    def resize_car(self, multiplier):
        # Function that resizes the traffic car according to the multiplier, used for the Toy Transforminator Power Up
        current_position = [self.rect.x, self.rect.y]  # storing the current position of the traffic car
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * multiplier), int(self.image.get_height() * multiplier)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.set_position(current_position[0], current_position[1])

class TrafficCar(Car):

    """
    A class representing a traffic car in the game.

    Parameters
    ----------
    car_type_number : int
        The number representing the car type.
    direction : str
        The direction of the car.
    difficulty : str
        The difficulty level of the game.

    Attributes
    ----------
    speed : int
        The speed of the car.
    health : int
        The health points of the car.

    Methods
    -------
    move_up()
        Move the car up.
    move_down()
        Move the car down.
    change_car(car_type_number, direction)
        Change the car's attributes based on car type and direction.
    resize_car(multiplier)
        Resize the car based on a multiplier.
    """

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
        self.set_position(current_position[0], current_position[1])
        # replacing the traffic car in the stored position
