# gameboard class
import pygame


class Gameboard:
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    AQUA = (24,116,205)

    pygame.init()

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
    subtitle = pygame.font.SysFont('Roboto', 50)
    font = pygame.font.SysFont('Roboto', 36)

    display_instructions = True
    instruction_page = 1

    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1
                if instruction_page == 3:
                    display_instructions = False

        # Set the screen background
        screen.fill(AQUA)

        if instruction_page == 1:
            # Draw instructions, page 1
            # This could also load an image created in another program.
            # That could be both easier and more flexible.

            text = title_font.render("Welcome to Connect 4", True, WHITE)
            screen.blit(text, [130, 280])

            text = font.render("(Click to Continue)", True, WHITE)
            screen.blit(text, [395, 380])

        if instruction_page == 2:
            # Draw instructions, page 2
            text = subtitle.render("Goal of the Game:", True, WHITE)
            screen.blit(text, [10, 10])

            text = font.render("The goal of Connect 4 is to get 4 discs in a row before your opponent", True, WHITE)
            screen.blit(text, [10, 60])

            text = subtitle.render("Instructions:", True, WHITE)
            screen.blit(text, [10, 110])

            text = font.render('1. Each player alternates droppings discs into the gameboard until ', True, WHITE)
            screen.blit(text, [10, 150])

            text = font.render('    one player gets 4 in a row or someone runs out of discs', True, WHITE)
            screen.blit(text, [10, 180])

            text = font.render("2. You can win by getting 4 in a row horizontally, vertically, or diagonally", True,
                               WHITE)
            screen.blit(text, [10, 220])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


        # Set the screen background
        screen.fill(WHITE)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()