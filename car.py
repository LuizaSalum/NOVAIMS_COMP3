import pygame
from abc import abstractmethod

class Car(pygame.sprite.Sprite): # a sprite is a thing that moves around the screen and can be interacted with
    # A car is a two-dimensional image that can be interacted with, a child of the Sprite class

    def __init__(self, car_image, width, height, x_box=0, y_box=0, speed=0, health=0, max_health=0):
        super().__init__()
        self.car_image = car_image
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.max_health = max_health
        self.base_width = width
        self.base_height = height
        self.x_box = x_box
        self.y_box = y_box

        self.image = pygame.image.load(car_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.box = pygame.Rect(self.rect.x + x_box, self.rect.y + y_box, x_box, y_box)

    def add_speed(self, speed):
        self.speed += speed

    def add_health(self, health):
        self.health += health

    def change_image(self, car_image, width, height, x_box, y_box): # this function is used to change the image of the car and resize it
        old_center = self.rect.center
        new_image = pygame.image.load(car_image).convert_alpha()
        new_image = pygame.transform.scale(new_image, (width, height))
        self.image = new_image 
        self.rect = self.image.get_rect()
        self.box = pygame.Rect(self.rect.x + x_box, self.rect.y + y_box, x_box, y_box)
        self.width = width
        self.height = height
        self.rect.center = old_center


class PlayerCar(Car):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)

    ''' The following functions are used to move the car around the screen. '''

    def move_right(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.x += pixels

    def move_left(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.x -= pixels

    def move_up(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.y -= pixels

    def move_down(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.y += pixels

    ''' End of movement functions. '''

    def player_resize(self):
        old_center = self.rect.center # Save the current center of the rect
        self.width = self.base_width
        self.height = self.base_height
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = old_center # Put the rect back in place

    @abstractmethod
    def change_car_image(self, player, power_up_type):

        power_up_images = {
            'normal': f'images/players_cars/{player}.png',
            'besties': f'images/power_ups_visuals/besties/{player}_besties.png',
            'besties_tangled': f'images/power_ups_visuals/besties_tangled/{player}_besties_tangled.png',
            'besties_growth': f'images/power_ups_visuals/besties_growth/{player}_besties.png',
            'besties_tangled_growth': f'images/power_ups_visuals/besties_tangled_growth/{player}_besties_tangled.png',
            'besties_diva': f'images/power_ups_visuals/besties_diva/{player}_besties_diva.png',
            'besties_diva_tangled': f'images/power_ups_visuals/besties_diva_tangled/{player}_besties_diva_tangled.png',
            'besties_diva_growth': f'images/power_ups_visuals/besties_diva_growth/{player}_besties_diva.png',
            'besties_diva_tangled_growth': f'images/power_ups_visuals/besties_diva_tangled_growth/{player}_besties_diva_tangled.png',
            'tangled': f'images/power_ups_visuals/tangled/{player}_tangled.png',
            'growth': f'images/power_ups_visuals/growth/{player}.png',
            'tangled_growth': f'images/power_ups_visuals/tangled_growth/{player}_tangled.png',
            'diva': f'images/power_ups_visuals/diva/{player}_diva.png',
            'diva_tangled': f'images/power_ups_visuals/diva_tangled/{player}_diva_tangled.png',
            'diva_growth': f'images/power_ups_visuals/diva_growth/{player}_diva.png',
            'diva_tangled_growth': f'images/power_ups_visuals/diva_tangled_growth/{player}_diva_tangled.png'
            }
        
        return power_up_images[power_up_type]


class TrafficCar(Car):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)

    ''' The following functions are used to move the car around the screen. '''

    def move_down(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.y += pixels

    def move_up(self, p_speed):
        pixels = self.speed + p_speed
        self.rect.y -= pixels

    ''' End of movement functions. '''

    def resize(self, multiplier_x, multiplier_y):
        old_center = self.rect.center  # Save the current center of the rect
        self.width *= multiplier_x
        self.height *= multiplier_y
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = old_center  # Put the rect back in place


# car 1: base speed, base hp, base size, more power up duration and less power up cooldown
class Car1(PlayerCar):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)
        self.car_type = 'car1'
        self.speed += 0
        self.health += 0

    def change_car_image(self, power_up_type):

        image_path = super().change_car_image('car1', power_up_type)

        if 'diva' in power_up_type:  # there's a border around the diva power up image, so we need to resize the car image
            self.width = 127
            self.height = 189
            self.x_box = 127
            self.y_box = 189

        if 'growth' in power_up_type:  # the growth power up image is bigger than the normal one, so we need to resize the car image
            self.width = self.width * 1.15
            self.height = self.height * 1.15
            self.x_box = self.x_box * 1.15
            self.y_box = self.y_box * 1.15

        self.image = pygame.image.load(image_path).convert_alpha()


# car 2: more speed, less hp, less width, base power up duration and base power up cooldown
class Car2(PlayerCar):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)
        self.car_type = 'car2'
        self.speed += 3
        self.health -= 2

    def change_car_image(self, power_up_type):

        image_path = super().change_car_image('car2', power_up_type)
        
        if 'diva' in power_up_type:  # there's a border around the diva power up image, so we need to resize the car image
            self.width = 111
            self.height = 212
            self.x_box = 111
            self.y_box = 212

        if 'growth' in power_up_type:  # the growth power up image is bigger than the normal one, so we need to resize the car image
            self.width = self.width * 1.15
            self.height = self.height * 1.15
            self.x_box = self.x_box * 1.15
            self.y_box = self.y_box * 1.15

        self.image = pygame.image.load(image_path).convert_alpha()


# car 3: less speed, more hp, more width, base power up duration and base power up cooldown
class Car3(PlayerCar):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)
        self.car_type = 'car3'
        self.speed -= 2
        self.health += 3

    def change_car_image(self, power_up_type):

        image_path = super().change_car_image('car3', power_up_type)

        if 'diva' in power_up_type:
            self.width = 114
            self.height = 195
            self.x_box = 114
            self.y_box = 195

        if 'growth' in power_up_type:
            self.width = self.width * 1.15
            self.height = self.height * 1.15
            self.x_box = self.x_box * 1.15
            self.y_box = self.y_box * 1.15

        self.image = pygame.image.load(image_path).convert_alpha()
