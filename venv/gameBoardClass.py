# gameboard class
import pygame
from main import Main


class Gameboard:
    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 50, 64)
    AQUA = (24, 116, 205)
    GRAY = (217, 217, 217)
    YELLOW = (255, 255, 0)
    WIDTH, HEIGHT = 1000, 700
    ROWS, COLS = 6, 7
    SQUARE_SIZE = 106

    pygame.init()
    main = Main()

    # Set the height and width of the screen
    size = [1000, 700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Welcome to Connect 4")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # This is a font we use to draw text on the screen (size 36)
    title_font = pygame.font.SysFont('Roboto', 100)
    subtitle = pygame.font.SysFont('Roboto', 74)
    font = pygame.font.SysFont('Roboto', 45)

    display_instructions = True
    instruction_page = 1

    # create a surface object for the Connect4 logo, image is drawn on it
    logo = pygame.image.load("/Users/sammacbookpro/PycharmProjects/Adv-python/Connect4/venv/Connect4copy.png").convert()

    pygame.mixer.music.load("pygamemusic.mp3")
    pygame.mixer.music.play(-1)

    # -------- Instruction Page Loop -----------
    while not done and display_instructions: # while the game isn't done and the instructions isnt done
        for event in pygame.event.get(): # records the events to detect clicks
            if event.type == pygame.QUIT: # if the game is quit
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is clicked
                instruction_page += 1
                if instruction_page == 3: # if we are on the final instruction page
                    display_instructions = False

        # Set the screen background
        screen.fill(BLACK)

        if instruction_page == 1:
            # Draw instructions, page 1
            # This could also load an image created in another program.
            # That could be both easier and more flexible.

            text = title_font.render("Welcome to", True, RED)
            screen.blit(text, [300, 165])
            screen.blit(logo, (115, 225))

            text = font.render("(Click Screen to Continue)", True, RED)
            screen.blit(text, [300, 465])

        if instruction_page == 2:
            # Draw instructions, page 2
            text = subtitle.render("Goal of the Game:", True, RED)
            screen.blit(text, [10, 10])

            text = font.render("The goal of Connect 4 is to get 4 discs in a row before", True, WHITE)
            screen.blit(text, [10, 65])

            text = font.render("your opponent", True, WHITE)
            screen.blit(text, [10, 90])

            text = subtitle.render("Instructions:", True, RED)
            screen.blit(text, [10, 180])

            text = font.render('1. Each player alternates droppings discs into the gameboard until ', True, WHITE)
            screen.blit(text, [10, 230])

            text = font.render('    one player gets 4 in a row', True, WHITE)
            screen.blit(text, [10, 270])

            text = font.render("2. You can win by getting 4 in a row horizontally, vertically,", True,
                               WHITE)
            screen.blit(text, [10, 315])

            text = font.render("    or diagonally", True,
                               WHITE)
            screen.blit(text, [10, 343])

            text = font.render("3. Once it is your turn, click the button at the bottom of the column", True,
                               WHITE)
            screen.blit(text, [10, 384])

            text = font.render("    you would like to play in", True, WHITE)
            screen.blit(text, [10, 415])

            text = font.render("4. If you would like to quit the game use the corresponding ", True,
                               WHITE)
            screen.blit(text, [10, 470])

            text = font.render("    button on the left", True, WHITE)
            screen.blit(text, [10, 507])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()



    # -------- Main Program Loop -----------
    while not done: # while the game is not finished
        for event in pygame.event.get():  # records the events that occur
            PL = main.main()
            screen.fill(BLACK)
            text = subtitle.render("Player " + str(PL) + " Wins!", True, RED)
            screen.blit(text, [340, 300])
            if event.type == pygame.QUIT: # if the game is quit
                done = True
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
