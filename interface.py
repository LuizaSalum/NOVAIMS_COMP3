import pygame
from game import multi_game


def start_screen():

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    start_image = pygame.image.load("images/interface/start.png").convert_alpha()
    screen.blit(start_image, (0, 0))
    pygame.display.flip()

    # inside the start_screen, we have the single-player, multiplayer, credits, and exit buttons
    buttons = [
        ('singleplayer', 955, 1163, 460, 505),
        ('multiplayer', 965, 1163, 568, 618),
        ('credits', 1040, 1163, 678, 727),
        ('exit', 1090, 1163, 787, 838)
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
                    start_image = pygame.image.load(f"images/interface/start_{buttons[number][0]}.png").convert_alpha()
                    screen.blit(start_image, (0, 0))
                    pygame.display.flip()
                else:  # if the user is not hovering over any button
                    start_image = pygame.image.load("images/interface/start.png").convert_alpha()
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

    # inside the single_customisation_screen, we have the back, start, lolly, dog, power-ups, and reset buttons
    buttons = [
    ('back', 80, 203, 860, 910),
    ('start', 238, 465, 860, 910),
    ('lolly', 250, 531, 250, 425),
    ('dog', 667, 948, 250, 425),
    ('power_ups', 250, 531, 515, 700),
    ('reset', 568, 630, 442, 509)
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
                    single_customisation_image = pygame.image.load(f"images/interface/singleplayer_{buttons[number][0]}.png").convert_alpha()
                    screen.blit(single_customisation_image, (0, 0))
                    pygame.display.flip()
                else:  # if the user is not hovering over any button
                    single_customisation_image = pygame.image.load("images/interface/singleplayer.png").convert_alpha()
                    screen.blit(single_customisation_image, (0, 0))
                    pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(6):
                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:
                        if buttons[number][0] == 'back':
                            start_screen()
                        elif buttons[number][0] == 'start':
                            single_game(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
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
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    multi_customisation_image = pygame.image.load("images/interface/multiplayer.png").convert_alpha()
    screen.blit(multi_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the multi_customisation_screen, we have the back, start, lolly, dog, bestie, power-ups, and reset buttons
    buttons = [
    ('back', 80, 203, 860, 910),
    ('start', 238, 465, 860, 910),
    ('lolly', 250, 531, 250, 425),
    ('dog', 667, 948, 250, 425),
    ('power_ups', 250, 531, 515, 700),
    ('bestie', 667, 948, 515, 700),
    ('reset', 568, 630, 442, 509)
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
                    multi_customisation_image = pygame.image.load(f"images/interface/multiplayer_{buttons[number][0]}.png").convert_alpha()
                    screen.blit(multi_customisation_image, (0, 0))
                    pygame.display.flip()
                else:  # if the user is not hovering over any button
                    multi_customisation_image = pygame.image.load("images/interface/multiplayer.png").convert_alpha()
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


def dog_customisation_screen(lolly, bestie, mode, difficulty, power_ups):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
    screen.blit(dog_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the dog_customisation_screen, we have the easy, normal, hard, info, back, and return buttons
    buttons = [
        ('easy', 154, 365, 364, 450),
        ('normal', 492, 702, 364, 450),
        ('hard', 836, 1046, 364, 450),
        ('info', 113, 169, 156, 213),
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
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
                    dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{buttons[number][0]}.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()
                else:  # if the user is not hovering over any button
                    dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(6):

                    if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:

                        if buttons[number][0] == 'easy':
                            difficulty = 'easy'
                            # display the easy dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'normal':
                            difficulty = 'normal'
                            # display the normal dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'hard':
                            difficulty = 'hard'
                            # display the hard dog
                            dog_customisation_image = pygame.image.load(f"images/interface/select_dog_{difficulty}.png").convert_alpha()
                            screen.blit(dog_customisation_image, (0, 0))
                            pygame.display.flip()

                        elif buttons[number][0] == 'info':
                            pass  # display info

                        elif buttons[number][0] == 'back':
                            start_screen()

                        elif buttons[number][0] == 'return':

                            if mode == 'single':
                                single_customisation_screen(lolly=lolly, difficulty=difficulty, power_ups=power_ups)
                            else:
                                multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)


def lolly_customisation_screen(lolly, mode, difficulty, power_ups, bestie=None):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
    screen.blit(lolly_customisation_image, (0, 0))
    pygame.display.flip()

    # in the Lolly customisation screen, we have the left arrow, right arrow, back, and return buttons
    buttons = [
        ('left', 200, 250, 446, 563),
        ('right', 945, 995, 446, 563),
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
        ] # (name, min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(4):  # looping through the buttons, we have 4 in this screen
                if buttons[number][1] <= mouse[0] <= buttons[number][2] and buttons[number][3] <= mouse[1] <= buttons[number][4]:
                    lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}_{buttons[number][0]}.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()
                else:
                    lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
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
    
                                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
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
    
                                lolly_customisation_image = pygame.image.load(f"images/interface/select_character_{lolly}.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()
    
                            elif buttons[number][0] == 'back':
                                start_screen()
    
                            elif buttons[number][0] == 'return':
    
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

    # in the Bestie customisation screen, we have the left arrow, right arrow, back, and return buttons
    buttons = [
        ('left', 200, 250, 446, 563),
        ('right', 945, 995, 446, 563),
        ('back', 77, 207, 859, 912),
        ('return', 230, 359, 859, 912)
        ] # (name, min_x, max_x, mix_y, max_y)
    
    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()  # getting the mouse position

            for number in range(4):  # looping through the buttons, we have 4 in this screen

                if bestie == 'car1':  # there's no left arrow
                    if number == 0:  # if the user hovers over the left arrow area
                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                        screen.blit(bestie_customisation_image, (0, 0))
                        pygame.display.flip()
                    else:
                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}_{buttons[number][0]}.png").convert_alpha()
                        screen.blit(bestie_customisation_image, (0, 0))
                        pygame.display.flip()

                elif bestie == 'car2':
                    bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}_{buttons[number][0]}.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                elif bestie == 'car3':  # there's no right arrow
                    if number == 1:  # if the user hovers over the right arrow area
                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                        screen.blit(bestie_customisation_image, (0, 0))
                        pygame.display.flip()
                    else:
                        bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}_{buttons[number][0]}.png").convert_alpha()
                        screen.blit(bestie_customisation_image, (0, 0))
                        pygame.display.flip()


            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:  # if the user clicks on the screen

                for number in range(4):
                        
                            if buttons[number][1] <= user_input.pos[0] <= buttons[number][2] and buttons[number][3] <= user_input.pos[1] <= buttons[number][4]:
        
                                if buttons[number][0] == 'left':

                                    if bestie == 'car2':
                                        if lolly == 'car1':
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_blocked_{lolly}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()
                                        else:
                                            bestie = 'car1'
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()

                                    elif bestie == 'car3':
                                        if lolly == 'car2':
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_blocked_{lolly}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()
                                        else:
                                            bestie = 'car2'
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()

                                elif buttons[number][0] == 'right':

                                    if bestie == 'car1':
                                        if lolly == 'car2':
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_blocked_{lolly}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()
                                        else:
                                            bestie = 'car2'
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()

                                    elif bestie == 'car2':
                                        if lolly == 'car3':
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_blocked_{lolly}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()
                                        else:
                                            bestie = 'car3'
                                            bestie_customisation_image = pygame.image.load(f"images/interface/select_character_{bestie}.png").convert_alpha()
                                            screen.blit(bestie_customisation_image, (0, 0))
                                            pygame.display.flip()

                                elif buttons[number][0] == 'back':
                                    start_screen()

                                elif buttons[number][0] == 'return':
                                    multi_customisation_screen(lolly=lolly, bestie=bestie, difficulty=difficulty, power_ups=power_ups)

