import pygame
import random
from car import TrafficCar, Car1, Car2, Car3
from power_up import *
import random

# GREY = (197, 197, 197)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
# YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
SKY_BLUE = (135, 206, 235)

score = 0

def multi_game(difficulty, lolly, bestie, power_ups):
    pygame.init()
    pygame.font.init()

    size = (1250, 950)
    screen = pygame.display.set_mode(size)  

    ''' Importing images'''

    # road
    road = pygame.image.load("images/road.png").convert()

    # hearts
    heart1 = pygame.image.load("images/hearts/heart1.png").convert_alpha()
    heart2 = pygame.image.load("images/hearts/heart2.png").convert_alpha()
    heart3 = pygame.image.load("images/hearts/heart3.png").convert_alpha()

    # incoming cars

    cars_dimensions = [
        (1, 6, 180*0.65, 352*0.65, 133*0.65, 318*0.65),
        (7, 12, 178*0.65, 383*0.65, 133*0.65, 348*0.65),
        (13, 18, 178*0.65, 244*0.65, 133*0.65, 211*0.65),
        (19, 26, 185*0.65, 383*0.65, 133*0.65, 352*0.65),
        (27, 32, 179*0.65, 302*0.65, 133*0.65, 277*0.65)
    ]  # starting number, ending number, width, height, x_box, y_box
    # multiply by 0.65 bc I had to resize some things

    cars_images_left = []
    cars_images_right = []

    for i in range(1, 33):
        for start, end, dim_x, dim_y, x_box, y_box in cars_dimensions:
            if start <= i <= end:
                dimension_x = dim_x
                dimension_y = dim_y
                break
        car_image_left = [f"images/cars_left/car{i}.png", dimension_x, dimension_y, x_box, y_box]
        car_image_right = [f"images/cars_right/car{i}.png", dimension_x, dimension_y, x_box, y_box]
        cars_images_left.append(car_image_left)
        cars_images_right.append(car_image_right)

    # players cars

    players_cars = []

    car_1 = [f"images/players_cars/car1.png", 116, 178, 116, 178]  # image, width, height, x_box, y_box
    car_2 = [f"images/players_cars/car2.png", 101, 202, 101, 202]
    car_3 = [f"images/players_cars/car3.png", 108, 189, 108, 189]

    players_cars.append(car_1)
    players_cars.append(car_2)
    players_cars.append(car_3)

    ''' Positioning Cars '''

    # incoming cars

    if difficulty == 'easy' or difficulty == 'normal':
        selected_left_car_1 = random.choice(cars_images_left)
        left_car_1 = TrafficCar(selected_left_car_1[0], selected_left_car_1[1], selected_left_car_1[2], selected_left_car_1[3], selected_left_car_1[4])
        left_car_1.rect.x = random.choice([285, 466, 643, 825])  # if it's only the box, it's 303, 482, 662, 842
        left_car_1.rect.y = random.randint(-1500, -100)

        selected_left_car_2 = random.choice(cars_images_left)
        left_car_2 = TrafficCar(selected_left_car_2[0], selected_left_car_2[1], selected_left_car_2[2], selected_left_car_2[3], selected_left_car_2[4])
        left_car_2.rect.x = random.choice([285, 466, 643, 825])
        left_car_2.rect.y = random.randint(-1500, -100)

        selected_left_car_3 = random.choice(cars_images_left)
        left_car_3 = TrafficCar(selected_left_car_3[0], selected_left_car_3[1], selected_left_car_3[2], selected_left_car_3[3], selected_left_car_3[4])
        left_car_3.rect.x = random.choice([285, 466, 643, 825])
        left_car_3.rect.y = random.randint(-1500, -100)

        selected_left_car_4 = random.choice(cars_images_left)
        left_car_4 = TrafficCar(selected_left_car_4[0], selected_left_car_4[1], selected_left_car_4[2], selected_left_car_4[3], selected_left_car_4[4])
        left_car_4.rect.x = random.choice([285, 466, 643, 825])
        left_car_4.rect.y = random.randint(-1500, -100)

        left_incoming_cars = pygame.sprite.Group()
        left_incoming_cars.add(left_car_1)
        left_incoming_cars.add(left_car_2)
        left_incoming_cars.add(left_car_3)
        left_incoming_cars.add(left_car_4)

    if difficulty == 'hard':
        selected_left_car_1 = random.choice(cars_images_left)
        left_car_1 = TrafficCar(selected_left_car_1[0], selected_left_car_1[1], selected_left_car_1[2], selected_left_car_1[3], selected_left_car_1[4])
        left_car_1.rect.x = random.choice([285, 466])
        left_car_1.rect.y = random.randint(-1500, -100)

        selected_left_car_2 = random.choice(cars_images_left)
        left_car_2 = TrafficCar(selected_left_car_2[0], selected_left_car_2[1], selected_left_car_2[2], selected_left_car_2[3], selected_left_car_2[4])
        left_car_2.rect.x = random.choice([285, 466])
        left_car_2.rect.y = random.randint(-1500, -100)

        selected_right_car_1 = random.choice(cars_images_right)
        right_car_1 = TrafficCar(selected_right_car_1[0], selected_right_car_1[1], selected_right_car_1[2], selected_right_car_1[3], selected_right_car_1[4])
        right_car_1.rect.x = random.choice([643, 825])
        right_car_1.rect.y = random.randint(-1500, -100)

        selected_right_car_2 = random.choice(cars_images_right)
        right_car_2 = TrafficCar(selected_right_car_2[0], selected_right_car_2[1], selected_right_car_2[2], selected_right_car_2[3], selected_right_car_2[4])
        right_car_2.rect.x = random.choice([643, 825])
        right_car_2.rect.y = random.randint(-1500, -100)

        left_incoming_cars = pygame.sprite.Group()
        left_incoming_cars.add(left_car_1)
        left_incoming_cars.add(left_car_2)

        right_incoming_cars = pygame.sprite.Group()
        right_incoming_cars.add(right_car_1)
        right_incoming_cars.add(right_car_2)

    # players cars (Lolly and Bestie)
    
    if lolly == 'car1':
        LollyCar = Car1(car_1[0], car_1[1], car_1[2], car_1[3], car_1[4])
        LollyCar.rect.x = 466
        LollyCar.rect.y = 800
        
    if lolly == 'car2':
        LollyCar = Car2(car_2[0], car_2[1], car_2[2], car_2[3], car_2[4])
        LollyCar.rect.x = 466
        LollyCar.rect.y = 800
    
    if lolly == 'car3':
        LollyCar = Car3(car_3[0], car_3[1], car_3[2], car_3[3], car_3[4])
        LollyCar.rect.x = 466
        LollyCar.rect.y = 800
        
    if bestie == 'car1':
        BestieCar = Car1(car_1[0], car_1[1], car_1[2], car_1[3], car_1[4])
        BestieCar.rect.x = 285
        BestieCar.rect.y = 800
        
    if bestie == 'car2':
        BestieCar = Car2(car_2[0], car_2[1], car_2[2], car_2[3], car_2[4])
        BestieCar.rect.x = 285
        BestieCar.rect.y = 800
        
    if bestie == 'car3':
        BestieCar = Car3(car_3[0], car_3[1], car_3[2], car_3[3], car_3[4])
        BestieCar.rect.x = 285
        BestieCar.rect.y = 800

    ''' Positioning Power Ups '''
    
    if 'besties_in_harmony' in power_ups:
        besties_in_harmony = BestiesInHarmony()
        besties_in_harmony.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100)) # starting pos of the power ups
        besties_in_harmony.active = False
        besties_in_harmony.base_speed = 3

    if 'diva_defiance' in power_ups:
        diva_defiance = DivaDefiance()
        diva_defiance.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        diva_defiance.active = False
        diva_defiance.base_speed = 3

    if 'frosty_frenzy' in power_ups:
        frosty_frenzy = FrostyFrenzy()
        frosty_frenzy.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        frosty_frenzy.active = False
        frosty_frenzy.base_speed = 3

    if 'gal_pal_rebirth' in power_ups:
        gal_pal_rebirth = GalPalRebirth()
        gal_pal_rebirth.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        gal_pal_rebirth.active = False
        gal_pal_rebirth.base_speed = 3
            
    if 'tangled_twist' in power_ups:
        tangled_twist = TangledTwist()
        tangled_twist.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        tangled_twist.active = False
        tangled_twist.base_speed = 3
   
    if 'glamorous_growth' in power_ups:
        glamorous_growth = GlamorousGrowth()
        glamorous_growth.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        glamorous_growth.active = False
        glamorous_growth.base_speed = 3

    if 'sissy_that_walk' in power_ups:
        sissy_that_walk = SissyThatWalk()
        sissy_that_walk.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        sissy_that_walk.active = False
        sissy_that_walk.base_speed = 3
        
    if 'toy_transforminator' in power_ups:
        toy_transforminator = ToyTransforminator()
        toy_transforminator.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
        toy_transforminator.active = False
        toy_transforminator.base_speed = 3

    ''' Define the probability for each power-up'''
    power_up_probabilities = {
        "besties_in_harmony": 0.01,
        "diva_defiance": 0.01,
        "frosty_frenzy": 0.01,
        "gal_pal_rebirth": 0.01,
        "tangled_twist": 0.01,
        "glamorous_growth": 0.01,
        "sissy_that_walk": 0.01,
        "toy_transforminator": 0.01,
    }
            
    ''' Adding Sprites to Group '''

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(LollyCar)
    all_sprites_list.add(BestieCar)
    all_sprites_list.add(left_incoming_cars)

    if difficulty == 'hard':
        all_sprites_list.add(right_incoming_cars)
    if 'besties_in_harmony' in power_ups:
        all_sprites_list.add(besties_in_harmony)
    if 'diva_defiance' in power_ups:
        all_sprites_list.add(diva_defiance)
    if 'frosty_frenzy' in power_ups:
        all_sprites_list.add(frosty_frenzy)
    if 'gal_pal_rebirth' in power_ups:
        all_sprites_list.add(gal_pal_rebirth)
    if 'tangled_twist' in power_ups:
        all_sprites_list.add(tangled_twist)
    if 'glamorous_growth' in power_ups:
        all_sprites_list.add(glamorous_growth)
    if 'sissy_that_walk' in power_ups:
        all_sprites_list.add(sissy_that_walk)
    if 'toy_transforminator' in power_ups:
        all_sprites_list.add(toy_transforminator)

    ''' Setting Up Variables '''

    Size_LollyCar = (LollyCar.width, LollyCar.height)
    Size_BestieCar = (BestieCar.width, BestieCar.height)
    score = 0
    road_y = 0
    obstacle_counter = 0

    if difficulty == 'easy':
        speed_buffer = 5
        traffic_speed_buffer = -3
        HP_buffer = 3
        power_ups_duration_buffer = 10
        power_ups_cooldown_nerfer = 3
    elif difficulty == 'normal':
        speed_buffer = 0
        traffic_speed_buffer = 0
        HP_buffer = 3
        power_ups_duration_buffer = 0
        power_ups_cooldown_nerfer = 0
    elif difficulty == 'hard':
        speed_buffer = -2
        traffic_speed_buffer = 2
        HP_buffer = -2
        power_ups_duration_buffer = -2
        power_ups_cooldown_nerfer = -2

    LollyCar.add_speed(speed_buffer)
    BestieCar.add_speed(speed_buffer)
    LollyCar.add_health(HP_buffer)
    BestieCar.add_health(HP_buffer)

    for car in left_incoming_cars:
        car.add_speed(traffic_speed_buffer)

    carryOn = True

    power_up = None
    power_ups = []

    # starting the clock
    clock = pygame.time.Clock()

    while carryOn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()

        ''' We should change this so it opens the pause menu instead of quitting the game.'''
        if keys[pygame.K_ESCAPE]:
            carryOn = False

        ''' Lolly controls '''

        if tangled_twist.active:  # if the tangled twist power up is active, the controls are reversed
            if BestieCar.health > 0:
                if keys[pygame.K_w]:
                    BestieCar.move_up(20)
                if keys[pygame.K_s]:
                    BestieCar.move_down(20)
                if keys[pygame.K_a]:
                    BestieCar.move_left(20)
                    if BestieCar.rect.y < 0:
                        BestieCar.rect.y = 0
                if keys[pygame.K_d]:
                    BestieCar.move_right(20)
                    if BestieCar.rect.y < 0:
                        BestieCar.rect.y = 0
            if LollyCar.health > 0: 
                if keys[pygame.K_UP]:
                    LollyCar.move_up(20)
                if keys[pygame.K_DOWN]:
                    LollyCar.move_down(20)
                if keys[pygame.K_LEFT]:
                    LollyCar.move_left(20)
                    if LollyCar.rect.y < 0:
                        LollyCar.rect.y = 0
                if keys[pygame.K_RIGHT]:
                    LollyCar.move_right(20)
                    if LollyCar.rect.y > 800:
                        LollyCar.rect.y = 800
            
        else: # if the tangled twist power up is not active, the controls are normal
                if LollyCar.health > 0: # if the player is alive, they can move
                    if keys[pygame.K_a]:
                        LollyCar.move_left(20)
                    if keys[pygame.K_d]:
                        LollyCar.move_right(20)
                    if keys[pygame.K_w]:
                        LollyCar.move_up(20)
                        if LollyCar.rect.y < 0:
                            LollyCar.rect.y = 0
                    if keys[pygame.K_s]:
                        LollyCar.move_down(20)
                        if LollyCar.rect.y > 800:
                            LollyCar.rect.y = 800
                if BestieCar.health > 0:
                    if keys[pygame.K_LEFT]:
                        BestieCar.move_left(20)
                    if keys[pygame.K_RIGHT]:
                        BestieCar.move_right(20)
                    if keys[pygame.K_UP]:
                        BestieCar.move_up(20)
                        if BestieCar.rect.y < 0:
                            BestieCar.rect.y = 0
                    if keys[pygame.K_DOWN]:
                        BestieCar.move_down(20)
                        if BestieCar.rect.y > 800:
                            BestieCar.rect.y = 800

        all_sprites_list.update(all_sprites_list)

        ''' Prevent the cars from going off the street'''
    
        if LollyCar.rect.x < 230:
            LollyCar.rect.x = 230
        if LollyCar.rect.x > 900:
            LollyCar.rect.x = 900

        if BestieCar.rect.x < 230:
            BestieCar.rect.x = 230
        if BestieCar.rect.x > 900:
            BestieCar.rect.x = 900

        ''' Scrolling the road '''

        # Scrolling the road
        scroll_speed = 3000
        dt = clock.tick(60) / 1000.0
        road_y += scroll_speed * dt
        score_font =  pygame.font.Font(pygame.font.get_default_font(), 36)

        # Wrap the road texture when it goes off the screen
        if road_y >= 950:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - 950))

        ''' Incoming Cars '''

        if difficulty != 'hard':

            for car in left_incoming_cars:
                car.move_down(15)
                if car.rect.y > 950:
                    new_car = random.choice(cars_images_left)
                    car.change_image(new_car[0], new_car[1], new_car[2], new_car[3], new_car[4])
                    car.add_speed(random.randint(-1, 3))
                    car.rect.y = random.randint(-2200, -800)
                    car.rect.x = random.choice([285, 466, 643, 825])

        if difficulty == 'hard':

            for car in left_incoming_cars:
                car.move_down(15)
                if car.rect.y > 950:
                    new_car = random.choice(cars_images_left)
                    car.change_image(new_car[0], new_car[1], new_car[2], new_car[3], new_car[4])
                    car.add_speed(random.randint(-1, 3))
                    car.rect.y = random.randint(-2200, -800)
                    car.rect.x = random.choice([285, 466])

            for car in right_incoming_cars:
                car.move_down(15)
                if car.rect.y > 950:
                    new_car = random.choice(cars_images_right)
                    car.change_image(new_car[0], new_car[1], new_car[2], new_car[3], new_car[4])
                    car.add_speed(random.randint(-1, 3))
                    car.rect.y = random.randint(-2200, -800)
                    car.rect.x = random.choice([643, 825])

        ''' Collision Between Players'''
        if besties_in_harmony.active:
            if pygame.sprite.collide_rect(LollyCar, BestieCar):
                pass
        else:
            if pygame.sprite.collide_rect(LollyCar, BestieCar):
                if LollyCar.rect.x < BestieCar.rect.x:
                    LollyCar.rect.x -= 20
                    BestieCar.rect.x += 20
                else:
                    LollyCar.rect.x += 20
                    BestieCar.rect.x -= 20
                ''' Collision Detection '''

        if difficulty != 'hard':

            for car_1 in left_incoming_cars:
                for car_2 in left_incoming_cars:
                    if car_1 != car_2 and car_1.rect.colliderect(car_2.rect):
                        if car_1.rect.y < -800 or car_2.rect.y < -200:
                            car_1.rect.y = random.randint(-2200, -800)
                            car_1.rect.x = random.choice([285, 466, 643, 825])
                        else:
                            car_2.speed = 0

                if pygame.sprite.collide_rect(LollyCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466, 643, 825])
                    # if the player collides with a car, check if they have the diva defiance power up
                    if diva_defiance.active:
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                    # if they don't, check if they have HP to survive the crash
                    elif LollyCar.health > 1:
                        LollyCar.add_health(-1)
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                    elif LollyCar.health == 1:
                        LollyCar.add_health(-1)
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                        LollyCar.rect.x = 0
                        LollyCar.rect.y = -50000 
                        # this will hide the car from the screen, so it will look like it was eliminated
                        # if both players are eliminated, the game ends
                        if BestieCar.health == 0:
                            game_over(road, difficulty, lolly, bestie, power_ups)

                if pygame.sprite.collide_rect(BestieCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466, 643, 825])
                    if diva_defiance.active:
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                    elif BestieCar.health > 1:
                        BestieCar.add_health(-1)
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                    elif BestieCar.health == 1:
                        BestieCar.add_health(-1)
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                        BestieCar.rect.x = 0
                        BestieCar.rect.y = -50000
                        if LollyCar.health == 0:
                            game_over(road, difficulty, lolly, bestie, power_ups)

        if difficulty == 'hard':

            for car_1 in left_incoming_cars:
                for car_2 in left_incoming_cars:
                    if car_1 != car_2 and car_1.rect.colliderect(car_2.rect):
                        if car_1.rect.y < -800 or car_2.rect.y < -200:
                            car_1.rect.y = random.randint(-2200, -800)
                            car_1.rect.x = random.choice([285, 466])
                        else:
                            car_1.speed = 0

                if pygame.sprite.collide_rect(LollyCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466])
                    if diva_defiance.active:
                        car_1.kill()
                    elif LollyCar.health > 1:
                        LollyCar.add_health(-1)
                        car_1.kill()
                    elif LollyCar.health == 1:
                        LollyCar.add_health(-1)
                        LollyCar.rect.x = 0
                        LollyCar.rect.y = -50000
                        if BestieCar.health == 0:
                            game_over(road, difficulty, lolly, bestie, power_ups)

                if pygame.sprite.collide_rect(BestieCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466])
                    if diva_defiance.active:
                        car_1.kill()
                    elif BestieCar.health > 1:
                        BestieCar.add_health(-1)
                        car_1.kill()
                    elif BestieCar.health == 1:
                        BestieCar.add_health(-1)
                        BestieCar.rect.x = 0
                        BestieCar.rect.y = -50000
                        if LollyCar.health == 0:
                            game_over(road, difficulty, lolly, bestie, power_ups)

            for car_1 in right_incoming_cars:
                for car_2 in right_incoming_cars:
                    if car_1 != car_2 and car_1.rect.colliderect(car_2.rect):
                        if car_1.rect.y < -800 or car_2.rect.y < -200:
                            car_1.rect.y = random.randint(-2200, -800)
                            car_1.rect.x = random.choice([643, 825])
                        else:
                            car_1.speed = 0

                if pygame.sprite.collide_rect(LollyCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([643, 825])
                    if diva_defiance.active:
                        car_1.kill()
                    elif LollyCar.health > 1:
                        LollyCar.add_health(-1)
                        car_1.kill()
                    elif LollyCar.health == 1:
                        LollyCar.add_health(-1)
                        LollyCar.rect.x = 0
                        LollyCar.rect.y = -50000
                        if BestieCar.health == 0:
                            game_over(road, difficulty, lolly, bestie, power_ups)

                if pygame.sprite.collide_rect(BestieCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([643, 825])
                    if diva_defiance.active:
                        car_1.kill()
                    elif BestieCar.health > 1:
                        BestieCar.add_health(-1)
                        car_1.kill()
                    elif BestieCar.health == 1:
                        BestieCar.add_health(-1)
                        BestieCar.rect.x = 0
                        BestieCar.rect.y = -50000 
                        if LollyCar.health == 0:
                            game_over(road, difficulty, lolly, bestie, power_ups)

        ''' Check if one of players are eliminated (used later on power ups)'''

        if BestieCar.health == 0 or LollyCar.health == 0:
            player_eliminated = True
        else:
            player_eliminated = False


        for power_up_name, probability in power_up_probabilities.items():
            if random.random() < probability:
                # Set power_up based on power_up_name
                if power_up_name == "besties_in_harmony":
                    power_ups.append(besties_in_harmony)
                elif power_up_name == "diva_defiance":
                    power_ups.append(diva_defiance)
                elif power_up_name == "frosty_frenzy":
                    power_ups.append(frosty_frenzy)
                elif power_up_name == "gal_pal_rebirth":
                    power_ups.append(gal_pal_rebirth)
                elif power_up_name == "tangled_twist":
                    power_ups.append(tangled_twist)
                elif power_up_name == "glamorous_growth":	
                    power_ups.append(glamorous_growth)
                elif power_up_name == "sissy_that_walk":
                    power_ups.append(sissy_that_walk)
                elif power_up_name == "toy_transforminator":
                    power_ups.append(toy_transforminator)

        if besties_in_harmony in power_ups:
            besties_in_harmony.move_down(3)
        if diva_defiance in power_ups:
            diva_defiance.move_down(3)
        if frosty_frenzy in power_ups:
            frosty_frenzy.move_down(3)
        if player_eliminated: # if at least one player is eliminated, the gal pal rebirth power up is spawned
            if gal_pal_rebirth in power_ups:
                gal_pal_rebirth.move_down(3)
        if tangled_twist in power_ups:
            tangled_twist.move_down(3)
        if glamorous_growth in power_ups:
            glamorous_growth.move_down(3)
        if sissy_that_walk in power_ups:
            sissy_that_walk.move_down(3)
        if toy_transforminator in power_ups:
            toy_transforminator.move_down(3)

        

        

        '''
        besties_in_harmony.move_down(besties_in_harmony.base_speed)
        diva_defiance.move_down(diva_defiance.base_speed)
        frosty_frenzy.move_down(frosty_frenzy.base_speed)
        if player_eliminated: # if at least one player is eliminated, the gal pal rebirth power up is spawned
            gal_pal_rebirth.move_down(gal_pal_rebirth.base_speed)
        tangled_twist.move_down(tangled_twist.base_speed)
        glamorous_growth.move_down(glamorous_growth.base_speed)
        sissy_that_walk.move_down(sissy_that_walk.base_speed)
        toy_transforminator.move_down(toy_transforminator.base_speed) '''
        
        if besties_in_harmony.rect.y > 950:
            besties_in_harmony.give_cooldown(30)
        if diva_defiance.rect.y > 950:
            diva_defiance.give_cooldown(30)
        if frosty_frenzy.rect.y > 950:
            frosty_frenzy.give_cooldown(30)
        if player_eliminated: # if at least one player is eliminated, the gal pal rebirth power up is spawned
            if gal_pal_rebirth.rect.y > 950:
                gal_pal_rebirth.give_cooldown(30)
        if tangled_twist.rect.y > 950:
            tangled_twist.give_cooldown(30)
        if glamorous_growth.rect.y > 950:
            glamorous_growth.give_cooldown(30)
        if sissy_that_walk.rect.y > 950:
            sissy_that_walk.give_cooldown(30)
        if toy_transforminator.rect.y > 950:
            toy_transforminator.give_cooldown(30)

        ''' Check collision between players and power ups '''

        if pygame.sprite.collide_rect(LollyCar, besties_in_harmony) or pygame.sprite.collide_rect(BestieCar, besties_in_harmony):
            LollyCar.change_car_image(lolly, 'besties')
            BestieCar.change_car_image(bestie, 'besties')
            besties_in_harmony.collision_with_player() # if the power up is collected, it is removed and enters cooldown

        if pygame.sprite.collide_rect(LollyCar, diva_defiance) or pygame.sprite.collide_rect(BestieCar, diva_defiance):
            diva_defiance.collision_with_player()

        if pygame.sprite.collide_rect(LollyCar, frosty_frenzy) or pygame.sprite.collide_rect(BestieCar, frosty_frenzy):
            frosty_frenzy.collision_with_player()

        if player_eliminated:
            if pygame.sprite.collide_rect(LollyCar, gal_pal_rebirth) or pygame.sprite.collide_rect(BestieCar, gal_pal_rebirth):
                gal_pal_rebirth.collision_with_player()
                if LollyCar.health == 0:
                    LollyCar.health = 1
                    LollyCar.rect.x = 466
                    LollyCar.rect.y = 800
                    player_eliminated = False

                if BestieCar.health == 0:
                    BestieCar.health = 1
                    BestieCar.rect.x = 285
                    BestieCar.rect.y = 800
                    player_eliminated = False

        if pygame.sprite.collide_rect(LollyCar, tangled_twist) or pygame.sprite.collide_rect(BestieCar, tangled_twist):
            LollyCar.change_car_image(lolly, 'tangled')
            BestieCar.change_car_image(bestie, 'tangled')  
            tangled_twist.collision_with_player() 

        if pygame.sprite.collide_rect(LollyCar, glamorous_growth) or pygame.sprite.collide_rect(BestieCar, glamorous_growth):
            if pygame.sprite.collide_rect(LollyCar, glamorous_growth):
                GlamorousGrowth.affect_player(LollyCar)
            if pygame.sprite.collide_rect(BestieCar, glamorous_growth):
                GlamorousGrowth.affect_player(BestieCar)
            glamorous_growth.collision_with_player()

        if pygame.sprite.collide_rect(LollyCar, sissy_that_walk) or pygame.sprite.collide_rect(BestieCar, sissy_that_walk):
            SissyThatWalk.affect_both_players(LollyCar, BestieCar, 15)
            sissy_that_walk.collision_with_player()

        if pygame.sprite.collide_rect(LollyCar, toy_transforminator) or pygame.sprite.collide_rect(BestieCar, toy_transforminator):
            for car in left_incoming_cars:
                car.resize(0.8, 0.8)
            toy_transforminator.collision_with_player()
        
        ''' Changes after collision with power ups and reset after duration '''

        if besties_in_harmony.active: # if the power up is active, the players are invincible
            besties_text = score_font.render("Besties", True, (255, 255, 255))
            screen.blit(besties_text, (10, 130))
            besties_in_harmony.timer += 1
            if besties_in_harmony.timer == besties_in_harmony.duration:
                besties_in_harmony.timer = 0
                besties_in_harmony.active = False
                LollyCar.change_car_image(lolly, 'normal')
                BestieCar.change_car_image(bestie, 'normal')
                besties_in_harmony.add_cooldown(15)
                besties_in_harmony.remove_from_screen()
      
        if player_eliminated: # if at least one player is eliminated, the gal pal rebirth power up is spawned)
            gal_pal_text = score_font.render("Gal Pal", True, (255, 255, 255))
            screen.blit(gal_pal_text, (10, 250))
            diva_defiance.timer += 1
            if gal_pal_rebirth.active:
                gal_pal_rebirth.timer += 1
                if gal_pal_rebirth.timer == gal_pal_rebirth.duration:
                    gal_pal_rebirth.timer = 0
                    gal_pal_rebirth.active = False
                    gal_pal_rebirth.remove_from_screen()
                    gal_pal_rebirth.add_cooldown(15)

        if diva_defiance.active: # if the diva defiance power up is active, the players dont take damage from cars
            LollyCar.change_car_image(lolly, 'diva')
            BestieCar.change_car_image(bestie, 'diva')
            diva_text = score_font.render("Diva", True, (255, 255, 255))
            screen.blit(diva_text, (10, 170))
            if diva_defiance.timer == diva_defiance.duration:
                diva_defiance.timer = 0
                diva_defiance.active = False
                diva_defiance.remove_from_screen()
                diva_defiance.add_cooldown(15)
                LollyCar.change_car_image(lolly, 'normal')
                BestieCar.change_car_image(bestie, 'normal')

            
        if frosty_frenzy.active:  # if the frosty frenzy power-up is active, the cars move slower
            frosty_text = score_font.render("Frosty", True, (255, 255, 255))
            screen.blit(frosty_text, (10, 210))
            for car in left_incoming_cars:
                car.speed = -6
            frosty_frenzy.timer += 1
            if frosty_frenzy.timer == frosty_frenzy.duration:
                frosty_frenzy.timer = 0
                frosty_frenzy.active = False
                frosty_frenzy.add_cooldown(15)
                frosty_frenzy.remove_from_screen()
                road = pygame.image.load("images/road.png")
                for car in left_incoming_cars:
                    car.speed = random.randint(-1, 2)

            
        if gal_pal_rebirth.active: # if the gal pal rebirth power up is active, the players are revived
            gal_pal_rebirth.timer += 1
            gal_pal_text = score_font.render("Gal Pal", True, (255, 255, 255))
            screen.blit(gal_pal_text, (10, 250))
            if gal_pal_rebirth.timer == gal_pal_rebirth.duration:
                gal_pal_rebirth.timer = 0
                gal_pal_rebirth.active = False
                gal_pal_rebirth.remove_from_screen()
                gal_pal_rebirth.add_cooldown(15)
        
        if tangled_twist.active:  # if the tangled twist power-up is active, the controls are reversed
            tangled_twist_text = score_font.render("Tangle Twist", True, (255, 255, 255))
            screen.blit(tangled_twist_text, (10, 290))
            tangled_twist.timer += 1
            if LollyCar.health == 0:  # if the player is alive, they can move
                if keys[pygame.K_LEFT]:
                    BestieCar.move_left(20)
                if keys[pygame.K_RIGHT]:
                    BestieCar.move_right(20)
                if keys[pygame.K_UP]:
                    BestieCar.move_up(20)
                    if BestieCar.rect.y < 0:
                        BestieCar.rect.y = 0
                if keys[pygame.K_DOWN]:
                    BestieCar.move_down(20)
                    if BestieCar.rect.y > 800:
                        BestieCar.rect.y = 800
            if BestieCar.health == 0:
                if keys[pygame.K_a]:
                    LollyCar.move_left(20)
                if keys[pygame.K_d]:
                    LollyCar.move_right(20)
                if keys[pygame.K_w]:
                    LollyCar.move_up(20)
                    if LollyCar.rect.y < 0:
                        LollyCar.rect.y = 0
                if keys[pygame.K_s]:
                    LollyCar.move_down(20)
                    if LollyCar.rect.y > 800:
                        LollyCar.rect.y = 800
            if tangled_twist.timer == tangled_twist.duration:
                tangled_twist.timer = 0
                tangled_twist.active = False
                tangled_twist.remove_from_screen()
                tangled_twist.add_cooldown(15)
                LollyCar.change_car_image(lolly, 'normal')
                BestieCar.change_car_image(bestie, 'normal')
        
        if glamorous_growth.active:  # if the glamorous growth power-up is active, the players grow
            glamorous_text = score_font.render("Glamorous", True, (255, 255, 255))
            screen.blit(glamorous_text, (10, 330))
            glamorous_growth.timer += 1
            if glamorous_growth.timer == glamorous_growth.duration:
                glamorous_growth.timer = 0
                glamorous_growth.active = False
                glamorous_growth.remove_from_screen()
                glamorous_growth.add_cooldown(15)
                LollyCar.player_resize()
                BestieCar.player_resize()

        if sissy_that_walk.active:  # if the sissy that walk power-up is active, the players move faster
            sissy_text = score_font.render("Sissy", True, (255, 255, 255))
            screen.blit(sissy_text, (10, 370))
            sissy_that_walk.timer += 1
            sissy_that_walk.affect_both_players(LollyCar, BestieCar, 10)
            if sissy_that_walk.timer == sissy_that_walk.duration:
                sissy_that_walk.timer = 0
                sissy_that_walk.active = False
                sissy_that_walk.affect_both_players(LollyCar, BestieCar, 0)
                sissy_that_walk.give_cooldown(15)
                sissy_that_walk.remove_from_screen()

        
        if toy_transforminator.active:  # if the toy transforminator power-up is active, the cars shrink
            toy_text = score_font.render("TOY", True, (255, 255, 255))
            screen.blit(toy_text, (10, 310))
            toy_transforminator.timer += 1
            if toy_transforminator.timer == toy_transforminator.duration:
                toy_transforminator.timer = 0
                toy_transforminator.active = False
                toy_transforminator.add_cooldown(15)
                toy_transforminator.remove_from_screen()
                for car in left_incoming_cars:
                    car.move_down(15)
                    if car.rect.y > 950:
                        new_car = random.choice(cars_images_left)
                        car.change_image(new_car[0], new_car[1], new_car[2], new_car[3], new_car[4])
                        car.add_speed(random.randint(-1, 3))
                        car.rect.y = random.randint(-2200, -800)
                        car.rect.x = random.choice([285, 466, 643, 825])
        
        ''' Cooldowns Reset and '''

        if besties_in_harmony.cooldown > 0:
            besties_in_harmony.cooldown -= 1
            if besties_in_harmony.cooldown == 0:
                power_ups.remove(besties_in_harmony)
                besties_in_harmony.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                besties_in_harmony.move_down(0)

        if diva_defiance.cooldown > 0:
            diva_defiance.cooldown -= 1
            if diva_defiance.cooldown == 0:
                power_ups.remove(diva_defiance)
                diva_defiance.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                diva_defiance.move_down(0)

        if frosty_frenzy.cooldown > 0:
            frosty_frenzy.cooldown -= 1
            if frosty_frenzy.cooldown == 0:
                power_ups.remove(frosty_frenzy)
                frosty_frenzy.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                frosty_frenzy.move_down(0)

        if gal_pal_rebirth.cooldown > 0:
            gal_pal_rebirth.cooldown -= 1
            if gal_pal_rebirth.cooldown == 0:
                power_ups.remove(gal_pal_rebirth)
                gal_pal_rebirth.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                gal_pal_rebirth.move_down(0)

        if tangled_twist.cooldown > 0:
            tangled_twist.cooldown -= 1
            if tangled_twist.cooldown == 0:
                power_ups.remove(tangled_twist)
                tangled_twist.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                tangled_twist.move_down(0)

        if glamorous_growth.cooldown > 0:
            glamorous_growth.cooldown -= 1
            if glamorous_growth.cooldown == 0:
                power_ups.remove(glamorous_growth)
                glamorous_growth.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                glamorous_growth.move_down(0)

        if sissy_that_walk.cooldown > 0:
            sissy_that_walk.cooldown -= 1
            if sissy_that_walk.cooldown == 0:
                power_ups.remove(sissy_that_walk)
                sissy_that_walk.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                sissy_that_walk.move_down(0)

        if toy_transforminator.cooldown > 0:
            toy_transforminator.cooldown -= 1
            if toy_transforminator.cooldown == 0:
                power_ups.remove(toy_transforminator)
                toy_transforminator.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                toy_transforminator.move_down(0)

        speed_effect = ["images/power_ups_visuals/sissy/sissy1.png", "images/power_ups_visuals/sissy/sissy2.png", "images/power_ups_visuals/sissy/sissy3.png"]
        if sissy_that_walk.active:
            screen.blit(pygame.image.load(random.choice(speed_effect)), (0, 0))

        ''' Score '''

        score += 1

        ''' Drawing Everything '''
        if frosty_frenzy.active:
            road = pygame.image.load("images/power_ups_visuals/frosty/road_snow.png")

        # score counter
        health_text = score_font.render(f"Health: {LollyCar.health}", True, (255, 255, 255))
        screen.blit(health_text, (10, 50))
        health_text = score_font.render(f"Health: {BestieCar.health}", True, (255, 255, 255))
        screen.blit(health_text, (10, 90))
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))


        ''' Drawing Everything '''
        all_sprites_list.update(all_sprites_list)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def game_over(road, difficulty, lolly, bestie, power_ups):


    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    ''' Loading Images '''

    game_over_image = pygame.image.load("images/game_over/game_over.png").convert_alpha()
    game_over_restart_image = pygame.image.load("images/game_over/game_over_restart.png").convert_alpha()
    game_over_exit_image = pygame.image.load("images/game_over/game_over_exit.png").convert_alpha()

    center_game_over_coord = ((1250 - 792) // 2, (950 - 792) // 2)
    pygame.display.flip()
    #(445, 295), (905, 400)] this are coordinates for a button called retry
    #[(450, 430), (770, 520)] this are coordinates for a button called exit
    restart_button_coor = 445, 295, 820, 400
    back_button_coor = 495, 420, 750, 520

    clock = pygame.time.Clock()
    road_y = 0

    carry_on = True
    event = pygame.event.Event(pygame.USEREVENT)  # Initialize event outside the loop with a default event


    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False

        screen.blit(road, (0, 0))
        scroll_speed = 3000
        dt = clock.tick(60) / 1000.0
        road_y += scroll_speed * dt

        if road_y >= 950:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - 950))

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        if keys[pygame.K_RETURN]:
            carry_on = False

        if keys[pygame.K_BACKSPACE]:
            carry_on = False

        if restart_button_coor[0] <= mouse[0] <= restart_button_coor[2] and restart_button_coor[1] < mouse[1] < restart_button_coor[3]:
            screen.blit(game_over_restart_image, center_game_over_coord)
            if event.type == pygame.MOUSEBUTTONDOWN:
                carry_on = False
                multi_game(difficulty, lolly, bestie, power_ups)
        elif back_button_coor[0] <= mouse[0] <= back_button_coor[2] and back_button_coor[1] < mouse[1] < back_button_coor[3]:
            screen.blit(game_over_exit_image, center_game_over_coord)
            if event.type == pygame.MOUSEBUTTONDOWN:
                carry_on = False
                pygame.quit()
        
        else:
            screen.blit(game_over_image, center_game_over_coord)

        pygame.display.flip()

    pygame.quit()

    return True
