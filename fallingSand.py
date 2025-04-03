import pygame 


def pygame_init():
    """ initilize the pygame window """
    # Colours for pygame
    WHITE = (255, 255, 255)
    WHITE_TRANSPARENT = (255, 255, 255, 90)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    pygame.init()
    screen_size = (1200, 800)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Sand Gravity Simulation")

    # CLock for FPS
    clock = pygame.time.Clock()

    # Grid 
    cell_size = 10
    grid_width = screen_size[0] // cell_size
    grid_height = screen_size[1] // cell_size

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for row in range(grid_height):
            for col in range(grid_width):
                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, WHITE_TRANSPARENT, rect, 1)

        # Updates Screen to make changes visible
        pygame.display.flip()

        # FPS
        clock.tick(60)



def new_grid():
    """ resets the simulation state """
    pass


def main():
    """ main function"""
    pygame_init()

    class Sand():

        def __init__(self):
            self.x = None
            self.y = None

main()