import pygame
from game import multi_game


def start_screen():

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    start_image = pygame.image.load("small_screen/images/interface/start.png").convert_alpha()
    # resize the image to fit the small screen:
    start_image = pygame.transform.scale(start_image, (1250*0.85, 950*0.85))
    screen.blit(start_image, (0, 0))
    pygame.display.flip()

    # inside the start_screen, we have the single-player, multiplayer, credits, and exit buttons
    buttons = [
        ('singleplayer', 955*0.85, 1163*0.85, 460*0.85, 505*0.85),
        ('multiplayer', 965*0.85, 1163*0.85, 568*0.85, 618*0.85),
        ('credits', 1040*0.85, 1163*0.85, 678*0.85, 727*0.85),
        ('exit', 1090*0.85, 1163*0.85, 787*0.85, 838*0.85)
    ]  # (name, min_x, max_x,mix_y, max_y)

    single_power_ups = ['diva_defiance', 'frosty_frenzy', 'girly dash', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']
    multi_power_ups = ['besties_in_harmony', 'diva_defiance', 'frosty_frenzy', 'gal_pal_rebirth', 'girly dash', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(4):  # looping through the buttons, we have 4 in this screen
                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:  # if the mouse is in the button range of width and height
                    button = buttons[number][0]
                    break
            else:  # if the user is not hovering over any button
                button = None

            if button == None:
                start_image = pygame.image.load("small_screen/images/interface/start.png").convert_alpha()
                # resize the image to fit the small screen:
                start_image = pygame.transform.scale(start_image, (1250*0.85, 950*0.85))
            else:
                start_image = pygame.image.load(f"small_screen/images/interface/start_{button}.png").convert_alpha()
                # resize the image to fit the small screen:
                start_image = pygame.transform.scale(start_image, (1250*0.85, 950*0.85))

            screen.blit(start_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(4):
                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:  # if the click is done in the button range of width and height
                        if buttons[number][0] == 'singleplayer':
                            single_customisation_screen(lolly='car1', difficulty='normal', power_ups=single_power_ups)
                        elif buttons[number][0] == 'multiplayer':
                            multi_customisation_screen(lolly='car1', bestie='car2', difficulty='normal', power_ups=multi_power_ups)
                        elif buttons[number][0] == 'credits':
                            credits_screen()
                        elif buttons[number][0] == 'exit':
                            pygame.quit()
                            exit()


def credits_screen():

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    credits_image = pygame.image.load("small_screen/images/interface/credits.png").convert_alpha()
    # resize the image to fit the small screen:
    credits_image = pygame.transform.scale(credits_image, (1250*0.85, 950*0.85))
    screen.blit(credits_image, (0, 0))
    pygame.display.flip()

    back_button_position = (1055*0.85, 1183*0.85, 370*0.85, 420*0.85)  # (min_x, max_x,mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the back button

            mouse = pygame.mouse.get_pos()

            if back_button_position[0] <= mouse[0] <= back_button_position[1] and back_button_position[2] <= mouse[1] <= back_button_position[3]:
                credits_image = pygame.image.load("small_screen/images/interface/credits_back.png").convert_alpha()
                # resize the image to fit the small screen:
                credits_image = pygame.transform.scale(credits_image, (1250*0.85, 950*0.85))
                screen.blit(credits_image, (0, 0))
                pygame.display.flip()

            else:
                credits_image = pygame.image.load("small_screen/images/interface/credits.png").convert_alpha()
                # resize the image to fit the small screen:
                credits_image = pygame.transform.scale(credits_image, (1250*0.85, 950*0.85))
                screen.blit(credits_image, (0, 0))
                pygame.display.flip()

            # if the user clicks on the back button
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                if back_button_position[0] <= user_input.pos[0] <= back_button_position[1] and back_button_position[2] <= user_input.pos[1] <= back_button_position[3]:
                    start_screen()


def single_customisation_screen(lolly, difficulty, power_ups):

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    single_customisation_image = pygame.image.load("small_screen/images/interface/singleplayer.png").convert_alpha()
    # resize the image to fit the small screen:
    single_customisation_image = pygame.transform.scale(single_customisation_image, (1250*0.85, 950*0.85))
    screen.blit(single_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the single_customisation_screen, we have the back, start, lolly, dog, power-ups, and reset buttons
    # every value multiplied by 0.85 to fit the small screen:
    buttons = [
    ('back', 80*0.85, 203*0.85, 860*0.85, 910*0.85),
    ('start', 238*0.85, 465*0.85, 860*0.85, 910*0.85),
    ('lolly', 250*0.85, 531*0.85, 250*0.85, 425*0.85),
    ('dog', 667*0.85, 948*0.85, 250*0.85, 425*0.85),
    ('power_ups', 250*0.85, 531*0.85, 515*0.85, 700*0.85),
    ('reset', 568*0.85, 630*0.85, 442*0.85, 509*0.85)
    ]  # (name, min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(6):  # looping through the buttons, we have 6 in this screen
                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:
                    button = buttons[number][0]
                    break
            else:  # if the user is not hovering over any button
                button = None

            if button == None:
                single_customisation_image = pygame.image.load("small_screen/images/interface/singleplayer.png").convert_alpha()
                # resize the image to fit the small screen:
                single_customisation_image = pygame.transform.scale(single_customisation_image, (1250*0.85, 950*0.85))
            else:
                single_customisation_image = pygame.image.load(f"small_screen/images/interface/singleplayer_{button}.png").convert_alpha()
                # resize the image to fit the small screen:
                single_customisation_image = pygame.transform.scale(single_customisation_image, (1250*0.85, 950*0.85))

            screen.blit(single_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(6):
                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:
                        if buttons[number][0] == 'back':
                            start_screen()
                        elif buttons[number][0] == 'start':
                            pass  # single_game(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'lolly':
                            lolly_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'dog':
                            dog_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'power_ups':
                            pass  # power_ups_customisation_screen(mode='single', lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'reset':
                            reset_customisation('single')


def multi_customisation_screen(lolly, bestie, difficulty, power_ups):

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    multi_customisation_image = pygame.image.load("small_screen/images/interface/multiplayer.png").convert_alpha()
    # resize the image to fit the small screen:
    multi_customisation_image = pygame.transform.scale(multi_customisation_image, (1250*0.85, 950*0.85))
    screen.blit(multi_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the multi_customisation_screen, we have the back, start, lolly, dog, bestie, power-ups, and reset buttons
    # every value multiplied by 0.85 to fit the small screen:
    buttons = [
    ('back', 80*0.85, 203*0.85, 860*0.85, 910*0.85),
    ('start', 238*0.85, 465*0.85, 860*0.85, 910*0.85),
    ('lolly', 250*0.85, 531*0.85, 250*0.85, 425*0.85),
    ('dog', 667*0.85, 948*0.85, 250*0.85, 425*0.85),
    ('power_ups', 250*0.85, 531*0.85, 515*0.85, 700*0.85),
    ('bestie', 667*0.85, 948*0.85, 515*0.85, 700*0.85),
    ('reset', 568*0.85, 630*0.85, 442*0.85, 509*0.85)
    ]  # (name, min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(7):  # looping through the buttons, we have 7 in this screen
                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:
                    button = buttons[number][0]
                    break
            else:  # if the user is not hovering over any button
                button = None

            if button == None:
                multi_customisation_image = pygame.image.load("small_screen/images/interface/multiplayer.png").convert_alpha()
                # resize the image to fit the small screen:
                multi_customisation_image = pygame.transform.scale(multi_customisation_image, (1250*0.85, 950*0.85))
            else:
                multi_customisation_image = pygame.image.load(f"small_screen/images/interface/multiplayer_{button}.png").convert_alpha()
                # resize the image to fit the small screen:
                multi_customisation_image = pygame.transform.scale(multi_customisation_image, (1250*0.85, 950*0.85))

            screen.blit(multi_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(7):
                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:
                        if buttons[number][0] == 'back':
                            start_screen()
                        elif buttons[number][0] == 'start':
                            multi_game(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'lolly':
                            lolly_customisation_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'dog':
                            dog_customisation_screen(mode='multi', lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'power_ups':
                            pass  # power_ups_customisation_screen('multi', power_ups)
                        elif buttons[number][0] == 'bestie':
                            bestie_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
                        elif buttons[number][0] == 'reset':
                            reset_customisation('multi')


def reset_customisation(mode):

    if mode == 'single':  # if the user is in the single_customisation_screen
        single_customisation_screen(lolly='car1', difficulty='normal', power_ups=['diva_defiance', 'frosty_frenzy', 'girly dash', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator'])
    else:  # if the user is in the multi_customisation_screen
        multi_customisation_screen(lolly='car1', bestie='car2', difficulty='normal', power_ups=['besties_in_harmony', 'diva_defiance', 'frosty_frenzy', 'gal_pal_rebirth', 'girly dash', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator'])


def dog_customisation_screen(lolly, mode, difficulty, power_ups, bestie=None):

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    dog_customisation_image = pygame.image.load(f"small_screen/images/interface/select_dog_{difficulty}.png").convert_alpha()
    # resize the image to fit the small screen:
    dog_customisation_image = pygame.transform.scale(dog_customisation_image, (1250*0.85, 950*0.85))
    screen.blit(dog_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the dog_customisation_screen, we have the easy, normal, hard, info, back, and return buttons
    # every value multiplied by 0.85 to fit the small screen:
    buttons = [
        ('easy', 154*0.85, 365*0.85, 364*0.85, 450*0.85),
        ('normal', 492*0.85, 702*0.85, 364*0.85, 450*0.85),
        ('hard', 836*0.85, 1046*0.85, 364*0.85, 450*0.85),
        ('info', 113*0.85, 169*0.85, 156*0.85, 213*0.85),
        ('back', 77*0.85, 207*0.85, 859*0.85, 912*0.85),
        ('return', 230*0.85, 359*0.85, 859*0.85, 912*0.85)
    ]  # (name, min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(3,6):  # looping through the buttons, we have 6 in this screen
                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:
                    button = buttons[number][0]
                    break
            else:  # if the user is not hovering over any button
                button = None

            if button == None:
                dog_customisation_image = pygame.image.load(f"small_screen/images/interface/select_dog_{difficulty}.png").convert_alpha()
                # resize the image to fit the small screen:
                dog_customisation_image = pygame.transform.scale(dog_customisation_image, (1250*0.85, 950*0.85))
            else:
                dog_customisation_image = pygame.image.load(f"small_screen/images/interface/select_dog_{difficulty}_{button}.png").convert_alpha()
                # resize the image to fit the small screen:
                dog_customisation_image = pygame.transform.scale(dog_customisation_image, (1250*0.85, 950*0.85))

            screen.blit(dog_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(6):

                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:

                        if buttons[number][0] == 'easy':
                            difficulty = 'easy'
                            # display the easy dog
                            dog_customisation_image = pygame.image.load(f"small_screen/images/interface/select_dog_{difficulty}.png").convert_alpha()
                            # resize the image to fit the small screen:
                            dog_customisation_image = pygame.transform.scale(dog_customisation_image, (1250*0.85, 950*0.85))
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'normal':
                            difficulty = 'normal'
                            # display the normal dog
                            dog_customisation_image = pygame.image.load(f"small_screen/images/interface/select_dog_{difficulty}.png").convert_alpha()
                            # resize the image to fit the small screen:
                            dog_customisation_image = pygame.transform.scale(dog_customisation_image, (1250*0.85, 950*0.85))
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'hard':
                            difficulty = 'hard'
                            # display the hard dog
                            dog_customisation_image = pygame.image.load(f"small_screen/images/interface/select_dog_{difficulty}.png").convert_alpha()
                            # resize the image to fit the small screen:
                            dog_customisation_image = pygame.transform.scale(dog_customisation_image, (1250*0.85, 950*0.85))
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'info':
                            pass  # display info

                        elif buttons[number][0] == 'back':
                            start_screen()
                            return

                        elif buttons[number][0] == 'return':

                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def lolly_customisation_screen(lolly, mode, difficulty, power_ups, bestie=None):

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    lolly_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}.png").convert_alpha()
    # resize the image to fit the small screen:
    lolly_customisation_image = pygame.transform.scale(lolly_customisation_image, (1250*0.85, 950*0.85))
    screen.blit(lolly_customisation_image, (0, 0))
    pygame.display.flip()

    # in the Lolly customisation screen, we have the left arrow, right arrow, back, and return buttons
    # every value multiplied by 0.85 to fit the small screen:
    buttons = [
        ('left', 200*0.85, 250*0.85, 446*0.85, 563*0.85),
        ('right', 945*0.85, 995*0.85, 446*0.85, 563*0.85),
        ('back', 77*0.85, 207*0.85, 859*0.85, 912*0.85),
        ('return', 230*0.85, 359*0.85, 859*0.85, 912*0.85)
        ] # (name, min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            button = None

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(4):  # looping through the buttons, we have 4 in this screen
                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:
                    
                    if lolly == 'car1':  # there's no left arrow
                        if number != 0:  # if the user hovers over anything but the left arrow area
                            button = buttons[number][0]

                    elif lolly == 'car2':
                        button = buttons[number][0]

                    elif lolly == 'car3':  # there's no right arrow
                        if number != 1:  # if the user hovers over anything but the right arrow area
                            button = buttons[number][0]

            if button == None:
                lolly_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}.png").convert_alpha()
                # resize the image to fit the small screen:
                lolly_customisation_image = pygame.transform.scale(lolly_customisation_image, (1250*0.85, 950*0.85))
            else:
                lolly_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}_{button}.png").convert_alpha()
                # resize the image to fit the small screen:
                lolly_customisation_image = pygame.transform.scale(lolly_customisation_image, (1250*0.85, 950*0.85))
            
            screen.blit(lolly_customisation_image, (0, 0))
            pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(4):

                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:

                        if buttons[number][0] == 'left':  # if the user clicks on the left arrow

                            if lolly == 'car2':
                                lolly = 'car1'
                                if bestie == 'car1':
                                    bestie = 'car2'

                            elif lolly == 'car3':
                                lolly = 'car2'
                                if bestie == 'car2':
                                    bestie = 'car3'

                            lolly_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}.png").convert_alpha()
                            # resize the image to fit the small screen:
                            lolly_customisation_image = pygame.transform.scale(lolly_customisation_image, (1250*0.85, 950*0.85))
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'right':  # if the user clicks on the right arrow

                            if lolly == 'car1':
                                lolly = 'car2'
                                if bestie == 'car2':
                                    bestie = 'car1'

                            elif lolly == 'car2':
                                lolly = 'car3'
                                if bestie == 'car3':
                                    bestie = 'car2'

                            lolly_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}.png").convert_alpha()
                            # resize the image to fit the small screen:
                            lolly_customisation_image = pygame.transform.scale(lolly_customisation_image, (1250*0.85, 950*0.85))
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'back':
                            start_screen()
                            return

                        elif buttons[number][0] == 'return':

                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def bestie_customisation_screen(lolly, bestie, difficulty, power_ups):

    # the bestie should not be able to be the same as the lolly, so we'll display the blocked screen when the arrow is clicked to the selected lolly screem

    pygame.init()
    size = (1250*0.85, 950*0.85)
    screen = pygame.display.set_mode(size)

    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}.png").convert_alpha()
    # resize the image to fit the small screen:
    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
    screen.blit(bestie_customisation_image, (0, 0))
    pygame.display.flip()

    # in the Bestie customisation screen, we have the left arrow, right arrow, back, and return buttons
    # every value multiplied by 0.85 to fit the small screen:
    buttons = [
        ('left', 200*0.85, 250*0.85, 446*0.85, 563*0.85),
        ('right', 945*0.85, 995*0.85, 446*0.85, 563*0.85),
        ('back', 77*0.85, 207*0.85, 859*0.85, 912*0.85),
        ('return', 230*0.85, 359*0.85, 859*0.85, 912*0.85)
        ] # (name, min_x, max_x, mix_y, max_y)
    
    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            button = None

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(4):  # looping through the buttons, we have 4 in this screen

                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:

                    if bestie == 'car1':  # there's no left arrow
                        if number != 0:  # if the user hovers over anything but the left arrow area
                            button = buttons[number][0]

                    elif bestie == 'car2':
                        button = buttons[number][0]

                    elif bestie == 'car3':  # there's no right arrow
                        if number != 1:  # if the user hovers over anything but the right arrow area
                            button = buttons[number][0]

            if button == None:
                bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}.png").convert_alpha()
                # resize the image to fit the small screen:
                bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
            else:
                bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}_{button}.png").convert_alpha()
                # resize the image to fit the small screen:
                bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(4):
                        
                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:

                        if buttons[number][0] == 'left':

                            if bestie == 'car2':
                                if lolly == 'car1':
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()
                                else:
                                    bestie = 'car1'
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()

                            elif bestie == 'car3':
                                if lolly == 'car2':
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()
                                else:
                                    bestie = 'car2'
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()

                        elif buttons[number][0] == 'right':

                            if bestie == 'car1':
                                if lolly == 'car2':
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()
                                else:
                                    bestie = 'car2'
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()

                            elif bestie == 'car2':
                                if lolly == 'car3':
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{lolly}_blocked.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()
                                else:
                                    bestie = 'car3'
                                    bestie_customisation_image = pygame.image.load(f"small_screen/images/interface/select_character_{bestie}.png").convert_alpha()
                                    # resize the image to fit the small screen:
                                    bestie_customisation_image = pygame.transform.scale(bestie_customisation_image, (1250*0.85, 950*0.85))
                                    screen.blit(bestie_customisation_image, (0, 0))
                                    pygame.display.flip()

                        elif buttons[number][0] == 'back':
                            start_screen()
                            return

                        elif buttons[number][0] == 'return':
                            multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)
