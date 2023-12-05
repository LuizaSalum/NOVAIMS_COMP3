import pygame
import random
from car import *
from power_up import *


def multi_game(difficulty, lolly_car, bestie_car):

    pygame.init() # for pygame
    pygame.mixer.init() # for sound
    pygame.font.init() # for text

    # Setting up the screen

    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly's Locket Dog Chase")

    # Importing Images

    # road

    normal_road = pygame.image.load("images/road.png").convert()
    normal_road2 = pygame.image.load("images/road2.png").convert()
    normal_road3 = pygame.image.load("images/road3.png").convert()
    road = normal_road

    # frozen road (for frosty frenzy power up)

    frozen_road = pygame.image.load("images/power_ups_visuals/frosty/road_snow.png").convert()
    frozen_road2 = pygame.image.load("images/power_ups_visuals/frosty/road2_snow.png").convert()
    frozen_road3 = pygame.image.load("images/power_ups_visuals/frosty/road3_snow.png").convert()
    snow_sky = pygame.image.load("images/power_ups_visuals/frosty/snow_sky.png").convert_alpha()
    snow_snowflakes = pygame.image.load("images/power_ups_visuals/frosty/snow_snowflakes.png").convert_alpha()

    # speed lines (for sissy that walk power up)

    speed_images = [
        pygame.image.load("images/power_ups_visuals/sissy/sissy1.png").convert_alpha(),
        pygame.image.load("images/power_ups_visuals/sissy/sissy2.png").convert_alpha(),
        pygame.image.load("images/power_ups_visuals/sissy/sissy3.png").convert_alpha()
    ]  # this is a list because we will be randomising the speed lines when the power up is active

    # score bar

    score_bar = pygame.image.load("images/score_bar.png").convert()

    # Creating and positioning the players cars and their hearts (lives) images. Also adding them to a group

    lolly = PlayerCar(lolly_car, difficulty)
    lolly.heart_on = pygame.image.load(f"images/hearts/heart{lolly_car[-1]}.png").convert_alpha()  # the lolly_car[-1] gives me the car number equivalent to the heart (1, 2 or 3)
    lolly.heart_off = pygame.image.load(f"images/hearts/heart{lolly_car[-1]}_loss.png").convert_alpha()
    bestie = PlayerCar(bestie_car, difficulty)
    bestie.heart_on = pygame.image.load(f"images/hearts/heart{bestie_car[-1]}.png").convert_alpha()
    bestie.heart_off = pygame.image.load(f"images/hearts/heart{bestie_car[-1]}_loss.png").convert_alpha()

    lolly.rect.x = 285
    lolly.rect.y = 800
    bestie.rect.x = 466
    bestie.rect.y = 850

    sprite_lolly = pygame.sprite.Group()
    sprite_bestie = pygame.sprite.Group()
    players_cars = pygame.sprite.Group()
    sprite_lolly.add(lolly)
    players_cars.add(lolly)
    sprite_bestie.add(bestie)
    players_cars.add(bestie)

    # Creating, positioning and adding the traffic cars to a group

    if difficulty != 'hard':

        cars_list = []
        incoming_cars = pygame.sprite.Group()

        left_car1 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        cars_list.append(left_car1)
        left_car2 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        cars_list.append(left_car2)
        left_car3 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        cars_list.append(left_car3)
        left_car4 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        cars_list.append(left_car4)

        for car in cars_list:
            car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
            incoming_cars.add(car)

    elif difficulty == 'hard':

        cars_list_left = []
        cars_list_right = []
        incoming_cars_left = pygame.sprite.Group()
        incoming_cars_right = pygame.sprite.Group()

        left_car1 = TrafficCar(random.randint(1, 32), 'left', 'hard')
        cars_list_left.append(left_car1)
        left_car2 = TrafficCar(random.randint(1, 32), 'left', 'hard')
        cars_list_left.append(left_car2)
        right_car1 = TrafficCar(random.randint(1, 32), 'right', 'hard')
        cars_list_right.append(right_car1)
        right_car2 = TrafficCar(random.randint(1, 32), 'right', 'hard')
        cars_list_right.append(right_car2)

        for car in cars_list_left:
            car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
            incoming_cars_left.add(car)
        for car in cars_list_right:
            car.set_position(random.choice([643, 825]), random.randint(-1500, -100))
            incoming_cars_right.add(car)

    # Creating, positioning and adding the power ups to a group

    power_ups_list = []
    power_ups = pygame.sprite.Group()

    besties = BestiesInHarmony(difficulty)
    power_ups_list.append(besties)
    galpal = GalPalRebirth(difficulty)
    power_ups_list.append(galpal)
    tangled = TangledTwist(difficulty)
    power_ups_list.append(tangled)
    sissy = SissyThatWalk(difficulty)
    power_ups_list.append(sissy)
    diva = DivaDefiance(difficulty)
    power_ups_list.append(diva)
    growth = GlamorousGrowth(difficulty)
    power_ups_list.append(growth)
    frosty = FrostyFrenzy(difficulty)
    power_ups_list.append(frosty)
    toy = ToyTransforminator(difficulty)
    power_ups_list.append(toy)

    for power_up in power_ups_list:
        power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
        power_ups.add(power_up)

    # Adding sprites to the all_sprites group

    all_sprites = pygame.sprite.Group()
    all_sprites.add(lolly)
    all_sprites.add(bestie)

    if difficulty != 'hard':
        for car in cars_list:
            all_sprites.add(car)
    elif difficulty == 'hard':
        for car in cars_list_left:
            all_sprites.add(car)
        for car in cars_list_right:
            all_sprites.add(car)

    for power_up in power_ups_list:
        all_sprites.add(power_up)

    # Setting up Variables

    score = 0
    road_y = 0

    carryOn = True

    clock = pygame.time.Clock()

    countdown(road)  # countdown function before the game starts

    while carryOn:

        score += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            game_screen = pygame.Surface(screen.get_size())
            game_screen.blit(screen, (0, 0))
            pause_menu(game_screen)

        # Player Car Movement

        if not lolly.controls_inverted:
            if keys[pygame.K_w]:
                lolly.move_up()
            if keys[pygame.K_s]:
                lolly.move_down()
            if keys[pygame.K_a]:
                lolly.move_left()
            if keys[pygame.K_d]:
                lolly.move_right()
        else:
            if keys[pygame.K_UP]:
                lolly.move_up()
            if keys[pygame.K_DOWN]:
                lolly.move_down()
            if keys[pygame.K_LEFT]:
                lolly.move_left()
            if keys[pygame.K_RIGHT]:
                lolly.move_right()

        if not bestie.controls_inverted:
            if keys[pygame.K_UP]:
                bestie.move_up()
            if keys[pygame.K_DOWN]:
                bestie.move_down()
            if keys[pygame.K_LEFT]:
                bestie.move_left()
            if keys[pygame.K_RIGHT]:
                bestie.move_right()
        else:
            if keys[pygame.K_w]:
                bestie.move_up()
            if keys[pygame.K_s]:
                bestie.move_down()
            if keys[pygame.K_a]:
                bestie.move_left()
            if keys[pygame.K_d]:
                bestie.move_right()

        # Updating the sprites

        all_sprites.update()

        # Road Scroll and changes according to score

        # defining the road image

        if score < 2000:
            road = normal_road
        elif 2000 < score < 4000:
            road = normal_road2
        else:
            road = normal_road3

        # scrolling the road

        if sissy.active:
            scroll_speed = 5000
        elif frosty.active:
            scroll_speed = 2000
        else:
            scroll_speed = 3000
        
        road_y += scroll_speed * clock.tick(60) / 1000  # we're multiplying the scroll speed by the clock tick to make the scrolling speed independent of the frame rate

        if road_y > 950:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - 950))

        # Incoming Cars

        # adding cars over time (score)

        if difficulty == 'easy':
            # every 1000 points, a new car is added, until there are 6 cars
            if score > 1000 and score % 1000 == 0 and len(cars_list) < 6:
                new_car = TrafficCar(random.randint(1, 32), 'left', 'easy')
                cars_list.append(new_car)
                incoming_cars.add(new_car)

        elif difficulty == 'normal':
            # every 500 points, a new car is added, until there are 8 cars
            if score > 500 and score % 500 == 0 and len(cars_list) < 8:
                new_car = TrafficCar(random.randint(1, 32), 'left', 'normal')
                cars_list.append(new_car)
                incoming_cars.add(new_car)

        elif difficulty == 'hard':
            # every 500 points, a new car is added, until there are 8 cars randomly on the left or right
            if len(cars_list_left) + len(cars_list_right) < 8:
                random_side = random.choice(['left', 'right'])
                if random_side == 'left':
                    new_car = TrafficCar(random.randint(1, 32), 'left', 'hard')
                    cars_list_left.append(new_car)
                    incoming_cars_left.add(new_car)
                elif random_side == 'right':
                    new_car = TrafficCar(random.randint(1, 32), 'right', 'hard')
                    cars_list_right.append(new_car)
                    incoming_cars_right.add(new_car)

        # if the cars go off the screen, they are repositioned and given a new image

        if difficulty != 'hard':
            for car in cars_list:
                car.move_down(random.randint(10,13))
                if car.rect.y > 950:
                    new_car_number = random.randint(1, 32)
                    car.change_car(new_car_number, 'left', 'normal')
                    car.add_speed(random.randint(-1, 3))
                    car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))

        elif difficulty == 'hard':
            for car in cars_list_left:
                car.move_down(random.randint(10,13))
                if car.rect.y > 950:
                    new_car_number = random.randint(1, 32)
                    random_side = random.choice(['left', 'right'])
                    car.change_car(new_car_number, random_side, 'hard')
                    car.add_speed(random.randint(-1, 3))
                    if random_side == 'left':
                        car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                    elif random_side == 'right':
                        car.set_position(random.choice([643, 825]), random.randint(-1500, -100))
            for car in cars_list_right:
                car.move_down(random.randint(10,13))
                if car.rect.y > 950:
                    new_car_number = random.randint(1, 32)
                    random_side = random.choice(['left', 'right'])
                    car.change_car(new_car_number, random_side, 'hard')
                    car.add_speed(random.randint(-1, 3))
                    if random_side == 'left':
                        car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                    elif random_side == 'right':
                        car.set_position(random.choice([643, 825]), random.randint(-1500, -100))

        # Collision Detection

        # collision between players

        if lolly.can_collide and bestie.can_collide:
            # if there's a collision betwen the rectangles, then check for collision between the masks
            if pygame.sprite.collide_rect(lolly, bestie):
                # spritecollide(sprite, group, boolean (True if the sprite should be killed), collision method)
                if pygame.sprite.spritecollide(lolly, sprite_bestie, False, pygame.sprite.collide_mask):
                    if lolly.rect.x < bestie.rect.x:
                        lolly.rect.x -= 20
                        bestie.rect.x += 20
                    else:
                        lolly.rect.x += 20
                        bestie.rect.x -= 20
        
        # collision between players and traffic cars

        if lolly.can_crash:

            if difficulty != 'hard':

                for traffic_car in incoming_cars:
                    if pygame.sprite.collide_rect(lolly, traffic_car):
                        if pygame.sprite.spritecollide(lolly, incoming_cars, False, pygame.sprite.collide_mask):
                            lolly.add_health(-1)
                            traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                            
                            if lolly.health == 0 and bestie.health != 0:
                                lolly.die()
                            elif lolly.health == 0 and bestie.health == 0:
                                game_over(road, difficulty, lolly, bestie)

            elif difficulty == 'hard':

                for traffic_car in incoming_cars_left:
                    if pygame.sprite.collide_rect(lolly, traffic_car):
                        if pygame.sprite.spritecollide(lolly, incoming_cars_left, False, pygame.sprite.collide_mask):
                            lolly.add_health(-1)
                            traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                
                            if lolly.health == 0 and bestie.health != 0:
                                lolly.die()
                            elif lolly.health == 0 and bestie.health == 0:
                                game_over(road, difficulty, lolly, bestie)

                for traffic_car in incoming_cars_right:
                    if pygame.sprite.collide_rect(lolly, traffic_car):
                        if pygame.sprite.spritecollide(lolly, incoming_cars_right, False, pygame.sprite.collide_mask):
                            lolly.add_health(-1)
                            traffic_car.set_position(random.choice([643, 825]), random.randint(-1500, -100))
                
                            if lolly.health == 0 and bestie.health != 0:
                                lolly.die()
                            elif lolly.health == 0 and bestie.health == 0:
                                game_over(road, difficulty, lolly, bestie)

        if bestie.can_crash:

            if difficulty != 'hard':

                for traffic_car in incoming_cars:
                    if pygame.sprite.collide_rect(bestie, traffic_car):
                        if pygame.sprite.spritecollide(bestie, incoming_cars, False, pygame.sprite.collide_mask):
                            bestie.add_health(-1)
                            traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                
                            if bestie.health == 0 and lolly.health != 0:
                                bestie.die()
                            elif bestie.health == 0 and lolly.health == 0:
                                game_over(road, difficulty, lolly, bestie)

            elif difficulty == 'hard':

                for traffic_car in incoming_cars_left:
                    if pygame.sprite.collide_rect(bestie, traffic_car):
                        if pygame.sprite.spritecollide(bestie, incoming_cars_left, False, pygame.sprite.collide_mask):
                            bestie.add_health(-1)
                            traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                
                            if bestie.health == 0 and lolly.health != 0:
                                bestie.die()
                            elif bestie.health == 0 and lolly.health == 0:
                                game_over(road, difficulty, lolly, bestie)

                for traffic_car in incoming_cars_right:
                    if pygame.sprite.collide_rect(bestie, traffic_car):
                        if pygame.sprite.spritecollide(bestie, incoming_cars_right, False, pygame.sprite.collide_mask):
                            bestie.add_health(-1)
                            traffic_car.set_position(random.choice([643, 825]), random.randint(-1500, -100))
                
                            if bestie.health == 0 and lolly.health != 0:
                                bestie.die()
                            elif bestie.health == 0 and lolly.health == 0:
                                game_over(road, difficulty, lolly, bestie)

        # collision between traffic cars

        if difficulty != 'hard':

            for traffic_car_1 in incoming_cars:
                for traffic_car_2 in incoming_cars:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -200:
                                traffic_car_1.rect.y = random.randint(-2200, -800)
                                traffic_car_1.rect.x = random.choice([285, 466, 643, 825])
                            else:
                                traffic_car_2.speed = 0

        elif difficulty == 'hard':

            for traffic_car_1 in incoming_cars_left:
                for traffic_car_2 in incoming_cars_left:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -200:
                                traffic_car_1.rect.y = random.randint(-2200, -800)
                                traffic_car_1.rect.x = random.choice([285, 466])
                            else:
                                traffic_car_2.speed = 0

            for traffic_car_1 in incoming_cars_right:
                for traffic_car_2 in incoming_cars_right:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -200:
                                traffic_car_1.rect.y = random.randint(-2200, -800)
                                traffic_car_1.rect.x = random.choice([643, 825])
                            else:
                                traffic_car_2.speed = 0

        # collision between players and power ups

        for power_up in power_ups:
            if pygame.sprite.collide_rect(lolly, power_up):
                if pygame.sprite.spritecollide(lolly, power_ups, False, pygame.sprite.collide_mask):
                    if power_up == besties or power_up == galpal or power_up == tangled or power_up == sissy:
                        power_up.collision(lolly, bestie)
                    elif power_up == diva or power_up == growth:
                        power_up.collision(lolly)
                    elif power_up == frosty or power_up == toy:
                        if difficulty != 'hard':
                            power_up.collision(lolly, bestie, incoming_cars)
                        elif difficulty == 'hard':
                            power_up.collision(lolly, bestie, incoming_cars_left, incoming_cars_right)
            if pygame.sprite.collide_rect(bestie, power_up):
                if pygame.sprite.spritecollide(bestie, power_ups, False, pygame.sprite.collide_mask):
                    if power_up == besties or power_up == galpal or power_up == tangled or power_up == sissy:
                        power_up.collision(lolly, bestie)
                    elif power_up == diva or power_up == growth:
                        power_up.collision(bestie)
                    elif power_up == frosty or power_up == toy:
                        if difficulty != 'hard':
                            power_up.collision(lolly, bestie, incoming_cars)
                        elif difficulty == 'hard':
                            power_up.collision(lolly, bestie, incoming_cars_left, incoming_cars_right)

        # Power Ups Activation

        if not (lolly.eliminated or bestie.eliminated):
            galpal.unavailable = True  # the gal pal rebirth power up is unavailable if both players are alive
        else:
            # if one of the players is eliminated, then the gal pal rebirth power up is available
            galpal.unavailable = False
            # but besties in harmony and tangled twist are unavailable
            besties.unavailable = True
            tangled.unavailable = True

        # Drawing the Sprites

        if frosty.active:
            if score < 2000:
                road = frozen_road
            elif score < 4000:
                road = frozen_road2
            else:
                road = frozen_road3

        lolly.change_image(active_power_ups(besties, diva, growth, tangled))
        bestie.change_image(active_power_ups(besties, diva, growth, tangled))

        all_sprites.update()
        all_sprites.draw(screen)

        # Drawing the Power Ups that change the road and screen

        if frosty.active:
            screen.blit(snow_sky, (0, 0))
            screen.blit(snow_snowflakes, (0, 0))

        if sissy.active:
            screen.blit(random.choice(speed_images), (0, 0))

        # Drawing the Score Bar

        score_bar_font = pygame.font.SysFont('comic_sans', 55)
        border_colour = (55, 18, 26)

        score_text = score_bar_font.render(f"{score}", True, (255, 255, 255))
        offsets = [
            (-3, -3), (-2, -3), (-1, -3), (0, -3), (1, -3), (2, -3), (3, -3),
            (-3, -2), (3, -2), (-3, -1), (3, -1), (-3, 0), (3, 0), (-3, 1), (3, 1),
            (-3, 2), (3, 2), (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3)
        ]

        screen.blit(score_bar, (0, 0))

        for offset in offsets:
            screen.blit(score_bar_font.render(f"{score}", True, border_colour), (170 + offset[0], offset[1]))

        screen.blit(score_text, (170, 0))

        # Drawing the Hearts (Lives)

        for HP in range(lolly.max_health):
            if HP < lolly.health:
                screen.blit(lolly.heart_on, (480 + HP * 75, 5))
            else:
                screen.blit(lolly.heart_off, (480 + HP * 75, 5))
        
        for HP in range(bestie.max_health):
            if HP < bestie.health:
                screen.blit(bestie.heart_on, (870 + HP * 75, 5))
            else:
                screen.blit(bestie.heart_off, (870 + HP * 75, 5))

        # Drawing the Power Ups Bar (on the left side of the screen)

        icon_position = 30
        for icon in power_ups_bar(besties.active, diva.active, growth.active, tangled.active, sissy.active, frosty.active, toy.active):
            icon_position += 80
            screen.blit(icon, (0, icon_position))

        # Updating the Display

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def countdown(game_screen):

    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    beeps = pygame.mixer.Sound("sounds/countdown/beeps.mp3")
    go = pygame.mixer.Sound("sounds/countdown/go.mp3")
    beeps.set_volume(0.5)
    go.set_volume(0.5)

    ''' Loading Images '''

    countdown_3 = pygame.image.load("images/countdown/countdown_3.png").convert_alpha()
    countdown_2 = pygame.image.load("images/countdown/countdown_2.png").convert_alpha()
    countdown_1 = pygame.image.load("images/countdown/countdown_1.png").convert_alpha()
    countdown_go = pygame.image.load("images/countdown/countdown_go.png").convert_alpha()

    screen.blit(game_screen, (0, 0))
    screen.blit(countdown_3, (0, 0))
    beeps.play()
    pygame.display.flip()

    pygame.time.wait(1000)
    screen.blit(game_screen, (0, 0))
    screen.blit(countdown_2, (0, 0))
    beeps.play()
    pygame.display.flip()

    pygame.time.wait(1000)
    screen.blit(game_screen, (0, 0))
    screen.blit(countdown_1, (0, 0))
    beeps.play()
    pygame.display.flip()

    pygame.time.wait(1000)
    screen.blit(game_screen, (0, 0))
    screen.blit(countdown_go, (0, 0))
    go.play()
    pygame.display.flip()

    pygame.time.wait(1500)
    return

def game_over(road, difficulty, lolly, bestie):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    ''' Loading Images '''

    game_over_image = pygame.image.load("images/game_over/game_over.png").convert_alpha()
    game_over_restart_image = pygame.image.load("images/game_over/game_over_restart.png").convert_alpha()
    game_over_exit_image = pygame.image.load("images/game_over/game_over_exit.png").convert_alpha()

    center_game_over_coord = ((1250 - 792) // 2, (950 - 792) // 2)
    pygame.display.flip()

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
                multi_game(difficulty, lolly.car_type, bestie.car_type)
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

def pause_menu(game_screen):

    menu_position = [451, 799, 326, 624]  # x1, x2, y1, y2
    buttons = (
        ['done', 544, 709, 376, 447],
        ['exit', 528, 723, 501, 572]
        )
    
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    ''' Loading Images '''

    pause_menu_image = pygame.image.load("images/interface/pause.png").convert_alpha()
    pause_menu_done_image = pygame.image.load("images/interface/pause_done.png").convert_alpha()
    pause_menu_exit_image = pygame.image.load("images/interface/pause_exit.png").convert_alpha()

    screen.blit(game_screen, (0, 0))
    screen.blit(pause_menu_image, (menu_position[0], menu_position[2]))
    pygame.display.flip()

    paused = True

    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            mouse = pygame.mouse.get_pos()

            if buttons[0][1] <= mouse[0] <= buttons[0][2] and buttons[0][3] < mouse[1] < buttons[0][4]:  # if the user hovers over the done button
                screen.blit(pause_menu_done_image, (menu_position[0], menu_position[2]))
                if event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the done button
                    paused = False

            elif buttons[1][1] <= mouse[0] <= buttons[1][2] and buttons[1][3] < mouse[1] < buttons[1][4]:  # if the user hovers over the exit button
                screen.blit(pause_menu_exit_image, (menu_position[0], menu_position[2]))
                if event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the exit button
                    pygame.quit()

            elif not (menu_position[0] <= mouse[0] <= menu_position[1] and menu_position[2] < mouse[1] < menu_position[3]):  # if the user hovers over anywhere else
                screen.blit(pause_menu_image, (menu_position[0], menu_position[2]))
                if event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks anywhere else
                    paused = False
                    
        pygame.display.flip()

def active_power_ups(besties, diva, growth, tangled):

    active_combination = 'normal'

    if besties.active and not diva.active and not growth.active and not tangled.active:  # if the besties in harmony power up is active
        active_combination = 'besties'
    if besties.active and not diva.active and not growth.active and tangled.active:  # if the besties in harmony and tangled twist power ups are active
        active_combination = 'besties_tangled'
    if besties.active and not diva.active and growth.active and not tangled.active:  # if the besties in harmony and glamorous growth power ups are active
        active_combination = 'besties_growth'
    if besties.active and not diva.active and growth.active and tangled.active:  # if the besties in harmony, glamorous growth and tangled twist power ups are active
        active_combination = 'besties_tangled_growth'
    if besties.active and diva.active and not growth.active and not tangled.active:  # if the besties in harmony and diva defiance power ups are active
        active_combination = 'besties_diva'
    if besties.active and diva.active and not growth.active and tangled.active:  # if the besties in harmony, diva defiance and tangled twist power ups are active
        active_combination = 'besties_diva_tangled'
    if besties.active and diva.active and growth.active and not tangled.active:  # if the besties in harmony, diva defiance and glamorous growth power ups are active
        active_combination = 'besties_diva_growth'
    if besties.active and diva.active and growth.active and tangled.active:  # if the besties in harmony, diva defiance, glamorous growth and tangled twist power ups are active
        active_combination = 'besties_diva_tangled_growth'
    if not besties.active and not diva.active and not growth.active and tangled.active:  # if the tangled twist power up is active
        active_combination = 'tangled'
    if not besties.active and not diva.active and growth.active and not tangled.active:  # if the glamorous growth power up is active
        active_combination = 'growth'
    if not besties.active and not diva.active and growth.active and tangled.active:  # if the glamorous growth and tangled twist power ups are active
        active_combination = 'tangled_growth'
    if not besties.active and diva.active and not growth.active and not tangled.active:  # if the diva defiance power up is active
        active_combination = 'diva'
    if not besties.active and diva.active and not growth.active and tangled.active:  # if the diva defiance and tangled twist power ups are active
        active_combination = 'diva_tangled'
    if not besties.active and diva.active and growth.active and not tangled.active:  # if the diva defiance and glamorous growth power ups are active
        active_combination = 'diva_growth'
    if not besties.active and diva.active and growth.active and tangled.active:  # if the diva defiance, glamorous growth and tangled twist power ups are active
        active_combination = 'diva_tangled_growth'

    return active_combination

def power_ups_bar(besties, diva, growth, tangled, sissy, frosty, toy):

    power_ups = []
    power_ups_names = ["besties_in_harmony", "diva_defiance", "frosty_frenzy", "gal_pal_rebirth", "tangled_twist", "glamorous_growth", "sissy_that_walk", "toy_transforminator"]
    power_ups_boolean_list = [besties, diva, frosty, tangled, growth, sissy, toy]

    for number in range(len(power_ups_boolean_list)):
        if power_ups_boolean_list[number]:
            power_ups.append(pygame.image.load(f"images/power_ups/{power_ups_names[number]}.png").convert_alpha())
        else:
            power_ups.append(pygame.image.load(f"images/power_ups/{power_ups_names[number]}_off.png").convert_alpha())
    
    return power_ups
