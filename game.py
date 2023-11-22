import pygame
import random
from car import TrafficCar, Car1, Car2, Car3
from power_up import PowerUp

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


def multi_game(difficulty, lolly_car, bestie_car, power_ups):
    pygame.init()

    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    ''' Importing images'''

    # road
    road = pygame.image.load("images/road.png").convert()

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

    car_1 = [f"images/players_cars/car1.png", 144, 222, 98, 202]
    car_2 = [f"images/players_cars/car2.png", 122, 245, 122, 245]
    car_3 = [f"images/players_cars/car3.png", 132, 229, 132, 228]

    players_cars.append(car_1)
    players_cars.append(car_2)
    players_cars.append(car_3)

    # power ups

    image_besties_in_harmony = "images/power_ups/besties_in_harmony.png"
    # don't lose HP if you crash into your bestie
    image_diva_defiance = "images/power_ups/diva_defiance.png"
    # invulnerability
    image_frosty_frenzy = "images/power_ups/frosty_frenzy.png"
    # the traffic slows down
    image_gal_pal_rebirth = "images/power_ups/gal_pal_rebirth.png"
    # an eliminated player is revived
    image_girly_dash = "images/power_ups/girly_dash.png"
    # car can dash/jump forward (space for lolly and enter for bestie)
    image_glamorous_growth = "images/power_ups/glamorous_growth.png"
    # the car grows in size and gain HP
    image_sissy_that_walk = "images/power_ups/sissy_that_walk.png"
    # speed boost
    image_toy_transforminator = "images/power_ups/toy_transforminator.png"
    # traffic shrinks in size and loses HP

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
    
    if lolly_car == 'car1':
        LollyCar = Car1(car_1[0], car_1[1], car_1[2], car_1[3], car_1[4])
        LollyCar.rect.x = 466
        LollyCar.rect.y = 800
        
    if lolly_car == 'car2':
        LollyCar = Car2(car_2[0], car_2[1], car_2[2], car_2[3], car_2[4])
        LollyCar.rect.x = 466
        LollyCar.rect.y = 800
    
    if lolly_car == 'car3':
        LollyCar = Car3(car_3[0], car_3[1], car_3[2], car_3[3], car_3[4])
        LollyCar.rect.x = 466
        LollyCar.rect.y = 800
        
    if bestie_car == 'car1':
        BestieCar = Car1(car_1[0], car_1[1], car_1[2], car_1[3], car_1[4])
        BestieCar.rect.x = 285
        BestieCar.rect.y = 800
        
    if bestie_car == 'car2':
        BestieCar = Car2(car_2[0], car_2[1], car_2[2], car_2[3], car_2[4])
        BestieCar.rect.x = 285
        BestieCar.rect.y = 800
        
    if bestie_car == 'car3':
        BestieCar = Car3(car_3[0], car_3[1], car_3[2], car_3[3], car_3[4])
        BestieCar.rect.x = 285
        BestieCar.rect.y = 800

    ''' Positioning Power Ups '''

    ''' TO BE IMPLEMENTED
    
    if 'besties_in_harmony' in power_ups:
        besties_in_harmony = PowerUp(image_besties_in_harmony, 80, 80)
        besties_in_harmony.rect.x = random.randint(285, 466, 643, 825)
        besties_in_harmony.rect.y = random.randint(-1500, -100)
        besties_in_harmony_base_speed = 3
        besties_in_harmony_duration = 10
        besties_in_harmony_timer = 0
        besties_in_harmony_active = False
        besties_in_harmony_cooldown = 30
        
    '''

    if 'diva_defiance' in power_ups:
        diva_defiance = PowerUp(image_diva_defiance, 80, 80)
        diva_defiance.rect.x = random.choice([285, 466, 643, 825])
        diva_defiance.rect.y = random.randint(-1500, -100)
        diva_defiance_base_speed = 3
        diva_defiance_duration = 60
        diva_defiance_timer = 0
        diva_defiance_active = False
        diva_defiance_cooldown = 20

    if 'frosty_frenzy' in power_ups:
        frosty_frenzy = PowerUp(image_frosty_frenzy, 80, 80)
        frosty_frenzy.rect.x = random.choice([285, 466, 643, 825])
        frosty_frenzy.rect.y = random.randint(-1500, -100)
        frosty_frenzy_base_speed = 3
        frosty_frenzy_duration = 60
        frosty_frenzy_timer = 0
        frosty_frenzy_active = False
        frosty_frenzy_cooldown = 15

    if 'gal_pal_rebirth' in power_ups:
        if player_eliminated:
            gal_pal_rebirth = PowerUp(image_gal_pal_rebirth, 80, 80)
            gal_pal_rebirth.rect.x = random.randint(285, 466, 643, 825)
            gal_pal_rebirth.rect.y = random.randint(-1500, -100)
            gal_pal_rebirth_base_speed = 3
            gal_pal_rebirth_active = False
            gal_pal_rebirth_cooldown = 30

    
    ''' TO BE IMPLEMENTED
            
    if 'girly_dash' in power_ups:
        girly_dash = PowerUp(image_girly_dash, 80, 80)
        girly_dash.rect.x = random.randint(285, 466, 643, 825)
        girly_dash.rect.y = random.randint(-1500, -100)
        girly_dash_base_speed = 3
        girly_dash_duration = 5
        girly_dash_timer = 0
        girly_dash_active = False
        girly_dash_cooldown = 15
        
    if 'glamorous_growth' in power_ups:
        glamorous_growth = PowerUp(image_glamorous_growth, 80, 80)
        glamorous_growth.rect.x = random.randint(285, 466, 643, 825)
        glamorous_growth.rect.y = random.randint(-1500, -100)
        glamorous_growth_base_speed = 3
        glamorous_growth_duration = 5
        glamorous_growth_timer = 0
        glamorous_growth_active = False
        glamorous_growth_cooldown = 15
        
    '''

    if 'sissy_that_walk' in power_ups:
        sissy_that_walk = PowerUp(image_sissy_that_walk, 80, 80)
        sissy_that_walk.rect.x = random.randint(285, 466, 643, 825)
        sissy_that_walk.rect.y = random.randint(-1500, -100)
        sissy_that_walk_base_speed = 3
        sissy_that_walk_duration = 5
        sissy_that_walk_timer = 0
        sissy_that_walk_active = False
        sissy_that_walk_cooldown = 15

    ''' TO BE IMPLEMENTED
        
    if 'toy_transforminator' in power_ups:
        toy_transforminator = PowerUp(image_toy_transforminator, 80, 80)
        toy_transforminator.rect.x = random.randint(285, 466, 643, 825)
        toy_transforminator.rect.y = random.randint(-1500, -100)
        toy_transforminator_base_speed = 3
        toy_transforminator_duration = 5
        toy_transforminator_timer = 0
        toy_transforminator_active = False
        toy_transforminator_cooldown = 15
        
    '''

    ''' Adding Sprites to Group '''

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(LollyCar)
    all_sprites_list.add(BestieCar)
    all_sprites_list.add(left_incoming_cars)
    if difficulty == 'hard':
        all_sprites_list.add(right_incoming_cars)

    if 'besties_in_harmony' in power_ups:
        all_sprites_list.add(besties_in_harmony)
        
    if 'gal_pal_rebirth' in power_ups:
        all_sprites_list.add(gal_pal_rebirth)
        gal_pal_rebirth.cooldown(power_ups_cooldown_nerfer)
    if 'diva_defiance' in power_ups:
        all_sprites_list.add(diva_defiance)
        diva_defiance.add_duration(power_ups_duration_buffer)
        diva_defiance.add_cooldown(power_ups_cooldown_nerfer)
    if 'frosty_frenzy' in power_ups:
        all_sprites_list.add(frosty_frenzy)
        frosty_frenzy.add_duration(power_ups_duration_buffer)
        frosty_frenzy.add_cooldown(power_ups_cooldown_nerfer)
    if 'girly_dash' in power_ups:
        all_sprites_list.add(girly_dash)
    if 'glamorous_growth' in power_ups:
        all_sprites_list.add(glamorous_growth)
    if 'sissy_that_walk' in power_ups:
        all_sprites_list.add(sissy_that_walk)
    if 'toy_transforminator' in power_ups:
        all_sprites_list.add(toy_transforminator)

    ''' Setting Up Variables '''

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

    # starting the clock
    clock = pygame.time.Clock()

    while carryOn:

        score += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()

        ''' We should change this so it opens the pause menu instead of quitting the game.'''
        if keys[pygame.K_ESCAPE]:
            carryOn = False

        ''' Lolly controls '''

        if keys[pygame.K_a]:
            LollyCar.move_left(20)
            if 0 < LollyCar.rect.x < 230:
                LollyCar.rect.x = 230
        if keys[pygame.K_d]:
            LollyCar.move_right(20)
            if LollyCar.rect.x > 900:
                LollyCar.rect.x = 900
        if keys[pygame.K_w]:
            LollyCar.move_up(20)
            if LollyCar.rect.y < 0:
                LollyCar.rect.y = 0
        if keys[pygame.K_s]:
            LollyCar.move_down(20)
            if LollyCar.rect.y > 800:
                LollyCar.rect.y = 800

        ''' Bestie controls '''

        if keys[pygame.K_LEFT]:
            BestieCar.move_left(20)
            if 0 < BestieCar.rect.x < 230:
                BestieCar.rect.x = 230
        if keys[pygame.K_RIGHT]:
            BestieCar.move_right(20)
            if BestieCar.rect.x > 900:
                BestieCar.rect.x = 900
        if keys[pygame.K_UP]:
            BestieCar.move_up(20)
            if BestieCar.rect.y < 0:
                BestieCar.rect.y = 0
        if keys[pygame.K_DOWN]:
            BestieCar.move_down(20)
            if BestieCar.rect.y > 800:
                BestieCar.rect.y = 800

        all_sprites_list.update()

        ''' Scrolling the road '''

        # Scrolling the road
        scroll_speed = 1000
        dt = clock.tick(60) / 1000.0
        road_y += scroll_speed * dt

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

        ''' Collision Detection '''

        if difficulty != 'hard':

            for car_1 in left_incoming_cars:
                for car_2 in left_incoming_cars:
                    if car_1 != car_2 and car_1.rect.colliderect(car_2.rect):
                        if car_1.rect.y < -800 or car_2.rect.y < -200:
                            car_1.rect.y = random.randint(-2200, -800)
                            car_1.rect.x = random.choice([285, 466, 643, 825])
                        else:
                            car_1.add_speed(0)
            for car_1 in left_incoming_cars:
                if pygame.sprite.collide_rect(LollyCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466, 643, 825])
                    # if the player collides with a car, check if they have the diva defiance power up
                    if diva_defiance_active:
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
                        LollyCar.rect.x = -500
                        LollyCar.rect.y = -500
                        # this will hide the car from the screen, so it will look like it was eliminated
                        # if both players are eliminated, the game ends
                        if BestieCar.health == 0:
                            game_over()

                if pygame.sprite.collide_rect(BestieCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466, 643, 825])
                    if diva_defiance_active:
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                    elif BestieCar.health > 1:
                        BestieCar.add_health(-1)
                        car_1.rect.y = random.randint(-2200, -800)
                        car_1.rect.x = random.choice([285, 466, 643, 825])
                    elif BestieCar.health == 1:
                        BestieCar.add_health(-1)
                        BestieCar.rect.x = -500
                        BestieCar.rect.y = -500
                        if LollyCar.health == 0:
                            game_over()

        if difficulty == 'hard':

            for car_1 in left_incoming_cars:
                for car_2 in left_incoming_cars:
                    if car_1 != car_2 and car_1.rect.colliderect(car_2.rect):
                        if car_1.rect.y < -800 or car_2.rect.y < -200:
                            car_1.rect.y = random.randint(-2200, -800)
                            car_1.rect.x = random.choice([285, 466])
                        else:
                            car_1.add_speed(-car_2.speed)

                if pygame.sprite.collide_rect(LollyCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466])
                    if diva_defiance_active:
                        car_1.kill()
                    elif LollyCar.health > 1:
                        LollyCar.add_health(-1)
                        car_1.kill()
                    elif LollyCar.health == 1:
                        LollyCar.add_health(-1)
                        LollyCar.kill()
                        if BestieCar.health == 0:
                            game_over()

                if pygame.sprite.collide_rect(BestieCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([285, 466])
                    if diva_defiance_active:
                        car_1.kill()
                    elif BestieCar.health > 1:
                        BestieCar.add_health(-1)
                        car_1.kill()
                    elif BestieCar.health == 1:
                        BestieCar.add_health(-1)
                        BestieCar.rect.x = -2500
                        BestieCar.rect.y = -2500
                        if LollyCar.health == 0:
                            game_over()

            for car_1 in right_incoming_cars:
                for car_2 in right_incoming_cars:
                    if car_1 != car_2 and car_1.rect.colliderect(car_2.rect):
                        if car_1.rect.y < -800 or car_2.rect.y < -200:
                            car_1.rect.y = random.randint(-2200, -800)
                            car_1.rect.x = random.choice([643, 825])
                        else:
                            car_1.add_speed(-car_2.speed)

                if pygame.sprite.collide_rect(LollyCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([643, 825])
                    if diva_defiance_active:
                        car_1.kill()
                    elif LollyCar.health > 1:
                        LollyCar.add_health(-1)
                        car_1.kill()
                    elif LollyCar.health == 1:
                        LollyCar.add_health(-1)
                        LoLollyCar.rect.x = -2500
                        LollyCar.rect.y = -2500
                        if BestieCar.health == 0:
                            game_over()

                if pygame.sprite.collide_rect(BestieCar, car_1):
                    car_1.rect.y = random.randint(-2200, -800)
                    car_1.rect.x = random.choice([643, 825])
                    if diva_defiance_active:
                        car_1.kill()
                    elif BestieCar.health > 1:
                        BestieCar.add_health(-1)
                        car_1.kill()
                    elif BestieCar.health == 1:
                        BestieCar.add_health(-1)
                        BestieCar.rect.x = -500
                        BestieCar.rect.y = -500
                        if LollyCar.health == 0:
                            game_over()

        ''' Power Ups '''
        ''' Besties in Harmony '''

        ''' Diva Defiance '''

        diva_defiance.move_down(diva_defiance_base_speed)

        if diva_defiance.rect.y > 950:
            # if the power up is off the screen, it is removed and enters cooldown
            diva_defiance.kill()
            diva_defiance_cooldown = 20
        
        if pygame.sprite.collide_rect(LollyCar, diva_defiance) or pygame.sprite.collide_rect(BestieCar, diva_defiance):
            # if the power up is collected, it is removed and enters cooldown
            diva_defiance.kill()
            diva_defiance_cooldown = 20
            diva_defiance_active = True

        if diva_defiance_active:
            diva_defiance_timer += 1
            #FALTA ACABAR

            if diva_defiance_timer == diva_defiance_duration:
                diva_defiance_active = False
                diva_defiance_timer = 0
                diva_defiance_cooldown = 20
                diva_defiance.kill()

        ''' Frosty Frenzy '''

        frosty_frenzy.move_down(frosty_frenzy_base_speed)

        if frosty_frenzy.rect.y > 950:
            # if the power up is off the screen, it is removed and enters cooldown
            frosty_frenzy.kill()
            frosty_frenzy_cooldown = 15

        if pygame.sprite.collide_rect(LollyCar, frosty_frenzy) or pygame.sprite.collide_rect(BestieCar, frosty_frenzy):
            # if the power up is collected, it is removed and enters cooldown
            frosty_frenzy.kill()
            frosty_frenzy_cooldown = 15
            frosty_frenzy_active = True

        if frosty_frenzy_active:
            frosty_frenzy_timer += 1
            for car in left_incoming_cars:
                car.speed = -5
            if frosty_frenzy_timer == frosty_frenzy_duration:
                frosty_frenzy_active = False
                frosty_frenzy_timer = 0
                frosty_frenzy_cooldown = 15
                frosty_frenzy.kill()
                for car in left_incoming_cars:
                    car.speed = 0

        if frosty_frenzy_cooldown > 0:
            frosty_frenzy_cooldown -= 1
            if frosty_frenzy_cooldown == 0:
                frosty_frenzy.rect.x = random.choice([285, 466, 643, 825])
                frosty_frenzy.rect.y = random.randint(-1500, -100)
                all_sprites_list.add(frosty_frenzy)

        ''' Gal Pal Rebirth '''

        gal_pal_rebirth.move_down(gal_pal_rebirth_base_speed)

        if BestieCar.health == 0 or LollyCar.health == 0:
            player_eliminated = True
        else:
            player_eliminated = False

        if gal_pal_rebirth.rect.y > 950:
            # if the power up is off the screen, it is removed and enters cooldown
            gal_pal_rebirth.kill()
            gal_pal_rebirth_cooldown = 30

        if pygame.sprite.collide_rect(LollyCar, gal_pal_rebirth) or pygame.sprite.collide_rect(BestieCar, gal_pal_rebirth):
            # if the power up is collected, it is removed and enters cooldown
            gal_pal_rebirth.kill()
            gal_pal_rebirth_cooldown = 30
            gal_pal_rebirth_active = True

        if player_eliminated:
            if gal_pal_rebirth_active:
                gal_pal_rebirth_active = False
                gal_pal_rebirth_cooldown = 30
                gal_pal_rebirth.kill()
                if LollyCar.health == 0:
                    LollyCar.health = 1
                    LollyCar.rect.x = 466
                    LollyCar.rect.y = 800
                elif BestieCar.health == 0:
                    BestieCar.health = 1
                    BestieCar.rect.x = 285
                    BestieCar.rect.y = 800

            

        ''' Girly Dash '''

        ''' Glamorous Growth '''

        ''' Sissy That Walk '''

        ''' Toy Transforminator '''

        ''' Drawing Everything '''
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
