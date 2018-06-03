import pygame

# Initialize Pygame.
pygame.init()
# Set size of pygame window.
screen = pygame.display.set_mode((640, 480))
# Create empty pygame surface.
background = pygame.Surface(screen.get_size())
# Fill the background white color.
background.fill((0, 0, 0))
# Convert Surface object to make blitting faster.
background = background.convert()
# Copy background to screen (position (0, 0) is upper left corner).
screen.blit(background, (0, 0))
# Create Pygame clock object.
clock = pygame.time.Clock()

mainloop = True
# Desired framerate in frames per second. Try out other values.
FPS = 30
# How many seconds the "game" is played.
playtime = 0.0

font = pygame.font.SysFont("Arial", 30)
label = font.render("hello World", 1, (255, 255, 0))

background = []
for y in range(screen.get_height()):
    background.append([50, 70, 120, 130])

while mainloop:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0

    screen.blit(label, (100, 100))

    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                mainloop = False

    for i in range(len(background)):
        pygame.draw.line(screen, pygame.Color(0, 255, 0, 255), [0, i], [background[i][0]-1, i])
        pygame.draw.line(screen, pygame.Color(255, 255, 0, 255), [background[i][0], i], [background[i][1]-1, i])
        pygame.draw.line(screen, pygame.Color(0, 0, 0, 255), [background[i][1], i], [background[i][2]-1, i])
        pygame.draw.line(screen, pygame.Color(255, 255, 0, 255), [background[i][2], i], [background[i][3]-1, i])
        pygame.draw.line(screen, pygame.Color(0, 255, 0, 255), [background[i][3], i], [screen.get_width(), i])
        background[i][0]
        background[i][0]

    # Print framerate and playtime in titlebar.
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)

    # Update Pygame display.
    pygame.display.flip()

# Finish Pygame.
pygame.quit()

# At the very last:
print("This game was played for {0:.2f} seconds".format(playtime))
