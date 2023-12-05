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
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

class PlayerCar(Car):

    def __init__(self, car_type, difficulty):

        if car_type == 'car1':
            image_path = 'images/players_cars/car1.png'
            speed = 3
            health = 3
            max_health = 4
        elif car_type == 'car2':
            image_path = 'images/players_cars/car2.png'
            speed = 6
            health = 2
            max_health = 3
        elif car_type == 'car3':
            image_path = 'images/players_cars/car3.png'
            speed = 0
            health = 4
            max_health = 5

        super().__init__(image_path, speed, health)

        self.car_type = car_type
        self.max_health = max_health

        self.can_collide = True
        self.can_crash = True
        self.eliminated = False
        self.can_move = True
        self.controls_inverted = False
        self.size_increased = False

        if difficulty == 'easy':
            self.add_health(1)
        elif difficulty == 'hard':
            self.add_health(-1)

    # Movement functions for the player car

    def move_up(self , speed_modifier=0):
        if self.can_move:
            self.rect.y -= (self.speed + speed_modifier)
            if self.rect.y < 0:
                self.rect.y = 0

    def move_down(self, speed_modifier=0):
        if self.can_move:
            self.rect.y += (self.speed + speed_modifier)
            if self.rect.y > 800 - self.rect.height:
                self.rect.y = 800 - self.rect.height

    def move_left(self, speed_modifier=0):
        if self.can_move:
            self.rect.x -= (self.speed + speed_modifier)
            if self.rect.x < 272:
                self.rect.x = 272

    def move_right(self, speed_modifier=0):
        if self.can_move:
            self.rect.x += (self.speed + speed_modifier)
            if self.rect.x > 980 - self.rect.width:
                self.rect.x = 980 - self.rect.width

    # Other functions

    def add_health(self, health):
        if self.health < self.max_health:
            self.health += health
        self.check_health()

    def check_health(self):
        if self.health <= 0:
            self.eliminated = True
            self.die()

    def change_image(self, active_power_ups):

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

        image_path = power_ups_images_paths[active_power_ups]
        super().change_image(image_path)

    def die(self):
        stored_position = [self.rect.x, self.rect.y]
        self.can_move = False
        self.rect.x = -2000
        return stored_position
    
    def respawn(self, stored_position):
        self.health = self.max_health - 1
        self.can_move = True
        self.rect.x = stored_position[0]
        self.rect.y = stored_position[1]


class TrafficCar(Car):

    def __init__(self, car_type_number, direction, difficulty):

        if 1 <= car_type_number <= 6:
            speed = 4
            health = 1
        elif 7 <= car_type_number <= 12:
            speed = 1
            health = 2
        elif 13 <= car_type_number <= 18:
            speed = 2
            health = 1
        elif 19 <= car_type_number <= 26:
            speed = 0
            health = 2
        elif 27 <= car_type_number <= 32:
            speed = 3
            health = 1

        image_path = f'images/cars_{direction}/car{car_type_number}.png'

        super().__init__(image_path, speed, health)

        if difficulty == 'hard':
            self.speed += 2

    # Movement functions for the traffic cars

    def move_up(self, speed_modifier=0):
        self.rect.y -= (self.speed + speed_modifier)

    def move_down(self, speed_modifier=0):
        self.rect.y += (self.speed + speed_modifier)

    # Other functions

    def change_car(self, car_type_number, direction, difficulty):

        # This function will receive a number, change the speed and health of the traffic car according to that number, and return the new image path to the parent class to change it

        if 1 <= car_type_number <= 6:
            speed = 4
            health = 1
        elif 7 <= car_type_number <= 12:
            speed = 1
            health = 2
        elif 13 <= car_type_number <= 18:
            speed = 2
            health = 1
        elif 19 <= car_type_number <= 26:
            speed = 0
            health = 2
        elif 27 <= car_type_number <= 32:
            speed = 3
            health = 1

        image_path = f'images/cars_{direction}/car{car_type_number}.png'

        super().change_image(image_path)

        self.speed = speed
        self.health = health

    def resize_car(self, multiplier):

        # Function that resizes the traffic car according to the multiplier, used for the Toy Transforminator Power Up

        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * multiplier), int(self.image.get_height() * multiplier)))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)