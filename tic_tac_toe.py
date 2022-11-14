import pygame
import os

# Font Engine Initialization for adding text
pygame.font.init()

# Constants for fps and window
FPS = 60
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe by BR")

# Rectangles for borders
V_BORDER1 = pygame.Rect(WIDTH / 3, 0, 5, HEIGHT)
V_BORDER2 = pygame.Rect(WIDTH // 1.5, 0, 5, HEIGHT)
H_BORDER1 = pygame.Rect(0, HEIGHT / 3, WIDTH, 5)
H_BORDER2 = pygame.Rect(0, HEIGHT / 1.5, WIDTH, 5)

# Initialization for result font
RESULT_FONT = pygame.font.SysFont("comicsans", 60)

# Creating RGB tuples for different Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set of tuples that are the wining condition 3 Horizontals, 3 Verticals and 2 Diagnoals
WINING_SET = {
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
}

# Loading the X and O image
CIRCLE_IMAGE = pygame.image.load(os.path.join('Assets', 'circle.png'))
CIRCLE = pygame.transform.scale(CIRCLE_IMAGE, (120, 120))

O_WIN_IMAGE = pygame.image.load(os.path.join('Assets', 'o_win.jpg'))
O_WIN = pygame.transform.scale(O_WIN_IMAGE, (WIDTH, HEIGHT))

X_IMAGE = pygame.image.load(os.path.join('Assets', 'x.png'))
X = pygame.transform.scale(X_IMAGE, (120, 120))

X_WIN_IMAGE = pygame.image.load(os.path.join('Assets', 'x_win.jpg'))
X_WIN = pygame.transform.scale(X_WIN_IMAGE, (WIDTH, HEIGHT))

# Decalaring list rectangles, total 9 rectangles for 9 playable slots
playable_rect = [
    [
        pygame.Rect(20, 20, WIDTH / 3, HEIGHT / 3),
        pygame.Rect(WIDTH / 3 + 20, 20, WIDTH / 1.5 - 200, HEIGHT / 3 - 50),
        pygame.Rect(WIDTH / 1.5 + 20, 20, WIDTH, HEIGHT / 3),
    ],
    [
        pygame.Rect(20, HEIGHT / 3 + 20, WIDTH / 3, HEIGHT / 3),
        pygame.Rect(
            WIDTH / 3 + 20, HEIGHT / 3 + 20, WIDTH / 1.5 - 200, HEIGHT / 3 - 50
        ),
        pygame.Rect(WIDTH / 1.5 + 20, HEIGHT / 3 + 20, WIDTH, HEIGHT / 3),
    ],
    [
        pygame.Rect(20, HEIGHT / 1.5 + 20, WIDTH / 3, HEIGHT / 3),
        pygame.Rect(WIDTH / 3 + 20, HEIGHT / 1.5 + 20, WIDTH / 1.5 - 200, HEIGHT / 3),
        pygame.Rect(WIDTH / 1.5 + 20, HEIGHT / 1.5 + 20, WIDTH / 1.5, HEIGHT / 3),
    ]
]

# drawing function to draw basic borders
def draw():
    pygame.draw.rect(WIN, WHITE, V_BORDER1)
    pygame.draw.rect(WIN, WHITE, V_BORDER2)
    pygame.draw.rect(WIN, WHITE, H_BORDER1)
    pygame.draw.rect(WIN, WHITE, H_BORDER2)
    pygame.display.update()


# drawing O when O players plays his move in the correct rectaangle
def draw_circle(pos, i, j, O_PLAYER):
    WIN.blit(CIRCLE, playable_rect[i][j])

    # adding the value of the rectangle(1-9) on which O is drawn to O set
    if i == 0:
        O_PLAYER.add(i + j + 1)
    if i == 1:
        O_PLAYER.add(i + j + 3)
    if i == 2:
        O_PLAYER.add(i + j + 5)
    pygame.display.update()


# drawing X when its X player turn
def draw_x(pos, i, j, X_PLAYER):
    WIN.blit(X, playable_rect[i][j])

    # adding the value of the rectangle(1-9) on which X is drawn to X set
    if i == 0:
        X_PLAYER.add(i + j + 1)
    if i == 1:
        X_PLAYER.add(i + j + 3)
    if i == 2:
        X_PLAYER.add(i + j + 5)
    pygame.display.update()


# main function
def main():
    clock = pygame.time.Clock()  # clock to limit the fps
    run = True  # variable to run infinite loop
    choice = True  # True mean - X turn else O turn
    X_PLAYER = set()  # 2 empty sets for both X and O player
    O_PLAYER = set()
    WIN.fill(BLACK)  # filling the screen black
    pygame.display.update()

    # empty list of rectangle to add the rectangles already use
    already_done_rect = []
    # variable to check if someone won
    won = False  # false - no win keep checking for draw

    # Infinite game loop
    while run:
        clock.tick(FPS)  # setting max fps

        # Loop to get all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                return

        # Getting mouse key pressed and mouse positions
        keys_pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        for i in range(3):
            for j in range(3):
                if keys_pressed[0] and playable_rect[i][j].collidepoint(pos):

                    if playable_rect[i][j] in already_done_rect:
                        break
                    else:
                        already_done_rect.append(playable_rect[i][j])

                    if choice:
                        draw_circle(pos, i, j, O_PLAYER)
                        choice = False
                    else:
                        draw_x(pos, i, j, X_PLAYER)
                        choice = True
                else:
                    draw()

        # Checking for O win
        for tup in WINING_SET:
            sum = 0
            for i in range(3):
                if tup[i] in O_PLAYER:
                    sum += 1
                if sum == 3:
                    # text = RESULT_FONT.render("O WON", 1, RED)
                    # WIN.blit(text, (WIDTH / 2, HEIGHT / 2))
                    # pygame.display.update()
                    pygame.time.delay(500)
                    WIN.blit(O_WIN, (0, 0))
                    pygame.display.update()
                    run = False
                    won = True

        # Checking for X win
        for tup in WINING_SET:
            sum = 0
            for i in range(3):
                if tup[i] in X_PLAYER:
                    sum += 1
                if sum == 3:
                    # text = RESULT_FONT.render("X WON", 1, RED)
                    # WIN.blit(text, (WIDTH / 2, HEIGHT / 2))
                    # pygame.display.update()
                    pygame.time.delay(500)
                    WIN.blit(X_WIN, (0, 0))
                    pygame.display.update()
                    run = False
                    won = True
                
        # Checking for draw
        if not won:
            if len(already_done_rect) == 9:
                text = RESULT_FONT.render("DRAW", 1, RED)
                # pygame.time.delay(500)
                WIN.blit(text, (WIDTH / 2, HEIGHT / 2))
                pygame.display.update()
                run = False

    # After match is finished displaying result and waiting for 1 sec before restarting the game
    pygame.time.delay(1000)
    main()


if __name__ == "__main__":
    main()
