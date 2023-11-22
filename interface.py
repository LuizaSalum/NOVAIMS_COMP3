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
    buttons_positions = [
        (955, 1163, 460, 505),
        (965, 1163, 568, 618),
        (1040, 1163, 678, 727),
        (1090, 1163, 787, 838)
    ]  # (min_x, max_x,mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()

            # if the user hovers over the single-player button
            if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                start_image = pygame.image.load("images/interface/start_singleplayer.png").convert_alpha()
                screen.blit(start_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the multiplayer button
            if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                start_image = pygame.image.load("images/interface/start_multiplayer.png").convert_alpha()
                screen.blit(start_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the credits button
            if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                start_image = pygame.image.load("images/interface/start_credits.png").convert_alpha()
                screen.blit(start_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the exit button
            if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                start_image = pygame.image.load("images/interface/start_exit.png").convert_alpha()
                screen.blit(start_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over nothing
            if not (buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]) \
                    and not (buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]) \
                    and not (buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]) \
                    and not (buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]):
                start_image = pygame.image.load("images/interface/start.png").convert_alpha()
                screen.blit(start_image, (0, 0))
                pygame.display.flip()

            # if the user clicks on the buttons
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                # if the user clicks on the single-player button
                if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                    single_customisation_screen()

                # if the user clicks on the multiplayer button
                if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                    multi_customisation_screen()

                # if the user clicks on the credits button
                if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:
                    credits_screen()

                # if the user clicks on the exit button
                if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                    pygame.quit()
                    exit()


def single_customisation_screen():

    lolly = 'car1'
    difficulty = 'normal'
    power_ups = ['besties_in_harmony', 'diva_defiance', 'frosty_frenzy', 'gal_pal_rebirth', 'girly dash', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    single_customisation_image = pygame.image.load("images/interface/singleplayer.png").convert_alpha()
    screen.blit(single_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the single_customisation_screen, we have the back, start, lolly, dog, power-ups, and reset buttons
    buttons_positions = [
        (80, 203, 860, 910),
        (238, 465, 860, 910),
        (250, 531, 250, 425),
        (667, 948, 250, 425),
        (250, 531, 515, 700),
        (568, 630, 442, 509)
    ]  # (min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()

            # if the user hovers over the back button
            if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                single_customisation_image = pygame.image.load("images/interface/singleplayer_back.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the start button
            if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                single_customisation_image = pygame.image.load("images/interface/singleplayer_start.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the lolly button
            if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                single_customisation_image = pygame.image.load("images/interface/singleplayer_lolly.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the dog button
            if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                single_customisation_image = pygame.image.load("images/interface/singleplayer_dog.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the power-ups button
            if buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]:
                single_customisation_image = pygame.image.load("images/interface/singleplayer_power_ups.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the reset button
            if buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]:
                single_customisation_image = pygame.image.load("images/interface/singleplayer_reset.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over nothing
            if not (buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]) \
                    and not (buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]) \
                    and not (buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]) \
                    and not (buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]) \
                    and not (buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]) \
                    and not (buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]):
                single_customisation_image = pygame.image.load("images/interface/singleplayer.png").convert_alpha()
                screen.blit(single_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user clicks on the buttons
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                # if the user clicks on the back button
                if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                    start_screen()

                # if the user clicks on the start button
                if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                    pass  # single_game() # TO-DO: singleplayer game

                # if the user clicks on the lolly button
                if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:
                    lolly_customisation_screen('single', lolly)

                # if the user clicks on the dog button
                if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                    dog_customisation_screen('single', difficulty)

                # if the user clicks on the power-ups button
                if buttons_positions[4][0] <= user_input.pos[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= user_input.pos[1] <= buttons_positions[4][3]:
                    pass
                    ''' TO-DO: power-ups customisation '''

                # if the user clicks on the reset button
                if buttons_positions[5][0] <= user_input.pos[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= user_input.pos[1] <= buttons_positions[5][3]:
                    reset_customisation('single')


def multi_customisation_screen():

    difficulty = 'normal'
    lolly = 'car1'
    bestie = 'car2'

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    multi_customisation_image = pygame.image.load("images/interface/multiplayer.png").convert_alpha()
    screen.blit(multi_customisation_image, (0, 0))
    pygame.display.flip()

    # inside the multi_customisation_screen, we have the back, start, lolly, dog, power-ups, bestie, and reset buttons
    buttons_positions = [
        (80, 203, 860, 910),
        (238, 465, 860, 910),
        (250, 531, 250, 425),
        (667, 948, 250, 425),
        (250, 531, 515, 700),
        (667, 948, 515, 700),
        (568, 630, 442, 509)
        ]  # (min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()

            # if the user hovers over the back button
            if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_back.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the start button
            if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_start.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the lolly button
            if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_lolly.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the dog button
            if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_dog.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the power-ups button
            if buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_power_ups.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the bestie button
            if buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_bestie.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the reset button
            if buttons_positions[6][0] <= mouse[0] <= buttons_positions[6][1] and buttons_positions[6][2] <= mouse[1] <= buttons_positions[6][3]:
                multi_customisation_image = pygame.image.load("images/interface/multiplayer_reset.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over nothing
            if not (buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]) \
                    and not (buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]) \
                    and not (buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]) \
                    and not (buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]) \
                    and not (buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]) \
                    and not (buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]) \
                    and not (buttons_positions[6][0] <= mouse[0] <= buttons_positions[6][1] and buttons_positions[6][2] <= mouse[1] <= buttons_positions[6][3]):
                multi_customisation_image = pygame.image.load("images/interface/multiplayer.png").convert_alpha()
                screen.blit(multi_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user clicks on the buttons
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                # if the user clicks on the back button
                if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                    start_screen()

                # if the user clicks on the start button
                if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                    multi_game('easy', 'car1', 'car2', ['diva_defiance', 'frosty_frenzy'])

                # if the user clicks on the lolly button
                if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:
                    lolly_customisation_screen('multi', lolly, bestie)

                # if the user clicks on the dog button
                if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                    dog_customisation_screen('multi', difficulty)

                # if the user clicks on the power-ups button
                if buttons_positions[4][0] <= user_input.pos[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= user_input.pos[1] <= buttons_positions[4][3]:
                    pass
                    ''' TO-DO: power-ups customisation '''

                # if the user clicks on the bestie button
                if buttons_positions[5][0] <= user_input.pos[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= user_input.pos[1] <= buttons_positions[5][3]:
                    bestie_customisation_screen(lolly, bestie)

                # if the user clicks on the reset button
                if buttons_positions[6][0] <= user_input.pos[0] <= buttons_positions[6][1] and buttons_positions[6][2] <= user_input.pos[1] <= buttons_positions[6][3]:
                    reset_customisation('multi')


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

            if not (back_button_position[0] <= mouse[0] <= back_button_position[1] and back_button_position[2] <= mouse[1] <= back_button_position[3]):
                credits_image = pygame.image.load("images/interface/credits.png").convert_alpha()
                screen.blit(credits_image, (0, 0))
                pygame.display.flip()

            # if the user clicks on the back button
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                if back_button_position[0] <= user_input.pos[0] <= back_button_position[1] and back_button_position[2] <= user_input.pos[1] <= back_button_position[3]:
                    start_screen()


def reset_customisation(single_or_multi):

    difficulty = 'normal'
    lolly = 'car1'
    power_ups = ['besties_in_harmony', 'diva_defiance', 'frosty_frenzy', 'gal_pal_rebirth', 'girly dash', 'glamorous_growth', 'sissy_that_walk', 'toy_transforminator']
    if single_or_multi == 'multi':
        bestie = 'car2'
        return difficulty, lolly, power_ups, bestie
    else:
        return difficulty, lolly, power_ups


def dog_customisation_screen(single_or_multi, difficulty):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    if difficulty == 'easy':
        dog_customisation_image = pygame.image.load("images/interface/select_dog_easy.png").convert_alpha()
        screen.blit(dog_customisation_image, (0, 0))
        pygame.display.flip()

    elif difficulty == 'normal':
        dog_customisation_image = pygame.image.load("images/interface/select_dog_normal.png").convert_alpha()
        screen.blit(dog_customisation_image, (0, 0))
        pygame.display.flip()

    elif difficulty == 'hard':
        dog_customisation_image = pygame.image.load("images/interface/select_dog_hard.png").convert_alpha()
        screen.blit(dog_customisation_image, (0, 0))
        pygame.display.flip()

    # inside the dog_customisation_screen, we have the easy, normal, hard, info, back, and return buttons
    buttons_positions = [
        (154, 365, 364, 450),
        (492, 702, 364, 450),
        (836, 1046, 364, 450),
        (113, 169, 156, 213),
        (77, 207, 859, 912),
        (230, 359, 859, 912)
    ]  # (min_x, max_x, mix_y, max_y)

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()

            # if the user hovers over the easy button
            if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                dog_customisation_image = pygame.image.load("images/interface/select_dog_easy.png").convert_alpha()
                screen.blit(dog_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the normal button
            if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                dog_customisation_image = pygame.image.load("images/interface/select_dog_normal.png").convert_alpha()
                screen.blit(dog_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the hard button
            if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                dog_customisation_image = pygame.image.load("images/interface/select_dog_hard.png").convert_alpha()
                screen.blit(dog_customisation_image, (0, 0))
                pygame.display.flip()

            # if the user hovers over the info, back or return button
            if difficulty == 'easy':
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_easy_info.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                if buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_easy_back.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                if buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_easy_return.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

            elif difficulty == 'normal':
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_normal_info.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                if buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_normal_back.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                if buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_normal_return.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

            elif difficulty == 'hard':
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_hard_info.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                if buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_hard_back.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                if buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]:
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_hard_return.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

            # if the user hovers over nothing, the difficulty button that was selected will stay selected
            if not (buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]) \
                    and not (buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]) \
                    and not (buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]) \
                    and not (buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]) \
                    and not (buttons_positions[4][0] <= mouse[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= mouse[1] <= buttons_positions[4][3]) \
                    and not (buttons_positions[5][0] <= mouse[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= mouse[1] <= buttons_positions[5][3]):

                if difficulty == 'easy':
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_easy.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                elif difficulty == 'normal':
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_normal.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                elif difficulty == 'hard':
                    dog_customisation_image = pygame.image.load("images/interface/select_dog_hard.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

            # if the user clicks on the buttons
            if user_input.type == pygame.MOUSEBUTTONDOWN:

                # if the user clicks on the easy button
                if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:

                    dog_customisation_image = pygame.image.load("images/interface/select_dog_easy.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                    difficulty = 'easy'

                    ''' TO-DO: easy difficulty in the game '''

                # if the user clicks on the normal button
                if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:

                    dog_customisation_image = pygame.image.load("images/interface/select_dog_normal.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                    difficulty = 'normal'

                    ''' TO-DO: normal difficulty in the game '''

                # if the user clicks on the hard button
                if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:

                    dog_customisation_image = pygame.image.load("images/interface/select_dog_hard.png").convert_alpha()
                    screen.blit(dog_customisation_image, (0, 0))
                    pygame.display.flip()

                    difficulty = 'hard'

                    ''' TO-DO: hard difficulty in the game '''

                # if the user clicks on the info button
                if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                    pass
                    ''' TO-DO: info dog customisation '''

                # if the user clicks on the back button
                if buttons_positions[4][0] <= user_input.pos[0] <= buttons_positions[4][1] and buttons_positions[4][2] <= user_input.pos[1] <= buttons_positions[4][3]:
                    start_screen()

                # if the user clicks on the return button
                if buttons_positions[5][0] <= user_input.pos[0] <= buttons_positions[5][1] and buttons_positions[5][2] <= user_input.pos[1] <= buttons_positions[5][3]:
                    if single_or_multi == 'single':
                        single_customisation_screen()
                    elif single_or_multi == 'multi':
                        multi_customisation_screen()


def lolly_customisation_screen(single_or_multi, lolly, bestie=None):

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    if lolly == 'car1':
        lolly_customisation_image = pygame.image.load("images/interface/select_character_car1.png").convert_alpha()
        screen.blit(lolly_customisation_image, (0, 0))
        pygame.display.flip()

    elif lolly == 'car2':
        lolly_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
        screen.blit(lolly_customisation_image, (0, 0))
        pygame.display.flip()

    elif lolly == 'car3':
        lolly_customisation_image = pygame.image.load("images/interface/select_character_car3.png").convert_alpha()
        screen.blit(lolly_customisation_image, (0, 0))
        pygame.display.flip()

    # in the Lolly customisation screen, we have the left arrow, right arrow, back, and return buttons
    buttons_positions = [
        (200, 250, 446, 563),
        (945, 995, 446, 563),
        (77, 207, 859, 912),
        (230, 359, 859, 912)
    ]

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()

            if lolly == 'car1':

                # if the user hovers over the right arrow
                if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_right.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_back.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_return.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

            elif lolly == 'car2':

                # if the user hovers over the left arrow
                if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_left.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the right arrow
                if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_right.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_back.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_return.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

            elif lolly == 'car3':

                # if the user hovers over the left arrow
                if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_left.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_back.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_return.png").convert_alpha()
                    screen.blit(lolly_customisation_image, (0, 0))
                    pygame.display.flip()

            if single_or_multi == 'multi':

                if bestie == 'car1':

                    # if the user hovers over the right arrow
                    if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked_right.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the back button
                    if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked_back.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the return button
                    if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked_return.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                elif bestie == 'car2':

                    # if the user hovers over the left arrow
                    if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_left.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the right arrow
                    if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_right.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the back button
                    if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_back.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the return button
                    if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_return.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                elif bestie == 'car3':

                    # if the user hovers over the left arrow
                    if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked_left.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the back button
                    if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked_back.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

                    # if the user hovers over the return button
                    if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                        lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked_return.png").convert_alpha()
                        screen.blit(lolly_customisation_image, (0, 0))
                        pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                if single_or_multi == 'multi':

                    if bestie == 'car1':  # the car1 screen will be blocked

                        if lolly == 'car2':  # if they click the left button, we'll display the blocked car1 screen, if they click the right button, we'll display the car3 screen, and car3 will be the new lolly car

                            if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:  # if the user clicks on the left arrow
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()

                            if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:  # if the user clicks on the right arrow
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car3.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()
                                lolly = 'car3'

                        elif lolly == 'car3':

                            # if the user clicks on the left arrow
                            if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()
                                lolly = 'car2'

                    elif bestie == 'car2':  # the car2 screen will be blocked

                        if lolly == 'car1':

                            # if the user clicks on the right arrow
                            if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()

                        elif lolly == 'car3':

                            # if the user clicks on the left arrow
                            if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()

                    elif bestie == 'car3':  # the car3 screen will be blocked

                        if lolly == 'car1':

                            # if the user clicks on the right arrow
                            if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()
                                lolly = 'car2'

                        elif lolly == 'car2':

                            # if the user clicks on the left arrow
                            if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car1.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()
                                lolly = 'car1'

                            # if the user clicks on the right arrow
                            if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                                lolly_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked.png").convert_alpha()
                                screen.blit(lolly_customisation_image, (0, 0))
                                pygame.display.flip()

                    # if the user clicks on the back button
                    if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:
                        start_screen()

                    # if the user clicks on the return button
                    if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                        multi_customisation_screen()

                elif single_or_multi == 'single':

                    # if the user clicks on the left arrow
                    if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:

                        if lolly == 'car2':
                            lolly_customisation_image = pygame.image.load("images/interface/select_character_car1.png").convert_alpha()
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()
                            lolly = 'car1'

                        elif lolly == 'car3':
                            lolly_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()
                            lolly = 'car2'

                    # if the user clicks on the right arrow
                    if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:

                        if lolly == 'car1':
                            lolly_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()
                            lolly = 'car2'

                        elif lolly == 'car2':
                            lolly_customisation_image = pygame.image.load("images/interface/select_character_car3.png").convert_alpha()
                            screen.blit(lolly_customisation_image, (0, 0))
                            pygame.display.flip()
                            lolly = 'car3'

                    # if the user clicks on the back button
                    if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:
                        start_screen()

                    # if the user clicks on the return button
                    if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                        single_customisation_screen()


def bestie_customisation_screen(lolly, bestie):  # this will be the same as the lolly customisation, but we don't need to check if it's multi or single, because it's always multiplayer

    pygame.init()
    size = (1250, 950)
    screen = pygame.display.set_mode(size)

    if bestie == 'car1':
        bestie_customisation_image = pygame.image.load("images/interface/select_character_car1.png").convert_alpha()
        screen.blit(bestie_customisation_image, (0, 0))
        pygame.display.flip()

    elif bestie == 'car2':
        bestie_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
        screen.blit(bestie_customisation_image, (0, 0))
        pygame.display.flip()

    elif bestie == 'car3':
        bestie_customisation_image = pygame.image.load("images/interface/select_character_car3.png").convert_alpha()
        screen.blit(bestie_customisation_image, (0, 0))
        pygame.display.flip()

    # the buttons are in the same positions as the lolly customisation screen, we have the left arrow, right arrow, back, and return buttons
    buttons_positions = [
        (200, 250, 446, 563),
        (945, 995, 446, 563),
        (77, 207, 859, 912),
        (230, 359, 859, 912)
    ]

    while True:

        for user_input in pygame.event.get():

            if user_input.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the user hovers over the buttons

            mouse = pygame.mouse.get_pos()

            if bestie == 'car1':

                # if the user hovers over the right arrow
                if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_right.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_back.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_return.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

            elif bestie == 'car2':

                # if the user hovers over the left arrow
                if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_left.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the right arrow
                if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_right.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_back.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_return.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

            elif bestie == 'car3':

                # if the user hovers over the left arrow
                if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_left.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_back.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_return.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

            if lolly == 'car1':

                # if the user hovers over the right arrow
                if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked_right.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked_back.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked_return.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

            elif lolly == 'car2':

                # if the user hovers over the left arrow
                if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_left.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the right arrow
                if buttons_positions[1][0] <= mouse[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= mouse[1] <= buttons_positions[1][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_right.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_back.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked_return.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

            elif lolly == 'car3':

                # if the user hovers over the left arrow
                if buttons_positions[0][0] <= mouse[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= mouse[1] <= buttons_positions[0][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked_left.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the back button
                if buttons_positions[2][0] <= mouse[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= mouse[1] <= buttons_positions[2][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked_back.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

                # if the user hovers over the return button
                if buttons_positions[3][0] <= mouse[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= mouse[1] <= buttons_positions[3][3]:
                    bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked_return.png").convert_alpha()
                    screen.blit(bestie_customisation_image, (0, 0))
                    pygame.display.flip()

            # if the user clicks on the buttons

            if user_input.type == pygame.MOUSEBUTTONDOWN:

                if lolly == 'car1':  # the car1 screen will be blocked

                    if bestie == 'car2':  # if they click the left button, we'll display the blocked car1 screen, if they click the right button, we'll display the car3 screen, and car3 will be the new bestie car

                        if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:  # if the user clicks on the left arrow
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car1_blocked.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()

                        if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:  # if the user clicks on the right arrow
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car3.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()
                            bestie = 'car3'

                    elif bestie == 'car3':

                        # if the user clicks on the left arrow
                        if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()
                            bestie = 'car2'

                elif lolly == 'car2':  # the car2 screen will be blocked

                    if bestie == 'car1':

                        # if the user clicks on the right arrow
                        if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()

                    elif bestie == 'car3':

                        # if the user clicks on the left arrow
                        if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car2_blocked.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()

                elif lolly == 'car3':  # the car3 screen will be blocked

                    if bestie == 'car1':

                        # if the user clicks on the right arrow
                        if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car2.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()
                            bestie = 'car2'

                    elif bestie == 'car2':

                        # if the user clicks on the left arrow
                        if buttons_positions[0][0] <= user_input.pos[0] <= buttons_positions[0][1] and buttons_positions[0][2] <= user_input.pos[1] <= buttons_positions[0][3]:
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car1.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()
                            bestie = 'car1'

                        # if the user clicks on the right arrow
                        if buttons_positions[1][0] <= user_input.pos[0] <= buttons_positions[1][1] and buttons_positions[1][2] <= user_input.pos[1] <= buttons_positions[1][3]:
                            bestie_customisation_image = pygame.image.load("images/interface/select_character_car3_blocked.png").convert_alpha()
                            screen.blit(bestie_customisation_image, (0, 0))
                            pygame.display.flip()

                # if the user clicks on the back button
                if buttons_positions[2][0] <= user_input.pos[0] <= buttons_positions[2][1] and buttons_positions[2][2] <= user_input.pos[1] <= buttons_positions[2][3]:
                    start_screen()

                # if the user clicks on the return button
                if buttons_positions[3][0] <= user_input.pos[0] <= buttons_positions[3][1] and buttons_positions[3][2] <= user_input.pos[1] <= buttons_positions[3][3]:
                    multi_customisation_screen()
