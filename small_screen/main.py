import pygame
from interface import start_screen
from game import multi_game, game_over


def main():

    pygame.init()
    screen = pygame.display.set_mode((1250*0.85, 950*0.85))
    running = True
    game_running = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if not game_running:
            start_screen()
            if keys[pygame.K_RETURN]:
                game_running = True
                multi_game()
            elif keys[pygame.K_ESCAPE]:
                running = False  # Quit the game
        else:
            game_over_choice = game_over()
            if game_over_choice == "restart":
                game_running = True
                multi_game()
            elif game_over_choice == "back_to_start":
                game_running = False

    pygame.quit()

if __name__ == "__main__":
    main()