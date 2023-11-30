import pygame

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):  # a sprite is a thing that moves around the screen and can be interacted with
    # A car is a two-dimensional image that can be interacted with, a child of the Sprite class

    def __init__(self, car_image, width, height, x_box=0, y_box=0, speed=0, health=0):
        super().__init__()
        self.car_image = car_image
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.base_width = width
        self.base_height = height

        self.image = pygame.image.load(car_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.box = pygame.Rect(self.rect.x + x_box, self.rect.y + y_box, x_box, y_box)

    ''' End of movement functions. '''

    def add_speed(self, speed):
        self.speed += speed

    def add_health(self, health):
        self.health += health

    def resize(self, multiplier_x, multiplier_y):
        old_center = self.rect.center  # Save the current center of the rect
        self.width *= multiplier_x
        self.height *= multiplier_y
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = old_center  # Put the rect back in place

    def player_resize(self):
        old_center = self.rect.center
        self.width = self.base_width
        self.height = self.base_height
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def change_image(self, car_image, width, height, x_box, y_box):
        old_center = self.rect.center
        new_image = pygame.image.load(car_image).convert_alpha()
        new_image = pygame.transform.scale(new_image, (width, height))
        self.image = new_image
        self.rect = self.image.get_rect()
        self.box = pygame.Rect(self.rect.x + x_box, self.rect.y + y_box, x_box, y_box)
        self.width = width
        self.height = height
        self.rect.center = old_center

    def change_car_image(self, player, power_up_type): # this is a generalization of the change_image function for all cars types
        if player == 'car1':
            car_type = 'car1'
        elif player == 'car2':
            car_type = 'car2'
        elif player == 'car3':
            car_type = 'car3'

        power_up_images = {
            'normal': {
                'car1': 'images/players_cars/car1.png',
                'car2': 'images/players_cars/car2.png',
                'car3': 'images/players_cars/car3.png',
            },
            'besties_in_harmony': {
                'car1': 'images/power_ups_visuals/besties_in_harmony/car1_besties.png',
                'car2': 'images/power_ups_visuals/besties_in_harmony/car2_besties.png',
                'car3': 'images/power_ups_visuals/besties_in_harmony/car3_besties.png',
            },
            'diva_defiance': {
                'car1': 'images/power_ups_visuals/diva_defiance/car1_diva.png',
                'car2': 'images/power_ups_visuals/diva_defiance/car2_diva.png',
                'car3': 'images/power_ups_visuals/diva_defiance/car3_diva.png',
            },
            'tangled_twist': {
                'car1': 'images/power_ups_visuals/tangled_twist/car1_tangled.png',
                'car2': 'images/power_ups_visuals/tangled_twist/car2_tangled.png',
                'car3': 'images/power_ups_visuals/tangled_twist/car3_tangled.png',
            }}

        image_path = power_up_images[power_up_type][car_type]
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def check_collision(self, other):
        return self.box.colliderect(other.box)


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


# car 1: base speed, base hp, base size, more power up duration and less power up cooldown
class Car1(PlayerCar):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)
        self.speed += 0
        self.health += 0


# car 2: more speed, less hp, less width, base power up duration and base power up cooldown
class Car2(PlayerCar):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)
        self.speed += 3
        self.health -= 2


# car 3: less speed, more hp, more width, base power up duration and base power up cooldown
class Car3(PlayerCar):

    def __init__(self, car_image, width, height, x_box, y_box, speed=0, health=0):
        super().__init__(car_image, width, height, x_box, y_box, speed, health)
        self.speed -= 2
        self.health += 3

