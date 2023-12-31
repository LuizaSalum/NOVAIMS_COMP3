import pygame
import random
from car import *
from power_up import *


def single_game(difficulty, lolly_car):

    """
    Run the singleplayer version of Lolly Locket's Dog Chase.

    Parameters
    ----------
    difficulty : str
        The difficulty level of the game ('easy', 'normal', 'hard').
    lolly_car : str
        The image file name of the player car.

    """

    pygame.mixer.init() # for sound
    pygame.init() # for pygame
    pygame.font.init() # for text

    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")  # sound for when the menu opens
    menu_open.set_volume(0.7)
    hp_loss = pygame.mixer.Sound("sounds/hp_loss.mpeg")
    hp_diva = pygame.mixer.Sound("sounds/hp_diva.mp3")
    hp_diva.set_volume(1.4)
    powerup_sound = pygame.mixer.Sound("sounds/powerup_sound.mpeg")

    # Setting up the screen

    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

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
    lolly.set_position(285, (950 - lolly.rect.height))  # the x position is different for each player car, set_position is a function from the Car class
   
    sprite_lolly = pygame.sprite.Group()
    players_cars = pygame.sprite.Group()
    sprite_lolly.add(lolly)
    players_cars.add(lolly)

    # Creating, positioning and adding the traffic cars to a group

    if difficulty == 'easy':

        cars_list = []
        incoming_cars = pygame.sprite.Group()

        left_car1 = TrafficCar(random.randint(1, 32), 'left', 'easy')  # TrafficCar(car_number (we have 32 images), direction of the car (left is for cars going downwards), difficulty)
        cars_list.append(left_car1)
        left_car2 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        cars_list.append(left_car2)
        left_car3 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        cars_list.append(left_car3)
        left_car4 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        cars_list.append(left_car4)

        for car in cars_list:
            car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
            incoming_cars.add(car)

    if difficulty == 'normal':

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

    # Creating, positioning and adding the cars that will be added over time to a group

    if difficulty == 'easy':

        added_cars_list = []

        added_car1 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        added_cars_list.append(added_car1)

    if difficulty == 'normal':

        added_cars_list = []

        added_car1 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        added_cars_list.append(added_car1)
        added_car2 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        added_cars_list.append(added_car2)

    elif difficulty == 'hard':

        added_cars_list_left = []
        added_cars_list_right = []

        added_car1 = TrafficCar(random.randint(1, 32), 'left', 'hard')
        added_cars_list_left.append(added_car1)
        added_car2 = TrafficCar(random.randint(1, 32), 'left', 'hard')
        added_cars_list_left.append(added_car2)

    # Creating, positioning and adding the power ups to a group

    power_ups_list = []
    power_ups = pygame.sprite.Group()

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
        if difficulty != 'hard':
            power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
            power_ups.add(power_up)
        elif difficulty == 'hard':
            x_position = random.choice([317, 496, 675, 853])
            if x_position == 317 or x_position == 496:
                power_up.set_position(x_position, random.randint(-1500, -100))
                power_ups.add(power_up)
            elif x_position == 675 or x_position == 853:
                power_up.set_position(x_position, random.randint(1500, 2750))
                power_ups.add(power_up)

    # Adding sprites to the all_sprites group

    all_sprites = pygame.sprite.Group()
    all_sprites.add(lolly)

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

    pygame.mixer.music.load("sounds/music/race_v2.mp3")  # loading the music after the countdown
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)  # -1 means that the music will loop

    while carryOn:

        clock.tick(60)

        if difficulty == 'easy':
            score += 3  # the score increases by 2 every frame
        elif difficulty == 'normal':
            score += 2 # the score increases by 1 every frame
        elif difficulty == 'hard':
            score += 1  # the score increases by 1 every frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            game_screen = pygame.Surface(size)  # creating a surface with the same size as the screen
            game_screen.blit(screen, (0, 0))  # copying the screen to the surface
            menu_open.play()  # playing the sound for when the menu opens
            pygame.time.delay(200)  # delaying the menu opening by 200 milliseconds, just so it looks smooth
            pygame.mixer.music.pause()  # pausing the music
            pause_menu(game_screen)  # calling the pause menu function
            pygame.mixer.music.unpause()  # unpausing the music

        # Player Car Movement

        if keys[pygame.K_w]:
            lolly.move_up()
        if keys[pygame.K_s]:
            lolly.move_down()
        if keys[pygame.K_a]:
            lolly.move_left()
        if keys[pygame.K_d]:
            lolly.move_right()

        # Power Up Movement
            
        for power_up in power_ups:
            if not power_up.on_cooldown:
                if difficulty == 'hard':
                    if power_up.rect.x == 317 or power_up.rect.x == 496:
                        power_up.move_down()
                    elif power_up.rect.x == 675 or power_up.rect.x == 853:
                        power_up.move_up()
                else:
                    power_up.move_down()

        # Updating the sprites so that they move on the screen after the player presses a key to move

        all_sprites.update()

        # Road Scroll and changes according to score

        # defining the road image

        if not frosty.active:
            if score < 2000:
                road = normal_road
            elif 2000 < score < 4000:
                road = normal_road2
            else:
                road = normal_road3
        else:
            if score < 2000:
                road = frozen_road
            elif score < 4000:
                road = frozen_road2
            else:
                road = frozen_road3

        # scrolling the road according to the active power ups

        if sissy.active:
            scroll_speed = 6000
        elif frosty.active:
            scroll_speed = 3000
        else:
            scroll_speed = 4000
        
        road_y += scroll_speed * clock.tick(60) / 1000  # we're multiplying the scroll speed by the clock tick to make the scrolling speed independent of the frame rate

        if road_y > 950:
            road_y = 0  # if the road goes off the screen, it is repositioned at the top of the screen

        screen.blit(road, (0, road_y))  # blitting the road twice so that there's no gap between the two images
        screen.blit(road, (0, road_y - 950))  # the second image is blitted at the top of the screen

        # Incoming Cars

        # adding cars over time (score)

        if difficulty == 'easy':
            # every 2000 points, a new car is added, until there are 5 cars
            if score > 2000 and score % 2000 == 0 and len(added_cars_list) != 0:
                added_car = added_cars_list.pop()  # the last car in the list is removed
                added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))  # the car is repositioned at the top of the screen
                for car in incoming_cars:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):  # if the car is too close to another car
                        added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                incoming_cars.add(added_car)  # added to the incoming cars group
                cars_list.append(added_car)  # and added to the cars list
                all_sprites.add(added_car)  # and added to the all sprites group
                
        elif difficulty == 'normal':
            # every 1000 points, a new car is added, until there are 6 cars
            if score > 1000 and score % 1000 == 0 and len(added_cars_list) != 0:
                added_car = added_cars_list.pop()
                added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                for car in incoming_cars:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):
                        added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                incoming_cars.add(added_car)
                cars_list.append(added_car)
                all_sprites.add(added_car)

        elif difficulty == 'hard':
            # every 1000 points, a new car is added, until there are 6 cars
            if score > 1000 and score % 1000 == 0 and len(added_cars_list_left) != 0:
                added_car = added_cars_list_left.pop()
                added_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                for car in incoming_cars_left:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):
                        added_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                incoming_cars_left.add(added_car)
                cars_list_left.append(added_car)
                all_sprites.add(added_car)
            if score > 1000 and score % 1000 == 0 and len(added_cars_list_right) != 0:
                added_car = added_cars_list_right.pop()
                added_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                for car in incoming_cars_right:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):
                        added_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                incoming_cars_right.add(added_car)
                cars_list_right.append(added_car)
                all_sprites.add(added_car)

        # if the cars go off the screen, they are repositioned and given a new image

        if difficulty != 'hard':
            for car in cars_list:
                car.move_down()  # the cars move down the screen at a random speed between 10 and 13
                if car.rect.y > 950:  # if the car goes off the screen
                    new_car_number = random.randint(1, 32)
                    car.change_car(new_car_number, 'left')  # the car is given a new image
                    car.add_speed(random.randint(-1, 3))  # the car is given a new speed buff or debuff
                    car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))  # the car is repositioned at the top of the screen
                    for car2 in cars_list:
                        if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                            car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))

        elif difficulty == 'hard':  # same thing as above, but for cars on the left and right
            for car in cars_list_left:
                car.move_down()
                if car.rect.y > 950:
                    new_car_number = random.randint(1, 32)
                    random_side = random.choice(['left', 'right'])
                    car.change_car(new_car_number, random_side)
                    car.add_speed(random.randint(-1, 3))
                    if random_side == 'left':
                        car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        for car2 in cars_list_left:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                    elif random_side == 'right':
                        car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        for car2 in cars_list_right:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
            for car in cars_list_right:
                car.move_up()
                if car.rect.y < -100:
                    new_car_number = random.randint(1, 32)
                    random_side = random.choice(['left', 'right'])
                    car.change_car(new_car_number, random_side)
                    car.add_speed(random.randint(-1, 3))
                    if random_side == 'left':
                        car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        for car2 in cars_list_left:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                    elif random_side == 'right':
                        car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        for car2 in cars_list_right:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([643, 825]), random.randint(1500, 2750))

        # Collision Detection

        # collision between players and traffic cars

        if difficulty != 'hard':

            for traffic_car in incoming_cars:
                if pygame.sprite.collide_rect(lolly, traffic_car):
                    if pygame.sprite.spritecollide(lolly, incoming_cars, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                        if lolly.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            lolly.add_health(-1)
                            if lolly.health == 0:
                                game_over(road, difficulty, lolly)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

        elif difficulty == 'hard':

            for traffic_car in incoming_cars_left:
                if pygame.sprite.collide_rect(lolly, traffic_car):
                    if pygame.sprite.spritecollide(lolly, incoming_cars_left, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        if lolly.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            lolly.add_health(-1)
                            if lolly.health == 0:
                                game_over(road, difficulty, lolly)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

            for traffic_car in incoming_cars_right:
                if pygame.sprite.collide_rect(lolly, traffic_car):
                    if pygame.sprite.spritecollide(lolly, incoming_cars_right, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        if lolly.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            lolly.add_health(-1)
                            if lolly.health == 0:
                                game_over(road, difficulty, lolly)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

        # collision between traffic cars

        if difficulty != 'hard':

            for traffic_car_1 in incoming_cars:
                for traffic_car_2 in incoming_cars:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):  # this time we're only checking for collision between the rectangles
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -800:  # if one of the cars is off screen
                                traffic_car_1.rect.y = random.randint(-2200, -800)  # then it is repositioned at the top of the screen
                                traffic_car_1.rect.x = random.choice([285, 466, 643, 825])  # and given a new image
                            elif traffic_car_1.rect.y < traffic_car_2.rect.y: #prevent the cars from overlapping
                                traffic_car_1.rect.y = traffic_car_2.rect.y - traffic_car_1.rect.height #then move the car 1 behind the car 2
                                traffic_car_1.speed = traffic_car_2.speed # and give it the same speed as the car 2
                            elif traffic_car_1.rect.y > traffic_car_2.rect.y: #check if the collision is happening when the traffic car 2 is behind
                                traffic_car_2.rect.y = traffic_car_1.rect.y - traffic_car_2.rect.height
                                traffic_car_2.speed = traffic_car_1.speed

        elif difficulty == 'hard':  # same thing as above, but for cars on the left and right

            for traffic_car_1 in incoming_cars_left:
                for traffic_car_2 in incoming_cars_left:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -800:
                                traffic_car_1.rect.y = random.randint(-2200, -800)
                                traffic_car_1.rect.x = random.choice([285, 466])
                            elif traffic_car_1.rect.y < traffic_car_2.rect.y: #prevent the cars from overlapping
                                traffic_car_1.rect.y = traffic_car_2.rect.y - traffic_car_1.rect.height #then move the car 1 behind the car 2
                                traffic_car_1.speed = traffic_car_2.speed # and give it the same speed as the car 2
                            elif traffic_car_1.rect.y > traffic_car_2.rect.y: #check if the collision is happening when the traffic car 2 is behind
                                traffic_car_2.rect.y = traffic_car_1.rect.y - traffic_car_2.rect.height
                                traffic_car_2.speed = traffic_car_1.speed

            for traffic_car_1 in incoming_cars_right:
                for traffic_car_2 in incoming_cars_right:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if traffic_car_1.rect.y < 2050 or traffic_car_2.rect.y < 2050:
                                traffic_car_1.rect.y = random.randint(1500, 2750)
                                traffic_car_1.rect.x = random.choice([643, 825])
                            elif traffic_car_1.rect.y < traffic_car_2.rect.y: #prevent the cars from overlapping
                                traffic_car_1.rect.y = traffic_car_2.rect.y - traffic_car_1.rect.height #then move the car 1 behind the car 2
                                traffic_car_1.speed = traffic_car_2.speed # and give it the same speed as the car 2
                            elif traffic_car_1.rect.y > traffic_car_2.rect.y: #check if the collision is happening when the traffic car 2 is behind
                                traffic_car_2.rect.y = traffic_car_1.rect.y - traffic_car_2.rect.height
                                traffic_car_2.speed = traffic_car_1.speed

        # collision between traffic cars and power ups
                                
        if difficulty != 'hard':
            
            for traffic_car in incoming_cars:
                for power_up in power_ups:
                    if pygame.sprite.collide_rect(traffic_car, power_up):
                        if pygame.sprite.spritecollide(traffic_car, power_ups, False, pygame.sprite.collide_mask):
                            # if they are not on screen, we reposition them at random
                            if traffic_car.rect.y < -800 or power_up.rect.y < -800:
                                traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                                power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
                            elif traffic_car.rect.y < power_up.rect.y:  # if the traffic car is behind the power up
                                traffic_car.rect.y = power_up.rect.y - traffic_car.rect.height
                                traffic_car.speed = power_up.speed
                            elif traffic_car.rect.y > power_up.rect.y:
                                power_up.rect.y = traffic_car.rect.y - power_up.rect.height
                                power_up.speed = traffic_car.speed

        elif difficulty == 'hard':

            for traffic_car in incoming_cars_left:
                for power_up in power_ups:
                    if pygame.sprite.collide_rect(traffic_car, power_up):
                        if pygame.sprite.spritecollide(traffic_car, power_ups, False, pygame.sprite.collide_mask):
                            if traffic_car.rect.y < -800 or power_up.rect.y < -800:
                                traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                                power_up.set_position(random.choice([317, 496]), random.randint(-1500, -100))
                            elif traffic_car.rect.y < power_up.rect.y:  # if the traffic car is behind the power up
                                traffic_car.rect.y = power_up.rect.y - traffic_car.rect.height
                                traffic_car.speed = power_up.speed
                            elif traffic_car.rect.y > power_up.rect.y:
                                power_up.rect.y = traffic_car.rect.y - power_up.rect.height
                                power_up.speed = traffic_car.speed

            for traffic_car in incoming_cars_right:
                for power_up in power_ups:
                    if pygame.sprite.collide_rect(traffic_car, power_up):
                        if pygame.sprite.spritecollide(traffic_car, power_ups, False, pygame.sprite.collide_mask):
                            if 1500 < traffic_car.rect.y < 2050 or 1500 < power_up.rect.y < 2050:
                                traffic_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                                power_up.set_position(random.choice([675, 853]), random.randint(1500, 2750))
                            elif traffic_car.rect.y < power_up.rect.y:  # if the traffic car is behind the power up
                                power_up.rect.y = traffic_car.rect.y - power_up.rect.height
                                power_up.speed = traffic_car.speed 
                            elif traffic_car.rect.y > power_up.rect.y:
                                traffic_car.rect.y = power_up.rect.y - traffic_car.rect.height
                                traffic_car.speed = power_up.speed

        # collision between players and power ups

        for power_up in power_ups:
            if pygame.sprite.collide_rect(lolly, power_up):
                if pygame.sprite.spritecollide(lolly, power_ups, False, pygame.sprite.collide_mask):
                    powerup_sound.play()
                    if power_up == sissy:
                        power_up.collision(lolly)
                    elif power_up == diva or power_up == growth:
                        power_up.collision('lolly', lolly)
                    elif power_up == frosty or power_up == toy:
                        if difficulty != 'hard':
                            power_up.collision(lolly, traffic_group=incoming_cars)
                        elif difficulty == 'hard':
                            power_up.collision(lolly, traffic_group_left=incoming_cars_left, traffic_group_right=incoming_cars_right) 
            
            # if the power up goes off the screen, it is repositioned at the top of the screen
            if difficulty != 'hard':
                if power_up.rect.y > 950:
                    power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
            else:
                if power_up.rect.y > 2750 or power_up.rect.y < -1500:
                    x_position = random.choice([317, 496, 675, 853])
                    if x_position == 317 or x_position == 496:
                        power_up.set_position(x_position, random.randint(-1500, -100))
                    elif x_position == 675 or x_position == 853:
                        power_up.set_position(x_position, random.randint(1500, 2750))

            if power_up.active:  # if the power up is active, then the duration timer decreases by 1 every frame
                power_up.duration -= 1
                if power_up.duration == 0: # if the duration reaches 0, then the power up is deactivated
                    if power_up == sissy:
                        power_up.deactivate(lolly)
                    elif power_up == diva or power_up == growth:
                        power_up.deactivate('lolly', lolly)
                    elif power_up == frosty or power_up == toy:
                        if difficulty != 'hard':
                            power_up.deactivate(incoming_cars)
                        elif difficulty == 'hard':
                            power_up.deactivate(traffic_group_left=incoming_cars_left, traffic_group_right=incoming_cars_right)
                    power_up.add_cooldown_prob() # give the power up a cooldown probability (the probability of the power up being available again)

            # now we're checking if the power up is available or not, and if it's not, then we're decreasing the cooldown timer by 1 every frame
            # if the cooldown reaches 0, then the power up is available again
            if power_up.on_cooldown:
                power_up.cooldown -= 1
                if power_up.cooldown == 0:
                    power_up.on_cooldown = False
                    power_up.add_cooldown(60)
                    if difficulty != 'hard':
                        power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
                    else:
                        x_position = random.choice([317, 496, 675, 853])
                        if x_position == 317 or x_position == 496:
                            power_up.set_position(x_position, random.randint(-1500, -100))
                        elif x_position == 675 or x_position == 853:
                            power_up.set_position(x_position, random.randint(1500, 2750))
                    power_up.can_move = True
                                    
        # Drawing the Sprites

        lolly.change_image(active_power_ups('lolly', diva, growth))

        all_sprites.update()  # updating the sprites again, so that the images are changed
        all_sprites.draw(screen)  # drawing the sprites on the screen

        # Drawing the Power Ups that change the road and screen

        if frosty.active:
            screen.blit(snow_sky, (0, 0))
            screen.blit(snow_snowflakes, (0, 0))

        if sissy.active:
            screen.blit(random.choice(speed_images), (0, 0))

        # Drawing the Score Bar

        score_bar_font = pygame.font.SysFont('comic_sans', 55)  # yes Liah, we're using comic sans
        border_colour = (55, 18, 26)

        score_text = score_bar_font.render(f"{score}", True, (255, 255, 255))
        offsets = [
            (-3, -3), (-2, -3), (-1, -3), (0, -3), (1, -3), (2, -3), (3, -3),
            (-3, -2), (3, -2), (-3, -1), (3, -1), (-3, 0), (3, 0), (-3, 1), (3, 1),
            (-3, 2), (3, 2), (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3)
        ]  # this is a list of tuples, each tuple is a coordinate offset for the score text

        screen.blit(score_bar, (0, 0))

        for offset in offsets:  # this for loop draws the score text with the offsets, so that it looks like it has a border
            screen.blit(score_bar_font.render(f"{score}", True, border_colour), (170 + offset[0], offset[1]))

        screen.blit(score_text, (170, 0))

        # Drawing the Hearts (Lives)

        for HP in range(lolly.max_health):
            if HP < lolly.health:
                screen.blit(lolly.heart_on, (870 + HP * 75, 5))
            else:
                screen.blit(lolly.heart_off, (870 + HP * 75, 5))

        # Drawing the Power Ups Bar (on the left side of the screen)

        icon_position = 30  # the y position of the first icon
        for icon in power_ups_bar(diva.active, growth.active, sissy.active, frosty.active, toy.active):
            icon_position += 80
            screen.blit(icon, (0, icon_position))

        # Inserting the Victory Part

        if difficulty == 'easy':
            if score >= 6000 and score % 3000 == 0:  # if the score reaches 6000 or every 3000 points after that
                pygame.mixer.music.set_volume(0.05)  # the music volume is decreased
                # get the current game screen to pause
                game_screen = pygame.Surface(size)  # creating a surface with the same size as the screen
                game_screen.blit(screen, (0, 0))  # copying the screen to the surface
                victory(game_screen, difficulty, lolly.car_type)  # the victory function is called
                pygame.mixer.music.set_volume(0.4)  # the music volume is increased again

        elif difficulty == 'normal':
            if score >= 6000 and score % 2000 == 0:  # if the score reaches 6000 or every 2000 points after that
                pygame.mixer.music.set_volume(0.05)
                game_screen = pygame.Surface(size)
                game_screen.blit(screen, (0, 0))
                victory(game_screen, difficulty, lolly.car_type)
                pygame.mixer.music.set_volume(0.4)

        elif difficulty == 'hard':
            if score >= 6000 and score % 1000 == 0:  # if the score reaches 6000 or every 1000 points after that
                pygame.mixer.music.set_volume(0.05)
                game_screen = pygame.Surface(size)
                game_screen.blit(screen, (0, 0))
                victory(game_screen, difficulty, lolly.car_type)
                pygame.mixer.music.set_volume(0.4)

        # Updating the Display

        pygame.display.flip()

    pygame.quit()

def multi_game(difficulty, lolly_car, bestie_car):

    """
    Function to start and run the multiplayer game.

    Parameters
    ----------
    difficulty : str
        The difficulty level of the game ('easy', 'normal', 'hard').
    lolly_car : str
        The image file name of the player car for Lolly.
    bestie_car : str
        The image file name of the player car for Bestie.
    """

    pygame.mixer.init() # for sound
    pygame.init() # for pygame
    pygame.font.init() # for text

    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")  # sound for when the menu opens
    menu_open.set_volume(0.7)
    hp_loss = pygame.mixer.Sound("sounds/hp_loss.mpeg")
    hp_die = pygame.mixer.Sound("sounds/hp_die.mpeg")
    hp_diva = pygame.mixer.Sound("sounds/hp_diva.mp3")
    powerup_sound = pygame.mixer.Sound("sounds/powerup_sound.mpeg")
    galpal_sound = pygame.mixer.Sound("sounds/galpal.mp3")
    error = pygame.mixer.Sound("sounds/error.mp3")
    error.set_volume(0.5)

    # Setting up the screen

    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

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

    lolly.set_position(285, (950 - lolly.rect.height))  # the x position is different for each player car, set_position is a function from the Car class
    bestie.set_position(466, (950 - bestie.rect.height))

    sprite_lolly = pygame.sprite.Group()
    sprite_bestie = pygame.sprite.Group()
    players_cars = pygame.sprite.Group()
    sprite_lolly.add(lolly)
    players_cars.add(lolly)
    sprite_bestie.add(bestie)
    players_cars.add(bestie)

    # Creating, positioning and adding the traffic cars to a group

    if difficulty == 'easy':

        cars_list = []
        incoming_cars = pygame.sprite.Group()

        left_car1 = TrafficCar(random.randint(1, 32), 'left', 'easy')  # TrafficCar(car_number (we have 32 images), direction of the car (left is for cars going downwards), difficulty)
        cars_list.append(left_car1)
        left_car2 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        cars_list.append(left_car2)
        left_car3 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        cars_list.append(left_car3)
        left_car4 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        cars_list.append(left_car4)

        for car in cars_list:
            car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
            incoming_cars.add(car)

    if difficulty == 'normal':

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

    # Creating, positioning and adding the cars that will be added over time to a group

    if difficulty == 'easy':

        added_cars_list = []

        added_car1 = TrafficCar(random.randint(1, 32), 'left', 'easy')
        added_cars_list.append(added_car1)

    if difficulty == 'normal':

        added_cars_list = []

        added_car1 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        added_cars_list.append(added_car1)
        added_car2 = TrafficCar(random.randint(1, 32), 'left', 'normal')
        added_cars_list.append(added_car2)

    elif difficulty == 'hard':

        added_cars_list_left = []
        added_cars_list_right = []

        added_car1 = TrafficCar(random.randint(1, 32), 'left', 'hard')
        added_cars_list_left.append(added_car1)
        added_car2 = TrafficCar(random.randint(1, 32), 'left', 'hard')
        added_cars_list_left.append(added_car2)

    # Creating, positioning and adding the power ups to a group

    power_ups_list = []
    power_ups = pygame.sprite.Group()

    besties = BestiesInHarmony(difficulty)  # each Power Up is a class, children of the PowerUp class
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
        if difficulty != 'hard':
            power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
            power_ups.add(power_up)
        elif difficulty == 'hard':
            x_position = random.choice([317, 496, 675, 853])
            if x_position == 317 or x_position == 496:
                power_up.set_position(x_position, random.randint(-1500, -100))
                power_ups.add(power_up)
            elif x_position == 675 or x_position == 853:
                power_up.set_position(x_position, random.randint(1500, 2750))
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

    pygame.mixer.music.load("sounds/music/race_v2.mp3")  # loading the music after the countdown
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)  # -1 means that the music will loop

    while carryOn:

        clock.tick(60)

        if difficulty == 'easy':
            score += 3  # the score increases by 2 every frame
        elif difficulty == 'normal':
            score += 2 # the score increases by 1 every frame
        elif difficulty == 'hard':
            score += 1  # the score increases by 1 every frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            game_screen = pygame.Surface(size)  # creating a surface with the same size as the screen
            game_screen.blit(screen, (0, 0))  # copying the screen to the surface
            menu_open.play()  # playing the sound for when the menu opens
            pygame.time.delay(200)  # delaying the menu opening by 200 milliseconds, just so it looks smooth
            pygame.mixer.music.pause()  # pausing the music
            pause_menu(game_screen)  # calling the pause menu function
            pygame.mixer.music.unpause()  # unpausing the music

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

        # Power Up Movement
            
        for power_up in power_ups:
            if not power_up.on_cooldown:
                if difficulty == 'hard':
                    if power_up.rect.x == 317 or power_up.rect.x == 496:
                        power_up.move_down()
                    elif power_up.rect.x == 675 or power_up.rect.x == 853:
                        power_up.move_up()
                else:
                    power_up.move_down()

        # Updating the sprites so that they move on the screen after the player presses a key to move

        all_sprites.update()

        # Road Scroll and changes according to score

        # defining the road image

        if not frosty.active:
            if score < 2000:
                road = normal_road
            elif 2000 < score < 4000:
                road = normal_road2
            else:
                road = normal_road3
        else:
            if score < 2000:
                road = frozen_road
            elif score < 4000:
                road = frozen_road2
            else:
                road = frozen_road3

        # scrolling the road according to the active power ups

        if sissy.active:
            scroll_speed = 6000
        elif frosty.active:
            scroll_speed = 3000
        else:
            scroll_speed = 4000
        
        road_y += scroll_speed * clock.tick(60) / 1000  # we're multiplying the scroll speed by the clock tick to make the scrolling speed independent of the frame rate

        if road_y > 950:
            road_y = 0  # if the road goes off the screen, it is repositioned at the top of the screen

        screen.blit(road, (0, road_y))  # blitting the road twice so that there's no gap between the two images
        screen.blit(road, (0, road_y - 950))  # the second image is blitted at the top of the screen

        # Incoming Cars

        # adding cars over time (score)

        if difficulty == 'easy':
            # every 2000 points, a new car is added, until there are 5 cars
            if score > 2000 and score % 2000 == 0 and len(added_cars_list) != 0:
                added_car = added_cars_list.pop()  # the last car in the list is removed
                added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))  # the car is repositioned at the top of the screen
                for car in incoming_cars:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):  # if the car is too close to another car
                        added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                incoming_cars.add(added_car)  # added to the incoming cars group
                cars_list.append(added_car)  # and added to the cars list
                all_sprites.add(added_car)  # and added to the all sprites group
                
        elif difficulty == 'normal':
            # every 1000 points, a new car is added, until there are 6 cars
            if score > 1000 and score % 1000 == 0 and len(added_cars_list) != 0:
                added_car = added_cars_list.pop()
                added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                for car in incoming_cars:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):
                        added_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                incoming_cars.add(added_car)
                cars_list.append(added_car)
                all_sprites.add(added_car)

        elif difficulty == 'hard':
            # every 1000 points, a new car is added, until there are 6 cars
            if score > 1000 and score % 1000 == 0 and len(added_cars_list_left) != 0:
                added_car = added_cars_list_left.pop()
                added_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                for car in incoming_cars_left:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):
                        added_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                incoming_cars_left.add(added_car)
                cars_list_left.append(added_car)
                all_sprites.add(added_car)
            if score > 1000 and score % 1000 == 0 and len(added_cars_list_right) != 0:
                added_car = added_cars_list_right.pop()
                added_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                for car in incoming_cars_right:
                    if added_car.rect.x == car.rect.x and ((car.rect.y - added_car.rect.y) < 400 or (car.rect.y - added_car.rect.y) > -400):
                        added_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                incoming_cars_right.add(added_car)
                cars_list_right.append(added_car)
                all_sprites.add(added_car)

        # if the cars go off the screen, they are repositioned and given a new image

        if difficulty != 'hard':
            for car in cars_list:
                car.move_down()  # the cars move down the screen at a random speed between 10 and 13
                if car.rect.y > 950:  # if the car goes off the screen
                    new_car_number = random.randint(1, 32)
                    car.change_car(new_car_number, 'left')  # the car is given a new image
                    car.add_speed(random.randint(-1, 3))  # the car is given a new speed buff or debuff
                    car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))  # the car is repositioned at the top of the screen
                    for car2 in cars_list:
                        if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                            car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))

        elif difficulty == 'hard':  # same thing as above, but for cars on the left and right
            for car in cars_list_left:
                car.move_down()
                if car.rect.y > 950:
                    new_car_number = random.randint(1, 32)
                    random_side = random.choice(['left', 'right'])
                    car.change_car(new_car_number, random_side)
                    car.add_speed(random.randint(-1, 3))
                    if random_side == 'left':
                        car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        for car2 in cars_list_left:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                    elif random_side == 'right':
                        car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        for car2 in cars_list_right:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
            for car in cars_list_right:
                car.move_up()
                if car.rect.y < -100:
                    new_car_number = random.randint(1, 32)
                    random_side = random.choice(['left', 'right'])
                    car.change_car(new_car_number, random_side)
                    car.add_speed(random.randint(-1, 3))
                    if random_side == 'left':
                        car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        for car2 in cars_list_left:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                    elif random_side == 'right':
                        car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        for car2 in cars_list_right:
                            if car.rect.x == car2.rect.x and ((car2.rect.y - car.rect.y) < 400 or (car2.rect.y - car.rect.y) > -400):
                                car.set_position(random.choice([643, 825]), random.randint(1500, 2750))

        # Collision Detection

        # collision between players

        if lolly.can_collide and bestie.can_collide:
            # if there's a collision betwen the rectangles, then check for collision between the masks
            if pygame.sprite.collide_rect(lolly, bestie):
                # spritecollide(sprite, group, boolean (True if the sprite should be killed), collision method)
                if pygame.sprite.spritecollide(lolly, sprite_bestie, False, pygame.sprite.collide_mask):

                    if lolly.rect.x < bestie.rect.x:  # if the Lolly is on the left side
                        if not (bestie.rect.x >= (980 - bestie.rect.width) or lolly.rect.x <= 272):  # if the players are not in the corner
                            lolly.rect.x -= lolly.speed # pull the Lolly more to the left side
                            bestie.rect.x += bestie.speed  # and the Bestie more to the right
                        elif bestie.rect.x >= (980 - bestie.rect.width):  # if the bestie is in the right corner
                            lolly.rect.x -= lolly.speed  # the lolly won't be able to move to the right
                        elif lolly.rect.x <= 272:  # if the lolly is in the left corner
                            bestie.rect.x += bestie.speed  # the bestie can't move to the left
                    else:  # the inverse if the Lolly is on the right side
                        if not (lolly.rect.x >= (980 - lolly.rect.width) or bestie.rect.x <= 272):
                            lolly.rect.x += lolly.speed
                            bestie.rect.x -= bestie.speed
                        elif lolly.rect.x >= (980 - lolly.rect.width):
                            bestie.rect.x -= bestie.speed
                        elif bestie.rect.x <= 272:
                            lolly.rect.x += lolly.speed

                    if lolly.rect.y < bestie.rect.y:  # if the Lolly is on the top side
                        if not (bestie.rect.y >= (950 - bestie.rect.height) or lolly.rect.y <= 0):
                            lolly.rect.y -= lolly.speed
                            bestie.rect.y += bestie.speed
                        elif bestie.rect.y >= (950 - bestie.rect.height):
                            lolly.rect.y -= lolly.speed
                        elif lolly.rect.y <= 0:
                            bestie.rect.y += bestie.speed
                    else:  # the inverse if the Lolly is on the bottom side
                        if not (lolly.rect.y >= (950 - lolly.rect.height) or bestie.rect.y <= 0):
                            lolly.rect.y += lolly.speed
                            bestie.rect.y -= bestie.speed
                        elif lolly.rect.y >= (950 - lolly.rect.height):
                            bestie.rect.y -= bestie.speed
                        elif bestie.rect.y <= 0:
                            lolly.rect.y += lolly.speed

        # collision between players and traffic cars

        if difficulty != 'hard':

            for traffic_car in incoming_cars:
                if pygame.sprite.collide_rect(lolly, traffic_car):
                    if pygame.sprite.spritecollide(lolly, incoming_cars, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                        if lolly.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            lolly.add_health(-1)
                            if lolly.health == 0 and bestie.health != 0:
                                hp_die.play()
                                lolly.die()  # if the Lolly is eliminated, then the die function is called,
                                # this function moves the car off screen and turns the can_move variable to False
                                # also, it stores the position of the car, so that it can be respawned later
                            elif lolly.health <= 0 and bestie.health <= 0:  # if both players are eliminated, then the game is over
                                game_over(road, difficulty, lolly, bestie)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

        elif difficulty == 'hard':

            for traffic_car in incoming_cars_left:
                if pygame.sprite.collide_rect(lolly, traffic_car):
                    if pygame.sprite.spritecollide(lolly, incoming_cars_left, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        if lolly.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            lolly.add_health(-1)
                            if lolly.health == 0 and bestie.health != 0:
                                hp_die.play()
                                lolly.die()
                            elif lolly.health <= 0 and bestie.health <= 0:
                                game_over(road, difficulty, lolly, bestie)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

            for traffic_car in incoming_cars_right:
                if pygame.sprite.collide_rect(lolly, traffic_car):
                    if pygame.sprite.spritecollide(lolly, incoming_cars_right, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        if lolly.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            lolly.add_health(-1)
                            if lolly.health == 0 and bestie.health != 0:
                                hp_die.play()
                                lolly.die()
                            elif lolly.health <= 0 and bestie.health <= 0:
                                game_over(road, difficulty, lolly, bestie)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

        if difficulty != 'hard':

            for traffic_car in incoming_cars:
                if pygame.sprite.collide_rect(bestie, traffic_car):
                    if pygame.sprite.spritecollide(bestie, incoming_cars, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                        if bestie.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            bestie.add_health(-1)
                            if bestie.health == 0 and lolly.health != 0:
                                hp_die.play()
                                bestie.die()
                            elif bestie.health <= 0 and lolly.health <= 0:
                                game_over(road, difficulty, lolly, bestie)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

        elif difficulty == 'hard':

            for traffic_car in incoming_cars_left:
                if pygame.sprite.collide_rect(bestie, traffic_car):
                    if pygame.sprite.spritecollide(bestie, incoming_cars_left, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                        if bestie.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            bestie.add_health(-1)
                            if bestie.health == 0 and lolly.health != 0:
                                hp_die.play()
                                bestie.die()
                            elif bestie.health <= 0 and lolly.health <= 0:
                                game_over(road, difficulty, lolly, bestie)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

            for traffic_car in incoming_cars_right:
                if pygame.sprite.collide_rect(bestie, traffic_car):
                    if pygame.sprite.spritecollide(bestie, incoming_cars_right, False, pygame.sprite.collide_mask):
                        traffic_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                        if bestie.can_crash:  # if diva defiance is active, the player is invincible, so can_crash is False
                            bestie.add_health(-1)	
                            if bestie.health == 0 and lolly.health != 0:
                                hp_die.play()
                                bestie.die()
                            elif bestie.health <= 0 and lolly.health <= 0:
                                game_over(road, difficulty, lolly, bestie)
                            else:
                                hp_loss.play()
                        else:
                            hp_diva.play()
                            pass

        # collision between traffic cars

        if difficulty != 'hard':

            for traffic_car_1 in incoming_cars:
                for traffic_car_2 in incoming_cars:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):  # this time we're only checking for collision between the rectangles
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -800:  # if one of the cars is off screen
                                traffic_car_1.rect.y = random.randint(-2200, -800)  # then it is repositioned at the top of the screen
                                traffic_car_1.rect.x = random.choice([285, 466, 643, 825])  # and given a new image
                            elif traffic_car_1.rect.y < traffic_car_2.rect.y: #prevent the cars from overlapping
                                traffic_car_1.rect.y = traffic_car_2.rect.y - traffic_car_1.rect.height #then move the car 1 behind the car 2
                                traffic_car_1.speed = traffic_car_2.speed # and give it the same speed as the car 2
                            elif traffic_car_1.rect.y > traffic_car_2.rect.y: #check if the collision is happening when the traffic car 2 is behind
                                traffic_car_2.rect.y = traffic_car_1.rect.y - traffic_car_2.rect.height
                                traffic_car_2.speed = traffic_car_1.speed

        elif difficulty == 'hard':  # same thing as above, but for cars on the left and right

            for traffic_car_1 in incoming_cars_left:
                for traffic_car_2 in incoming_cars_left:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if traffic_car_1.rect.y < -800 or traffic_car_2.rect.y < -800:
                                traffic_car_1.rect.y = random.randint(-2200, -800)
                                traffic_car_1.rect.x = random.choice([285, 466])
                            elif traffic_car_1.rect.y < traffic_car_2.rect.y: #prevent the cars from overlapping
                                traffic_car_1.rect.y = traffic_car_2.rect.y - traffic_car_1.rect.height #then move the car 1 behind the car 2
                                traffic_car_1.speed = traffic_car_2.speed # and give it the same speed as the car 2
                            elif traffic_car_1.rect.y > traffic_car_2.rect.y: #check if the collision is happening when the traffic car 2 is behind
                                traffic_car_2.rect.y = traffic_car_1.rect.y - traffic_car_2.rect.height
                                traffic_car_2.speed = traffic_car_1.speed

            for traffic_car_1 in incoming_cars_right:
                for traffic_car_2 in incoming_cars_right:
                    if traffic_car_1 != traffic_car_2:
                        if pygame.sprite.collide_rect(traffic_car_1, traffic_car_2):
                            if 1500 < traffic_car_1.rect.y < 2050 or 1500 < traffic_car_2.rect.y < 2050:
                                traffic_car_1.rect.y = random.randint(1500, 2750)
                                traffic_car_1.rect.x = random.choice([643, 825])
                            elif traffic_car_1.rect.y < traffic_car_2.rect.y: #prevent the cars from overlapping
                                traffic_car_1.rect.y = traffic_car_2.rect.y - traffic_car_1.rect.height #then move the car 1 behind the car 2
                                traffic_car_1.speed = traffic_car_2.speed # and give it the same speed as the car 2
                            elif traffic_car_1.rect.y > traffic_car_2.rect.y: #check if the collision is happening when the traffic car 2 is behind
                                traffic_car_2.rect.y = traffic_car_1.rect.y - traffic_car_2.rect.height
                                traffic_car_2.speed = traffic_car_1.speed

        # collision between traffic cars and power ups
                                
        if difficulty != 'hard':
            
            for traffic_car in incoming_cars:
                for power_up in power_ups:
                    if pygame.sprite.collide_rect(traffic_car, power_up):
                        if pygame.sprite.spritecollide(traffic_car, power_ups, False, pygame.sprite.collide_mask):
                            # if they are not on screen, we reposition them at random
                            if traffic_car.rect.y < -800 or power_up.rect.y < -800:
                                traffic_car.set_position(random.choice([285, 466, 643, 825]), random.randint(-1500, -100))
                                power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
                            elif traffic_car.rect.y < power_up.rect.y:  # if the traffic car is behind the power up
                                traffic_car.rect.y = power_up.rect.y - traffic_car.rect.height
                                traffic_car.speed = power_up.speed
                            elif traffic_car.rect.y > power_up.rect.y:
                                power_up.rect.y = traffic_car.rect.y - power_up.rect.height
                                power_up.speed = traffic_car.speed

        elif difficulty == 'hard':

            for traffic_car in incoming_cars_left:
                for power_up in power_ups:
                    if pygame.sprite.collide_rect(traffic_car, power_up):
                        if pygame.sprite.spritecollide(traffic_car, power_ups, False, pygame.sprite.collide_mask):
                            if traffic_car.rect.y < -800 or power_up.rect.y < -800:
                                traffic_car.set_position(random.choice([285, 466]), random.randint(-1500, -100))
                                power_up.set_position(random.choice([317, 496]), random.randint(-1500, -100))
                            elif traffic_car.rect.y < power_up.rect.y:  # if the traffic car is behind the power up
                                traffic_car.rect.y = power_up.rect.y - traffic_car.rect.height
                                traffic_car.speed = power_up.speed
                            elif traffic_car.rect.y > power_up.rect.y:
                                power_up.rect.y = traffic_car.rect.y - power_up.rect.height
                                power_up.speed = traffic_car.speed

            for traffic_car in incoming_cars_right:
                for power_up in power_ups:
                    if pygame.sprite.collide_rect(traffic_car, power_up):
                        if pygame.sprite.spritecollide(traffic_car, power_ups, False, pygame.sprite.collide_mask):
                            if 1500 < traffic_car.rect.y < 2050 or 1500 < power_up.rect.y < 2050:
                                traffic_car.set_position(random.choice([643, 825]), random.randint(1500, 2750))
                                power_up.set_position(random.choice([675, 853]), random.randint(1500, 2750))
                            elif traffic_car.rect.y < power_up.rect.y:  # if the traffic car is behind the power up
                                power_up.rect.y = traffic_car.rect.y - power_up.rect.height
                                power_up.speed = traffic_car.speed 
                            elif traffic_car.rect.y > power_up.rect.y:
                                traffic_car.rect.y = power_up.rect.y - traffic_car.rect.height
                                traffic_car.speed = power_up.speed

        # collision between players and power ups

        for power_up in power_ups:
            if pygame.sprite.collide_rect(lolly, power_up) or pygame.sprite.collide_rect(bestie, power_up):
                if pygame.sprite.spritecollide(lolly, power_ups, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(bestie, power_ups, False, pygame.sprite.collide_mask):
                    if power_up == galpal:
                        powerup_sound.play()
                        galpal_sound.play()
                        power_up.collision(lolly=lolly, bestie=bestie)
                    elif power_up == tangled:
                        error.play()
                        power_up.collision(lolly=lolly, bestie=bestie)
                    elif power_up == besties or power_up == sissy:
                        powerup_sound.play()
                        power_up.collision(lolly=lolly, bestie=bestie)
                    elif power_up == diva or power_up == growth:
                        powerup_sound.play()
                        if pygame.sprite.spritecollide(lolly, power_ups, False, pygame.sprite.collide_mask):
                            power_up.collision('lolly', lolly)
                        elif pygame.sprite.spritecollide(bestie, power_ups, False, pygame.sprite.collide_mask):
                            power_up.collision('bestie', bestie)
                    elif power_up == frosty or power_up == toy:
                        powerup_sound.play()
                        if difficulty != 'hard':
                            power_up.collision(lolly, bestie, traffic_group=incoming_cars)
                        elif difficulty == 'hard':
                            power_up.collision(lolly, bestie, traffic_group_left=incoming_cars_left, traffic_group_right=incoming_cars_right) 
            
            # if the power up goes off the screen, it is repositioned at the top of the screen
            if difficulty != 'hard':
                if power_up.rect.y > 950:
                    power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
            else:
                if power_up.rect.y > 2750 or power_up.rect.y < -1500:
                    x_position = random.choice([317, 496, 675, 853])
                    if x_position == 317 or x_position == 496:
                        power_up.set_position(x_position, random.randint(-1500, -100))
                    elif x_position == 675 or x_position == 853:
                        power_up.set_position(x_position, random.randint(1500, 2750))

            if power_up.active:  # if the power up is active, then the duration timer decreases by 1 every frame
                power_up.duration -= 1
                if power_up.duration == 0: # if the duration reaches 0, then the power up is deactivated
                    if power_up == besties or power_up == galpal or power_up == tangled or power_up == sissy:
                        power_up.deactivate(lolly= lolly, bestie = bestie)
                    elif power_up == diva or power_up == growth:
                        power_up.deactivate('lolly', lolly)
                        power_up.deactivate('bestie', bestie)
                    elif power_up == frosty or power_up == toy:
                        if difficulty != 'hard':
                            power_up.deactivate(incoming_cars)
                        elif difficulty == 'hard':
                            power_up.deactivate(traffic_group_left=incoming_cars_left, traffic_group_right=incoming_cars_right)
                    power_up.add_cooldown_prob() # give the power up a cooldown probability

            # if the power up is not active (on cooldown), then the cooldown timer decreases by 1 every frame
            # if the cooldown reaches 0, then the power up is available again
            if power_up.on_cooldown:
                power_up.cooldown -= 1
                if power_up.cooldown == 0:
                    power_up.on_cooldown = False
                    power_up.add_cooldown(60)
                    if difficulty != 'hard':
                        power_up.set_position(random.choice([317, 496, 675, 853]), random.randint(-1500, -100))
                    else:
                        x_position = random.choice([317, 496, 675, 853])
                        if x_position == 317 or x_position == 496:
                            power_up.set_position(x_position, random.randint(-1500, -100))
                        elif x_position == 675 or x_position == 853:
                            power_up.set_position(x_position, random.randint(1500, 2750))
                    power_up.can_move = True
                    # the power up is repositioned and can move again
                                    
        if lolly.eliminated or bestie.eliminated:
            galpal.can_move = True
            tangled.can_move = False
            tangled.hide()
            besties.can_move = False
            besties.hide()
        else:
            # if one of the players is eliminated, then the gal pal rebirth power up is available
            galpal.can_move = False
            galpal.hide()
            tangled.can_move = True
            besties.can_move = True

        # Drawing the Sprites

        lolly.change_image(active_power_ups('lolly', diva=diva, growth=growth, tangled=tangled, besties=besties))  # changing the image of the player cars according to the active power ups
        bestie.change_image(active_power_ups('bestie', diva=diva, growth=growth, tangled=tangled, besties=besties))

        all_sprites.update()  # updating the sprites again, so that the images are changed
        all_sprites.draw(screen)  # drawing the sprites on the screen

        # Drawing the Power Ups that change the road and screen

        if frosty.active:
            screen.blit(snow_sky, (0, 0))
            screen.blit(snow_snowflakes, (0, 0))

        if sissy.active:
            screen.blit(random.choice(speed_images), (0, 0))

        # Drawing the Score Bar

        score_bar_font = pygame.font.SysFont('comic_sans', 55)  # yes Liah, we're using comic sans
        border_colour = (55, 18, 26)

        score_text = score_bar_font.render(f"{score}", True, (255, 255, 255))
        offsets = [
            (-3, -3), (-2, -3), (-1, -3), (0, -3), (1, -3), (2, -3), (3, -3),
            (-3, -2), (3, -2), (-3, -1), (3, -1), (-3, 0), (3, 0), (-3, 1), (3, 1),
            (-3, 2), (3, 2), (-3, 3), (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3), (3, 3)
        ]  # this is a list of tuples, each tuple is a coordinate offset for the score text

        screen.blit(score_bar, (0, 0))

        for offset in offsets:  # this for loop draws the score text with the offsets, so that it looks like it has a border
            screen.blit(score_bar_font.render(f"{score}", True, border_colour), (170 + offset[0], offset[1]))

        screen.blit(score_text, (170, 0))

        # Drawing the Hearts (Lives)

        for HP in range(lolly.max_health):
            if HP < lolly.health:  # if the HP is less than the health, then the heart is drawn
                screen.blit(lolly.heart_on, (480 + HP * 75, 5))  # the hearts are drawn at different x positions, so that they're not on top of each other
            else:  # if the HP is greater or equal to the health, then the heart loss image is drawn, which is just a heart with less opacity
                screen.blit(lolly.heart_off, (480 + HP * 75, 5))
        
        for HP in range(bestie.max_health):
            if HP < bestie.health:
                screen.blit(bestie.heart_on, (870 + HP * 75, 5))
            else:
                screen.blit(bestie.heart_off, (870 + HP * 75, 5))

        # Drawing the Power Ups Bar (on the left side of the screen)

        icon_position = 30  # the y position of the first icon
        for icon in power_ups_bar(diva.active, growth.active, sissy.active, frosty.active, toy.active, tangled.active, besties.active):
            icon_position += 80
            screen.blit(icon, (0, icon_position))

        # Inserting the Victory Part

        if difficulty == 'easy':
            if score >= 6000 and score % 3000 == 0:  # if the score reaches 6000 or every 3000 points after that
                pygame.mixer.music.set_volume(0.05)  # the music volume is decreased
                # get the current game screen to pause
                game_screen = pygame.Surface(size)  # creating a surface with the same size as the screen
                game_screen.blit(screen, (0, 0))  # copying the screen to the surface
                victory(game_screen, difficulty, lolly.car_type, bestie.car_type)  # the victory function is called
                pygame.mixer.music.set_volume(0.4)  # the music volume is increased again

        elif difficulty == 'normal':
            if score >= 6000 and score % 2000 == 0:  # if the score reaches 6000 or every 2000 points after that
                pygame.mixer.music.set_volume(0.05)
                game_screen = pygame.Surface(size)
                game_screen.blit(screen, (0, 0))
                victory(game_screen, difficulty, lolly.car_type, bestie.car_type)
                pygame.mixer.music.set_volume(0.4)

        elif difficulty == 'hard':
            if score >= 6000 and score % 1000 == 0:  # if the score reaches 6000 or every 1000 points after that
                pygame.mixer.music.set_volume(0.05)
                game_screen = pygame.Surface(size)
                game_screen.blit(screen, (0, 0))
                victory(game_screen, difficulty, lolly.car_type, bestie.car_type)
                pygame.mixer.music.set_volume(0.4)

        # Updating the Display

        pygame.display.flip()

    pygame.quit()

def countdown(game_screen):

    """
    Display a countdown animation before the game starts.

    Parameters
    ----------
    game_screen : pygame.Surface
        The game screen surface.
    """

    # Initialising the game and setting the screen, done in the same way as the game function
    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    # Loading the countdown sounds
    beeps = pygame.mixer.Sound("sounds/countdown/beeps.mp3")
    go = pygame.mixer.Sound("sounds/countdown/go.mp3")
    beeps.set_volume(0.5)
    go.set_volume(0.5)

    # Loading the countdown images
    countdown_3 = pygame.image.load("images/countdown/countdown_3.png").convert_alpha()
    countdown_2 = pygame.image.load("images/countdown/countdown_2.png").convert_alpha()
    countdown_1 = pygame.image.load("images/countdown/countdown_1.png").convert_alpha()
    countdown_go = pygame.image.load("images/countdown/countdown_go.png").convert_alpha()

    screen.blit(game_screen, (0, 0))  # blitting the game screen
    screen.blit(countdown_3, (0, 0))  # blitting the countdown image on top of the game screen
    beeps.play()  # playing the beeps sound
    pygame.display.flip()

    pygame.time.wait(1000)  # waiting 1 second before blitting the next image
    screen.blit(game_screen, (0, 0))
    screen.blit(countdown_2, (0, 0))  # blitting the next image
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

    pygame.time.wait(1500)  # waiting 1.5 seconds before the game starts
    return  # returning to the game function

def game_over(road, difficulty, lolly, bestie = None):
    
    """
    Display the game over screen and handle user input for restarting or exiting the game.

    Parameters
    ----------
    road : pygame.Surface
        The image of the road background.
    difficulty : str
        The difficulty level of the game.
    lolly Car : object
        The player's car object.
    bestie Car : object, optional
        The second player's car object in multiplayer mode. Defaults to None.
    """

    # Initialising the game and setting the screen, done in the same way as the game function
    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    # Loading Sounds
    pygame.mixer.music.stop()
    gameover_music = pygame.mixer.Sound("sounds/music/gameover.mp3")
    exit_pressed = pygame.mixer.Sound("sounds/exit_button.mp3")
    exit_pressed.set_volume(0.2)
    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)

    # Loading Images
    game_over_image = pygame.image.load("images/game_over/game_over.png").convert_alpha()
    game_over_restart_image = pygame.image.load("images/game_over/game_over_restart.png").convert_alpha()
    game_over_exit_image = pygame.image.load("images/game_over/game_over_exit.png").convert_alpha()

    center_game_over_coord = ((1250 - 792) // 2, (950 - 792) // 2)  # the center coordinates of the game over image
    pygame.display.flip()

    restart_button_coor = 445, 295, 820, 400  # x1, x2, y1, y2
    exit_button_coor = 495, 420, 750, 520

    clock = pygame.time.Clock()
    road_y = 0

    carry_on = True
    event = pygame.event.Event(pygame.USEREVENT)

    gameover_music.play(-1)

    while carry_on:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False

        # Same scrolling background as in the game function, same logic as well
        screen.blit(road, (0, 0))
        scroll_speed = 3000
        dt = clock.tick(60) / 1000.0
        road_y += scroll_speed * dt

        if road_y >= 950:
            road_y = 0

        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y - 950))

        mouse = pygame.mouse.get_pos()

        if restart_button_coor[0] <= mouse[0] <= restart_button_coor[2] and restart_button_coor[1] < mouse[1] < restart_button_coor[3]:  # if the user hovers over the restart button
            screen.blit(game_over_restart_image, center_game_over_coord)  # the restart image is blitted
            if event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the restart button
                gameover_music.stop()
                button_pressed.play()
                if bestie == None:
                    single_game(difficulty, lolly.car_type)  # calling the single_game function with the same difficulty and car types as before
                else:
                    multi_game(difficulty, lolly.car_type, bestie.car_type)  # calling the multi_game function with the same difficulty and car types as before

        elif exit_button_coor[0] <= mouse[0] <= exit_button_coor[2] and exit_button_coor[1] < mouse[1] < exit_button_coor[3]:
            screen.blit(game_over_exit_image, center_game_over_coord)
            if event.type == pygame.MOUSEBUTTONDOWN:
                exit_pressed.play()
                pygame.time.delay(800)
                carry_on = False
        
        else:
            screen.blit(game_over_image, center_game_over_coord)  # if the user hovers over anywhere else, then the normal game over image is blitted

        pygame.display.flip()

    pygame.quit()

def pause_menu(game_screen):

    """
    Display a pause menu on the game screen.

    Parameters
    ----------
    game_screen : pygame.Surface
        The game screen surface.
    """

    menu_position = [451, 799, 326, 624]  # x1, x2, y1, y2
    buttons = (
        ['done', 544, 709, 376, 447],
        ['exit', 528, 723, 501, 572]
        )  # name, x1, x2, y1, y2
    
    # Initialising the game and setting the screen, done in the same way as the game function
    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    # Loading the sounds
    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    exit_pressed = pygame.mixer.Sound("sounds/exit_button.mp3")
    exit_pressed.set_volume(0.2)

    # Loading the images
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
                    button_pressed.play()
                    paused = False

            elif buttons[1][1] <= mouse[0] <= buttons[1][2] and buttons[1][3] < mouse[1] < buttons[1][4]:  # if the user hovers over the exit button
                screen.blit(pause_menu_exit_image, (menu_position[0], menu_position[2]))
                if event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the exit button
                    exit_pressed.play()
                    pygame.time.delay(800)
                    pygame.quit()

            elif not (menu_position[0] <= mouse[0] <= menu_position[1] and menu_position[2] < mouse[1] < menu_position[3]):  # if the user hovers over anywhere else
                screen.blit(pause_menu_image, (menu_position[0], menu_position[2]))
                if event.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks anywhere else
                    button_pressed.play()
                    paused = False
                    
        pygame.display.flip()

def active_power_ups(player, diva, growth, tangled=None, besties=None):

    """
    Determine the active combination of power-ups based on the player and power-up states.

    Parameters
    ----------
    player : str
        The player's name 'lolly' or 'bestie'.
    diva : object
        The Diva power-up object.
    growth : object
        The Glamorous Growth power-up object.
    tangled : object, optional
        The Tangled Twist power-up object. Defaults to None.
    besties : object, optional
        The Besties in Harmony power-up object. Defaults to None.

    Returns
    -------
    active_combination : str
        The active combination of power-ups.
    """

    active_combination = 'normal'

    if tangled is None and besties is None:  # if it's the single player game
        if diva.active_lolly and not growth.active_lolly:  # if the Diva Defiance power-up is active
            active_combination = 'diva'
        elif growth.active_lolly and not diva.active_lolly:  # if the Glamorous Growth power-up is active
            active_combination = 'growth'
        elif diva.active_lolly and growth.active_lolly:  # if the Diva Defiance and Glamorous Growth power-ups are active
            active_combination = 'diva_growth'
    else:  # if it's the multiplayer game
        if player == 'lolly':
            if besties.active and not diva.active_lolly and not growth.active_lolly and not tangled.active:  # if the Besties in Harmony power-up is active
                active_combination = 'besties'
            if besties.active and not diva.active_lolly and not growth.active_lolly and tangled.active:  # if the Besties in Harmony and Tangled Twist power-ups are active
                active_combination = 'besties_tangled'
            if besties.active and not diva.active_lolly and growth.active_lolly and not tangled.active:  # if the Besties in Harmony and Glamorous Growth power-ups are active
                active_combination = 'besties_growth'
            if besties.active and not diva.active_lolly and growth.active_lolly and tangled.active:  # if the Besties in Harmony, Glamorous Growth, and Tangled Twist power-ups are active
                active_combination = 'besties_tangled_growth'
            if besties.active and diva.active_lolly and not growth.active_lolly and not tangled.active:  # if the Besties in Harmony and Diva Defiance power-ups are active
                active_combination = 'besties_diva'
            if besties.active and diva.active_lolly and not growth.active_lolly and tangled.active:  # if the Besties in Harmony, Diva Defiance, and Tangled Twist power-ups are active
                active_combination = 'besties_diva_tangled'
            if besties.active and diva.active_lolly and growth.active_lolly and not tangled.active:  # if the Besties in Harmony, Diva Defiance, and Glamorous Growth power-ups are active
                active_combination = 'besties_diva_growth'
            if besties.active and diva.active_lolly and growth.active_lolly and tangled.active:  # if the Besties in Harmony, Diva Defiance, Glamorous Growth, and Tangled Twist power-ups are active
                active_combination = 'besties_diva_tangled_growth'
            if not besties.active and not diva.active_lolly and growth.active_lolly and not tangled.active:  # if the Glamorous Growth power-up is active
                active_combination = 'growth'
            if not besties.active and not diva.active_lolly and not growth.active_lolly and tangled.active:  # if the Tangled Twist power-up is active
                active_combination = 'tangled'
            if not besties.active and not diva.active_lolly and growth.active_lolly and tangled.active:  # if the Glamorous Growth and Tangled Twist power-ups are active
                active_combination = 'tangled_growth'
            if not besties.active and diva.active_lolly and not growth.active_lolly and not tangled.active:  # if the Diva Defiance power-up is active
                active_combination = 'diva'
            if not besties.active and diva.active_lolly and not growth.active_lolly and tangled.active:  # if the Diva Defiance and Tangled Twist power-ups are active
                active_combination = 'diva_tangled'
            if not besties.active and diva.active_lolly and growth.active_lolly and not tangled.active:  # if the Diva Defiance and Glamorous Growth power-ups are active
                active_combination = 'diva_growth'
            if not besties.active and diva.active_lolly and growth.active_lolly and tangled.active:  # if the Diva Defiance, Glamorous Growth, and Tangled Twist power-ups are active
                active_combination = 'diva_tangled_growth'
        elif player == 'bestie':  # same thing as above, but for the bestie
            if besties.active and not diva.active_bestie and not growth.active_bestie and not tangled.active:
                active_combination = 'besties'
            if besties.active and not diva.active_bestie and not growth.active_bestie and tangled.active:
                active_combination = 'besties_tangled'
            if besties.active and not diva.active_bestie and growth.active_bestie and not tangled.active:
                active_combination = 'besties_growth'
            if besties.active and not diva.active_bestie and growth.active_bestie and tangled.active:
                active_combination = 'besties_tangled_growth'
            if besties.active and diva.active_bestie and not growth.active_bestie and not tangled.active:
                active_combination = 'besties_diva'
            if besties.active and diva.active_bestie and not growth.active_bestie and tangled.active:
                active_combination = 'besties_diva_tangled'
            if besties.active and diva.active_bestie and growth.active_bestie and not tangled.active:
                active_combination = 'besties_diva_growth'
            if besties.active and diva.active_bestie and growth.active_bestie and tangled.active:
                active_combination = 'besties_diva_tangled_growth'
            if not besties.active and not diva.active_bestie and growth.active_bestie and not tangled.active:
                active_combination = 'growth'
            if not besties.active and not diva.active_bestie and not growth.active_bestie and tangled.active:
                active_combination = 'tangled'
            if not besties.active and not diva.active_bestie and growth.active_bestie and tangled.active:
                active_combination = 'tangled_growth'
            if not besties.active and diva.active_bestie and not growth.active_bestie and not tangled.active:
                active_combination = 'diva'
            if not besties.active and diva.active_bestie and not growth.active_bestie and tangled.active:
                active_combination = 'diva_tangled'
            if not besties.active and diva.active_bestie and growth.active_bestie and not tangled.active:
                active_combination = 'diva_growth'
            if not besties.active and diva.active_bestie and growth.active_bestie and tangled.active:
                active_combination = 'diva_tangled_growth'

    return active_combination

def power_ups_bar(diva, growth, sissy, frosty, toy, tangled=None, besties=None):

    """
    Generate a list of power-up images based on the given boolean values.

    Parameters
    ----------
    diva : bool
        Whether the "diva_defiance" power-up is active.
    growth : bool
        Whether the "glamorous_growth" power-up is active.
    sissy : bool
        Whether the "sissy_that_walk" power-up is active.
    frosty : bool
        Whether the "frosty_frenzy" power-up is active.
    toy : bool
        Whether the "toy_transforminator" power-up is active.
    tangled : bool, optional
        Whether the "tangled_twist" power-up is active. Defaults to None.
    besties : bool, optional
        Whether the "besties_in_harmony" power-up is active. Defaults to None.

    Returns
    -------
    list
        A list of power-up images.
    """

    power_ups = []
    if tangled == None and besties == None:  # if it's the single player game
        power_ups_names = ["diva_defiance", "glamorous_growth", "sissy_that_walk", "frosty_frenzy", "toy_transforminator"]
        power_ups_boolean_list = [diva, growth, sissy, frosty, toy]
    else:  # if it's the multiplayer game
        power_ups_names = ["diva_defiance", "glamorous_growth", "sissy_that_walk", "frosty_frenzy", "toy_transforminator", "tangled_twist", "besties_in_harmony"]
        power_ups_boolean_list = [diva, growth, sissy, frosty, toy, tangled, besties]

    for number in range(len(power_ups_boolean_list)):  # this for loop adds the power ups to the list, according to the boolean values
        if power_ups_boolean_list[number]:  # if the power up is active
            power_ups.append(pygame.image.load(f"images/power_ups/{power_ups_names[number]}.png").convert_alpha())
        else:  # if the power up is inactive
            power_ups.append(pygame.image.load(f"images/power_ups/{power_ups_names[number]}_off.png").convert_alpha())
    
    return power_ups  # returning the list of power ups

def victory(game_screen, difficulty, lolly, bestie = None):

    victory = False

    if difficulty == 'easy':
        dog = 1
    elif difficulty == 'normal':
        dog = 2
    elif difficulty == 'hard':
        dog = 3

    # Initialising the game and setting the screen, done in the same way as the game function
    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    # Loading the sounds
    phone_ring = pygame.mixer.Sound("sounds/victory/phone_ring.mp3")
    phone_ring.set_volume(0.5)
    phone_pickup = pygame.mixer.Sound("sounds/victory/phone_pickup.mp3")
    phone_pickup.set_volume(0.7)
    talking = pygame.mixer.Sound("sounds/victory/talking.mp3")
    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    exit_pressed = pygame.mixer.Sound("sounds/exit_button.mp3")
    exit_pressed.set_volume(0.2)
    win_sound = pygame.mixer.Sound("sounds/victory/win_sound.mp3")
    win_music = pygame.mixer.Sound("sounds/music/win.mp3")
    win_music.set_volume(0.6)

    # Loading the images
    victory_question = pygame.image.load("images/victory/victory_question.png").convert_alpha()
    waiting_1 = pygame.image.load("images/victory/waiting_1.png").convert_alpha()
    waiting_2 = pygame.image.load("images/victory/waiting_2.png").convert_alpha()
    waiting_3 = pygame.image.load("images/victory/waiting_3.png").convert_alpha()
    victory_story_1 = pygame.image.load("images/victory/victory_story_1.png").convert_alpha()
    victory_story_2 = pygame.image.load("images/victory/victory_story_2.png").convert_alpha()

    if bestie != None:  # if it's the multiplayer game
        victory_image = pygame.image.load(f"images/victory/victory_end_{dog}{lolly[-1]}{bestie[-1]}.png").convert()
        victory_restart_image = pygame.image.load(f"images/victory/victory_end_restart_{dog}{lolly[-1]}{bestie[-1]}.png").convert()
        victory_exit_image = pygame.image.load(f"images/victory/victory_end_exit_{dog}{lolly[-1]}{bestie[-1]}.png").convert()
    else:  # if it's the single player game
        victory_image = pygame.image.load(f"images/victory/victory_end_{dog}{lolly[-1]}.png").convert()
        victory_restart_image = pygame.image.load(f"images/victory/victory_end_restart_{dog}{lolly[-1]}.png").convert()
        victory_exit_image = pygame.image.load(f"images/victory/victory_end_exit_{dog}{lolly[-1]}.png").convert()

    # Loading the images for the buttons (restart and exit)
    restart_coord = 1026, 1168, 325, 376
    exit_coord = 1088, 1168, 238, 289

    screen.blit(game_screen, (0, 0))
    screen.blit(victory_question, (0, 0))
    pygame.display.flip()

    carry_on = True
    carry_on_2 = False

    phone_ring.play(-1)  # playing the phone ring sound on a loop

    while carry_on:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            mouse = pygame.mouse.get_pos()

            # first, we're displaying the question image, if the user presses Y, we're displaying the story image for 20 seconds, if the user presses N, we're unpausing the game

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_y:

                    phone_ring.stop()  # stopping the phone ring sound
                    button_pressed.play()
                    carry_on_2 = True
                    victory = True
                    pygame.mixer.music.stop()  # stopping the music
                    phone_pickup.play()  # playing the phone pickup sound
                    pygame.time.delay(1000)

                    # displaying three dots while the person is talking
                    screen.blit(game_screen, (0, 0))
                    screen.blit(waiting_1, (0, 0))
                    pygame.display.flip()
                    talking.play()
                    pygame.time.delay(500)
                    screen.blit(waiting_2, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(500)
                    screen.blit(waiting_3, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(4500)

                    #displaying the story
                    win_sound.play()
                    screen.blit(victory_story_1, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(4000)
                    screen.blit(victory_story_2, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(4000)

                    carry_on = False

                elif event.key == pygame.K_n:
                    phone_ring.stop()
                    carry_on = False

        pygame.display.flip()

    if victory:

        screen.blit(victory_image, (0, 0))
        pygame.display.flip()

        win_music.play(-1)  # playing the victory music on a loop

        while carry_on_2:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                mouse = pygame.mouse.get_pos()
            
                # if the user hovers and clicks over the buttons
                if restart_coord[0] <= mouse[0] <= restart_coord[1] and restart_coord[2] < mouse[1] < restart_coord[3]:
                    screen.blit(victory_restart_image, (0, 0))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button_pressed.play()
                        carry_on_2 = False
                        win_music.stop()
                        if bestie == None:
                            single_game(difficulty, lolly)
                        else:
                            multi_game(difficulty, lolly, bestie)

                elif exit_coord[0] <= mouse[0] <= exit_coord[1] and exit_coord[2] < mouse[1] < exit_coord[3]:
                    screen.blit(victory_exit_image, (0, 0))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        exit_pressed.play()
                        pygame.time.delay(800)
                        pygame.quit()
                else:
                    screen.blit(victory_image, (0, 0))

            pygame.display.flip()