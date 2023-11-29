import pygame
from game import multi_game


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
        ('info', 113, 169, 156, 213),
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
        ],
    'select_character': [
        ('left', 200, 250, 446, 563),
        ('right', 945, 995, 446, 563),
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

def start_screen():

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    start_image = pygame.image.load("images/interface/start.png").convert_alpha()
    screen.blit(start_image, (0, 0))
    pygame.display.flip()

    single_power_ups = ['diva_defiance', 'frosty_frenzy', 'tangled_twist', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']
    multi_power_ups = ['besties_in_harmony', 'diva_defiance', 'frosty_frenzy', 'gal_pal_rebirth', 'tangled_twist', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            if user_input.type == pygame.KEYDOWN:
                if user_input.key == pygame.K_ESCAPE:
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
                            single_customisation_screen(lolly='car1', difficulty='normal', power_ups=single_power_ups)
                        elif buttons['start'][number][0] == 'multiplayer':
                            multi_customisation_screen(lolly='car1', bestie='car2', difficulty='normal', power_ups=multi_power_ups)
                        elif buttons['start'][number][0] == 'credits':
                            credits_screen()
                        elif buttons['start'][number][0] == 'exit':
                            pygame.quit()
                            exit()


def credits_screen():

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                    start_screen()


def single_customisation_screen(lolly, difficulty, power_ups):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                            start_screen()
                        elif buttons['singleplayer'][number][0] == 'start':
                            pass  # single_game(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['singleplayer'][number][0] == 'lolly':
                            lolly_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['singleplayer'][number][0] == 'dog':
                            dog_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['singleplayer'][number][0] == 'power_ups':
                            power_ups_list_screen(mode='single', lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['singleplayer'][number][0] == 'reset':
                            lolly = 'car1'
                            difficulty = 'normal'
                            power_ups = ['diva_defiance', 'frosty_frenzy', 'tangled_twist', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']


def multi_customisation_screen(lolly, bestie, difficulty, power_ups):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                            start_screen()
                        elif buttons['multiplayer'][number][0] == 'start':
                            multi_game(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['multiplayer'][number][0] == 'lolly':
                            lolly_customisation_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['multiplayer'][number][0] == 'dog':
                            dog_customisation_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['multiplayer'][number][0] == 'power_ups':
                            power_ups_list_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['multiplayer'][number][0] == 'bestie':
                            bestie_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons['multiplayer'][number][0] == 'reset':
                            lolly = 'car1'
                            bestie = 'car2'
                            difficulty = 'normal'
                            power_ups = ['sissy_that_walk', 'toy_transforminator', 'besties_in_harmony', 'diva_defiance', 'frosty_frenzy', 'gal_pal_rebirth', 'tangled_twist', 'glamorous_growth']


def dog_customisation_screen(lolly, mode, difficulty, power_ups, bestie=None):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                    menu(screen_image=dog_customisation_image)

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range((len(buttons['select_dog']) -3) , len(buttons['select_dog'])):
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
                            # display the easy dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons['select_dog'][number][0] == 'normal':
                            difficulty = 'normal'
                            # display the normal dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons['select_dog'][number][0] == 'hard':
                            difficulty = 'hard'
                            # display the hard dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons['select_dog'][number][0] == 'back':
                            start_screen()
                            return
                        
                        elif buttons['select_dog'][number][0] == 'return':
                                
                                if mode == 'single':
                                    single_customisation_screen(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                                else:
                                    multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def lolly_customisation_screen(mode, lolly, difficulty, power_ups, bestie=None):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                    menu(screen_image=lolly_customisation_image)

            # if the user hovers over the buttons

            button = None

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(len(buttons['select_character'])):

                if buttons['select_character'][number][1] <= mouse[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= mouse[1] <= buttons['select_character'][number][4]:

                    if lolly == 'car1':  # there's no left arrow
                        if number != 0:  # if the user hovers over anything but the left arrow area
                            button = buttons['select_character'][number][0]

                    elif lolly == 'car2':
                        button = buttons['select_character'][number][0]

                    elif lolly == 'car3':  # there's no right arrow
                        if number != 1:  # if the user hovers over anything but the right arrow area
                            button = buttons['select_character'][number][0]

            if button == None:
                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
            else:
                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_{button}.png").convert_alpha()

            screen.blit(lolly_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(len(buttons['select_character'])):

                    if buttons['select_character'][number][1] <= user_input.pos[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= user_input.pos[1] <= buttons['select_character'][number][4]:

                        if buttons['select_character'][number][0] == 'left':
                                
                            if lolly == 'car2':
                                lolly = 'car1'
                                if bestie == 'car1':
                                    bestie = 'car2'

                            elif lolly == 'car3':
                                lolly = 'car2'
                                if bestie == 'car2':
                                    bestie = 'car3'

                            lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons['select_character'][number][0] == 'right':

                            if lolly == 'car1':
                                lolly = 'car2'
                                if bestie == 'car2':
                                    bestie = 'car1'

                            elif lolly == 'car2':
                                lolly = 'car3'
                                if bestie == 'car3':
                                    bestie = 'car2'

                            lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons['select_character'][number][0] == 'back':
                            start_screen()
                            return
                        
                        elif buttons['select_character'][number][0] == 'return':

                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def bestie_customisation_screen(lolly, bestie, difficulty, power_ups):

    # the bestie should not be able to be the same as the lolly, so we'll display the blocked screen when the arrow is clicked to the selected lolly screem

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                        menu(screen_image=bestie_customisation_image)
    
                # if the user hovers over the buttons
    
                button = None
    
                mouse = pygame.mouse.get_pos()  # getting the mouse position

                for number in range(len(buttons['select_character'])):

                    if buttons['select_character'][number][1] <= mouse[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= mouse[1] <= buttons['select_character'][number][4]:

                        if bestie == 'car1':  # there's no left arrow
                            if number != 0:  # if the user hovers over anything but the left arrow area
                                button = buttons['select_character'][number][0]

                        elif bestie == 'car2':
                            button = buttons['select_character'][number][0]

                        elif bestie == 'car3':  # there's no right arrow
                            if number != 1:  # if the user hovers over anything but the right arrow area
                                button = buttons['select_character'][number][0]

                if button == None:
                    bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                else:
                    bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}_{button}.png").convert_alpha()

                screen.blit(bestie_customisation_image, (0, 0))
                pygame.display.flip()

                # if the user clicks on the buttons

                if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                    for number in range(len(buttons['select_character'])):

                        if buttons['select_character'][number][1] <= user_input.pos[0] <= buttons['select_character'][number][2] and buttons['select_character'][number][3] <= user_input.pos[1] <= buttons['select_character'][number][4]:

                            if buttons['select_character'][number][0] == 'left':

                                if bestie == 'car2':
                                    if lolly == 'car1':
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()
                                    else:
                                        bestie = 'car1'
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()

                                elif bestie == 'car3':
                                    if lolly == 'car2':
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()
                                    else:
                                        bestie = 'car2'
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()

                            elif buttons['select_character'][number][0] == 'right':

                                if bestie == 'car1':
                                    if lolly == 'car2':
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()
                                    else:
                                        bestie = 'car2'
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()

                                elif bestie == 'car2':
                                    if lolly == 'car3':
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()
                                    else:
                                        bestie = 'car3'
                                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                        screen.blit(bestie_customisation_image, (0, 0))
                                        pygame.display.flip()

                            elif buttons['select_character'][number][0] == 'back':
                                start_screen()
                                return
                            
                            elif buttons['select_character'][number][0] == 'return':
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def power_ups_list_screen(mode, lolly, difficulty, power_ups, bestie=None):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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

                        if buttons['power_ups_list'][number][0] == 'back':
                            start_screen()
                            return
                        
                        elif buttons['power_ups_list'][number][0] == 'return':
                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def menu(screen_image):

    menu_position = (451, 799, 201, 749)  # (min_x, max_x, mix_y, max_y)

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

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
                            return

                        elif buttons['menu'][number][0] == 'credits':
                            credits_screen()

                        elif buttons['menu'][number][0] == 'back':
                            start_screen()
                            return

                        elif buttons['menu'][number][0] == 'exit':
                            pygame.quit()
                            exit()