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

    def change_image(self, car_image, width, height, x_box, y_box):
        new_image = pygame.image.load(car_image).convert_alpha()
        new_image = pygame.transform.scale(new_image, (width, height))
        self.image = new_image
        self.rect = self.image.get_rect()
        self.box = pygame.Rect(self.rect.x + x_box, self.rect.y + y_box, x_box, y_box)
        self.width = width
        self.height = height

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

