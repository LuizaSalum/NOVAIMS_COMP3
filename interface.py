import pygame
from game import *


# buttons is a dictionary with the screen name as key and the buttons lists as values
# each button is in the format (name, min_x, max_x, mix_y, max_y) and the list has several of these tuples

buttons = {
    'start': [
        ('singleplayer', 955, 1163, 460, 505),
        ('multiplayer', 965, 1163, 568, 618),
        ('credits', 1040, 1163, 678, 727),
        ('exit', 1090, 1163, 787, 838)
        ],
    'singleplayer': [
        ('back', 80, 203, 860, 910),
        ('start', 238, 465, 860, 910),
        ('lolly', 250, 531, 250, 425),
        ('dog', 667, 948, 250, 425),
        ('power_ups', 250, 531, 515, 700),
        ('reset', 568, 630, 442, 509)
        ],
    'multiplayer': [
        ('back', 80, 203, 860, 910),
        ('start', 238, 465, 860, 910),
        ('lolly', 250, 531, 250, 425),
        ('dog', 667, 948, 250, 425),
        ('power_ups', 250, 531, 515, 700),
        ('bestie', 667, 948, 515, 700),
        ('reset', 568, 630, 442, 509)
        ],
    'select_dog': [
        ('easy', 154, 365, 364, 450),
        ('normal', 492, 702, 364, 450),
        ('hard', 836, 1046, 364, 450),
        ('choose', 273, 927, 168, 274),
        ('info', 113, 169, 156, 213),
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
        ],
    'select_character': [
        ('car1', 170, 363, 357, 763),
        ('car2', 501, 707, 357, 763),
        ('car3', 833, 1028, 357, 763),
        ('choose', 273, 927, 168, 274),
        ('info', 113, 169, 156, 213),
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
        ],
    'power_ups_list': [
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
        ],
    'menu': [
        ('done', 543, 708, 251, 320),
        ('credits', 500, 750, 375, 445),
        ('back', 508, 738, 503, 575),
        ('exit', 528, 722, 626, 696)
        ]
    }


def start_screen(music_started=True):

    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    if not music_started:
        pygame.mixer.music.load("sounds/music/start_screen_v2.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        music_started = True

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    exit_pressed = pygame.mixer.Sound("sounds/exit_button.mp3")
    exit_pressed.set_volume(0.2)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    start_image = pygame.image.load("images/interface/start.png").convert_alpha()
    screen.blit(start_image, (0, 0))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=start_image)

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['start'])):
                if buttons['start'][number][1] <= mouse[0] <= buttons['start'][number][2] and buttons['start'][number][3] <= mouse[1] <= buttons['start'][number][4]:  # if the mouse is in the button range of width and height
                    button = buttons['start'][number][0]
                    break
            else:
                button = None

            if button == None:
                start_image = pygame.image.load("images/interface/start.png").convert_alpha()
            else:
                start_image = pygame.image.load(f"images/interface/start_{button}.png").convert_alpha()

            screen.blit(start_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons 

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['start'])):
                    if buttons['start'][number][1] <= user_input.pos[0] <= buttons['start'][number][2] and buttons['start'][number][3] <= user_input.pos[1] <= buttons['start'][number][4]:
                        if buttons['start'][number][0] == 'singleplayer':
                            button_pressed.play()
                            single_customisation_screen(lolly='car1', difficulty='normal')
                        elif buttons['start'][number][0] == 'multiplayer':
                            button_pressed.play()
                            multi_customisation_screen(lolly='car1', bestie='car2', difficulty='normal')
                        elif buttons['start'][number][0] == 'credits':
                            button_pressed.play()
                            credits_screen()
                        elif buttons['start'][number][0] == 'exit':
                            pygame.mixer.music.fadeout(800)
                            exit_pressed.play()
                            pygame.time.delay(800)
                            pygame.quit()
                            exit()


def credits_screen():

    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    credits_image = pygame.image.load("images/interface/credits.png").convert_alpha()
    screen.blit(credits_image, (0, 0))
    pygame.display.flip()

    back_button_position = (1055, 1183, 370, 420)  # (min_x, max_x,mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=credits_image)

            # if the user hovers over the back button

            mouse = pygame.mouse.get_pos()

            if back_button_position[0] <= mouse[0] <= back_button_position[1] and back_button_position[2] <= mouse[1] <= back_button_position[3]:
                credits_image = pygame.image.load("images/interface/credits_back.png").convert_alpha()
                screen.blit(credits_image, (0, 0))
                pygame.display.flip()

            else:
                credits_image = pygame.image.load("images/interface/credits.png").convert_alpha()
                screen.blit(credits_image, (0, 0))
                pygame.display.flip()

            # if the user clicks on the back button
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                if back_button_position[0] <= user_input.pos[0] <= back_button_position[1] and back_button_position[2] <= user_input.pos[1] <= back_button_position[3]:
                    button_pressed.play()
                    start_screen()


def single_customisation_screen(lolly, difficulty):

    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    single_customisation_image = pygame.image.load("images/interface/singleplayer.png").convert_alpha()
    screen.blit(single_customisation_image, (0, 0))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=single_customisation_image)

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['singleplayer'])):
                if buttons['singleplayer'][number][1] <= mouse[0] <= buttons['singleplayer'][number][2] and buttons['singleplayer'][number][3] <= mouse[1] <= buttons['singleplayer'][number][4]:
                    button = buttons['singleplayer'][number][0]
                    break
            else:
                button = None

            if button == None:
                single_customisation_image = pygame.image.load("images/interface/singleplayer.png").convert_alpha()
            else:
                single_customisation_image = pygame.image.load(f"images/interface/singleplayer_{button}.png").convert_alpha()

            screen.blit(single_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['singleplayer'])):
                    if buttons['singleplayer'][number][1] <= user_input.pos[0] <= buttons['singleplayer'][number][2] and buttons['singleplayer'][number][3] <= user_input.pos[1] <= buttons['singleplayer'][number][4]:
                        if buttons['singleplayer'][number][0] == 'back':
                            button_pressed.play()
                            start_screen()
                        elif buttons['singleplayer'][number][0] == 'start':
                            # pygame.mixer.music.stop()
                            pass  # single_game(lolly_car=lolly, difficulty=difficulty)
                        elif buttons['singleplayer'][number][0] == 'lolly':
                            button_pressed.play()
                            lolly_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty)
                        elif buttons['singleplayer'][number][0] == 'dog':
                            button_pressed.play()
                            dog_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty)
                        elif buttons['singleplayer'][number][0] == 'power_ups':
                            button_pressed.play()
                            power_ups_list_screen(mode='single', lolly=lolly, difficulty=difficulty)
                        elif buttons['singleplayer'][number][0] == 'reset':
                            button_pressed.play()
                            lolly = 'car1'
                            difficulty = 'normal'


def multi_customisation_screen(lolly, bestie, difficulty):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    multi_customisation_image = pygame.image.load("images/interface/multiplayer.png").convert_alpha()
    screen.blit(multi_customisation_image, (0, 0))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=multi_customisation_image)

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['multiplayer'])):
                if buttons['multiplayer'][number][1] <= mouse[0] <= buttons['multiplayer'][number][2] and buttons['multiplayer'][number][3] <= mouse[1] <= buttons['multiplayer'][number][4]:
                    button = buttons['multiplayer'][number][0]
                    break
            else:
                button = None

            if button == None:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer.png").convert_alpha()
            else:
                multi_customisation_image = pygame.image.load(f"images/interface/multiplayer_{button}.png").convert_alpha()

            screen.blit(multi_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['multiplayer'])):
                    if buttons['multiplayer'][number][1] <= user_input.pos[0] <= buttons['multiplayer'][number][2] and buttons['multiplayer'][number][3] <= user_input.pos[1] <= buttons['multiplayer'][number][4]:
                        if buttons['multiplayer'][number][0] == 'back':
                            button_pressed.play()
                            start_screen()
                        elif buttons['multiplayer'][number][0] == 'start':
                            button_pressed.play()
                            pygame.mixer.music.stop()
                            multi_game(lolly_car=lolly, bestie_car=bestie, difficulty=difficulty)
                        elif buttons['multiplayer'][number][0] == 'lolly':
                            button_pressed.play()
                            lolly_customisation_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty)
                        elif buttons['multiplayer'][number][0] == 'dog':
                            button_pressed.play()
                            dog_customisation_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty)
                        elif buttons['multiplayer'][number][0] == 'power_ups':
                            button_pressed.play()
                            power_ups_list_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty)
                        elif buttons['multiplayer'][number][0] == 'bestie':
                            button_pressed.play()
                            bestie_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty)
                        elif buttons['multiplayer'][number][0] == 'reset':
                            button_pressed.play()
                            lolly = 'car1'
                            bestie = 'car2'
                            difficulty = 'normal'


def dog_customisation_screen(lolly, mode, difficulty, bestie=None):

    selected_difficulty = difficulty  # storing the difficulty selected before the customisation screen is opened

    pygame.mixer.init()
    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    easy_bark = pygame.mixer.Sound("sounds/dogs/easy.mp3")
    normal_bark = pygame.mixer.Sound("sounds/dogs/normal.mp3")
    hard_bark = pygame.mixer.Sound("sounds/dogs/hard.mp3")

    dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
    screen.blit(dog_customisation_image, (0, 0))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=dog_customisation_image)

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range((len(buttons['select_dog']) - 4) , len(buttons['select_dog'])):
                if buttons['select_dog'][number][1] <= mouse[0] <= buttons['select_dog'][number][2] and buttons['select_dog'][number][3] <= mouse[1] <= buttons['select_dog'][number][4]:
                    button = buttons['select_dog'][number][0]
                    break
            else:
                button = None

            if button == None:
                dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
            else:
                dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}_{button}.png").convert_alpha()

            screen.blit(dog_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['select_dog'])):

                    if buttons['select_dog'][number][1] <= user_input.pos[0] <= buttons['select_dog'][number][2] and buttons['select_dog'][number][3] <= user_input.pos[1] <= buttons['select_dog'][number][4]:

                        if buttons['select_dog'][number][0] == 'easy':
                            difficulty = 'easy'
                            button_pressed.play()
                            pygame.time.delay(200)
                            easy_bark.play()
                            # display the easy dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()

                        elif buttons['select_dog'][number][0] == 'normal':
                            difficulty = 'normal'
                            button_pressed.play()
                            pygame.time.delay(200)
                            normal_bark.play()
                            # display the normal dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()

                        elif buttons['select_dog'][number][0] == 'hard':
                            difficulty = 'hard'
                            button_pressed.play()
                            pygame.time.delay(200)
                            hard_bark.play()
                            # display the hard dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()

                        elif buttons['select_dog'][number][0] == 'choose':
                            button_pressed.play()
                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty)

                        elif buttons['select_dog'][number][0] == 'back':
                            button_pressed.play()
                            start_screen()
                            return
                        
                        elif buttons['select_dog'][number][0] == 'return':
                                
                                if mode == 'single':
                                    button_pressed.play()
                                    single_customisation_screen(lolly=lolly, difficulty=selected_difficulty)
                                else:
                                    button_pressed.play()
                                    multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=selected_difficulty)


def lolly_customisation_screen(mode, lolly, difficulty, bestie=None):

    selected_lolly = lolly  # storing the lolly selected before the customisation screen is opened

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)
    error = pygame.mixer.Sound("sounds/error.mp3")
    error.set_volume(0.5)

    lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
    screen.blit(lolly_customisation_image, (0, 0))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=lolly_customisation_image)

            # if the user hovers over the buttons

            button = None

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['select_character']) - 4, len(buttons['select_character'])):  
                if buttons['select_character'][number][1] <= mouse[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= mouse[1] <= buttons['select_character'][number][4]:
                    button = buttons['select_character'][number][0]
                    break
            else:
                button = None

            if button == None:
                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
            else:
                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_{button}.png").convert_alpha()

            screen.blit(lolly_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['select_character'])):

                    if buttons['select_character'][number][1] <= user_input.pos[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= user_input.pos[1] <= buttons['select_character'][number][4]:

                        if buttons['select_character'][number][0] == 'car1':
                            if bestie != 'car1':
                                lolly = 'car1'
                                button_pressed.play()
                                # display the car1
                                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
                            else:
                                error.play()

                        elif buttons['select_character'][number][0] == 'car2':
                            if bestie != 'car2':
                                lolly = 'car2'
                                button_pressed.play()
                                # display the car2
                                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
                            else:
                                error.play()

                        elif buttons['select_character'][number][0] == 'car3':
                            if bestie != 'car3':
                                lolly = 'car3'
                                button_pressed.play()
                                # display the car3
                                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
                            else:
                                error.play()

                        elif buttons['select_character'][number][0] == 'choose':
                            button_pressed.play()
                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty)

                        elif buttons['select_character'][number][0] == 'back':
                            button_pressed.play()
                            start_screen()
                            return
                        
                        elif buttons['select_character'][number][0] == 'return':  # reset the lolly to the previously selected one

                            if mode == 'single':
                                button_pressed.play()
                                single_customisation_screen(lolly=selected_lolly, difficulty=difficulty)
                            else:
                                button_pressed.play()
                                multi_customisation_screen(lolly=selected_lolly, bestie=bestie, difficulty=difficulty)



def bestie_customisation_screen(lolly, bestie, difficulty):

    selected_bestie = bestie  # storing the bestie selected before the customisation screen is opened

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)
    error = pygame.mixer.Sound("sounds/error.mp3")
    error.set_volume(0.5)

    bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
    screen.blit(bestie_customisation_image, (0, 0))
    pygame.display.flip()

    while True:
        
        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=bestie_customisation_image)

            # if the user hovers over the buttons

            button = None

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['select_character']) - 4, len(buttons['select_character'])):
                if buttons['select_character'][number][1] <= mouse[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= mouse[1] <= buttons['select_character'][number][4]:
                    button = buttons['select_character'][number][0]
                    break
            else:
                button = None

            if button == None:
                bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
            else:
                bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}_{button}.png").convert_alpha()

            screen.blit(bestie_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['select_character'])):

                    if buttons['select_character'][number][1] <= user_input.pos[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= user_input.pos[1] <= buttons['select_character'][number][4]:

                        if buttons['select_character'][number][0] == 'car1':
                            if lolly != 'car1':
                                bestie = 'car1'
                                button_pressed.play()
                                # display the car1
                                bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                            else:
                                error.play()

                        elif buttons['select_character'][number][0] == 'car2':
                            if lolly != 'car2':
                                bestie = 'car2'
                                button_pressed.play()
                                # display the car2
                                bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                            else:
                                error.play()

                        elif buttons['select_character'][number][0] == 'car3':
                            if lolly != 'car3':
                                bestie = 'car3'
                                button_pressed.play()
                                # display the car3
                                bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                            else:
                                error.play()

                        elif buttons['select_character'][number][0] == 'choose':
                            button_pressed.play()
                            multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty)

                        elif buttons['select_character'][number][0] == 'back':
                            button_pressed.play()
                            start_screen()
                            return
                        
                        elif buttons['select_character'][number][0] == 'return':  # reset the bestie to the previously selected one
                            button_pressed.play()
                            multi_customisation_screen(lolly=lolly, bestie=selected_bestie, difficulty=difficulty)


def power_ups_list_screen(mode, lolly, difficulty, bestie=None):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    if mode == 'single':
        power_ups_list_image = pygame.image.load("images/interface/singleplayer_power_ups_list.png").convert_alpha()
    else:
        power_ups_list_image = pygame.image.load("images/interface/multiplayer_power_ups_list.png").convert_alpha()
    screen.blit(power_ups_list_image, (0, 0))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    menu(screen_image=power_ups_list_image)

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['power_ups_list'])):
                if buttons['power_ups_list'][number][1] <= mouse[0] <= buttons['power_ups_list'][number][2] and buttons['power_ups_list'][number][3] <= mouse[1] <= buttons['power_ups_list'][number][4]:
                    button = buttons['power_ups_list'][number][0]
                    break
            else:
                button = None

            if mode == 'single':
                if button == None:
                    power_ups_list_image = pygame.image.load("images/interface/singleplayer_power_ups_list.png").convert_alpha()
                else:
                    power_ups_list_image = pygame.image.load(f"images/interface/singleplayer_power_ups_list_{button}.png").convert_alpha()

            else:
                if button == None:
                    power_ups_list_image = pygame.image.load("images/interface/multiplayer_power_ups_list.png").convert_alpha()
                else:
                    power_ups_list_image = pygame.image.load(f"images/interface/multiplayer_power_ups_list_{button}.png").convert_alpha()

            screen.blit(power_ups_list_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['power_ups_list'])):

                    if buttons['power_ups_list'][number][1] <= user_input.pos[0] <= buttons['power_ups_list'][number][2] and buttons['power_ups_list'][number][3] <= user_input.pos[1] <= buttons['power_ups_list'][number][4]:

                        button_pressed.play()

                        if buttons['power_ups_list'][number][0] == 'back':
                            start_screen()
                            return
                        
                        elif buttons['power_ups_list'][number][0] == 'return':
                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty)


def menu(screen_image):

    menu_position = (451, 799, 201, 749)  # (min_x, max_x, mix_y, max_y)

    button_pressed = pygame.mixer.Sound("sounds/button_pressed.mp3")
    button_pressed.set_volume(0.5)
    exit_pressed = pygame.mixer.Sound("sounds/exit_button.mp3")
    exit_pressed.set_volume(0.2)
    menu_open = pygame.mixer.Sound("sounds/menu_open.mp3")
    menu_open.set_volume(0.7)

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")

    # display the background image (screen_image) and the menu on top of it, in the menu position

    screen.blit(screen_image, (0, 0))
    menu_image = pygame.image.load("images/interface/menu.png").convert_alpha()
    screen.blit(menu_image, (menu_position[0], menu_position[2]))
    pygame.display.flip()

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
                    menu_open.play()
                    pygame.time.delay(200)
                    return

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['menu'])):
                if buttons['menu'][number][1] <= mouse[0] <= buttons['menu'][number][2] and buttons['menu'][number][3] <= mouse[1] <= buttons['menu'][number][4]:
                    button = buttons['menu'][number][0]
                    break
            else:
                button = None

            if button == None:
                menu_image = pygame.image.load("images/interface/menu.png").convert_alpha()
            else:
                menu_image = pygame.image.load(f"images/interface/menu_{button}.png").convert_alpha()

            screen.blit(screen_image, (0, 0))
            screen.blit(menu_image, (menu_position[0], menu_position[2]))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                for number in range(len(buttons['menu'])):

                    if buttons['menu'][number][1] <= user_input.pos[0] <= buttons['menu'][number][2] and buttons['menu'][number][3] <= user_input.pos[1] <= buttons['menu'][number][4]:

                        if buttons['menu'][number][0] == 'done':  # if the user clicks on the done button, we'll close the menu and return to the previous screen
                            button_pressed.play()
                            return

                        elif buttons['menu'][number][0] == 'credits':
                            button_pressed.play()
                            credits_screen()

                        elif buttons['menu'][number][0] == 'back':
                            button_pressed.play()
                            start_screen()
                            return

                        elif buttons['menu'][number][0] == 'exit':
                            pygame.mixer.music.fadeout(800)
                            exit_pressed.play()
                            pygame.time.delay(800)
                            pygame.quit()
                            exit()

                if not (menu_position[0] <= mouse[0] <= menu_position[1] and menu_position[2] <= mouse[1] <= menu_position[3]):  # if the user clicks on the screen but not on the menu, we'll close the menu and return to the previous screen
                    return