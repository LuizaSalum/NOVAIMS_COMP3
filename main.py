from interface import start_screen
from interface_small import start_screen_small
import pygame

def size_selection():

    pygame.init()

    size = (350, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lolly Locket's Dog Chase")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    pink = (217, 11, 141)
    screen.fill(pink)

    menu_size = pygame.image.load("images/interface/size.png").convert_alpha()
    hover_small = pygame.image.load("images/interface/size_small.png").convert_alpha()
    hover_normal = pygame.image.load("images/interface/size_big.png").convert_alpha()

    screen.blit(menu_size, (0, 0))
    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 67 < mouse[0] < 287 and 50 < mouse[1] < 110:
            screen.blit(hover_small, (0, 0))
            if click[0] == 1:
                pygame.quit()
                main(small=True)
        elif 43 < mouse[0] < 308 and 180 < mouse[1] < 239:
            screen.blit(hover_normal, (0, 0))
            if click[0] == 1:
                pygame.quit()
                main()
        else:
            screen.blit(menu_size, (0, 0))

        pygame.display.flip()

def main(small=False):

    if not small: # use the start screen from the normal interface
        start_screen(music_started=False)
    else: # use the start screen from the small interface
        start_screen_small(music_started=False)
        
if __name__ == "__main__":
    size_selection()