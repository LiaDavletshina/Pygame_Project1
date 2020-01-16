import pygame
import random

pygame.init()

GREEN = pygame.Color('green')
DARK_GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
hsv = DARK_GREEN.hsva
DARK_GREEN.hsva = (hsv[0], hsv[1], hsv[2] - 10, hsv[3])
pygame.mixer.music.load('eat_sound.mp3')
SIZE = [800, 800]
game_window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")
BLUE = pygame.Color('blue')
SNAKE = [[11, 12], [11, 13]]
font = "14860.otf"
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
running = False


def text_format(message, textfont, textsize, textcolor):
    newfont = pygame.font.Font(textfont, textsize)
    newtext = newfont.render(message, 0, textcolor)
    return newtext


def draw_field():

    x = 0
    y = 0
    for i in range(25):
        for j in range(25):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(game_window, GREEN, (x, y, 32, 32), 0)
                else:
                    pygame.draw.rect(game_window, DARK_GREEN, (x, y, 32, 32), 0)
            else:
                if j % 2 == 0:
                    pygame.draw.rect(game_window, DARK_GREEN, (x, y, 32, 32), 0)
                else:
                    pygame.draw.rect(game_window, GREEN, (x, y, 32, 32), 0)
            x += 32
        x = 0
        y += 32


class Snake:
    global SNAKE

    def __init__(self):
        self.image = pygame.image.load('element.jpg').convert_alpha()

    def render(self):
        for i in SNAKE:
            game_window.blit(self.image, (i[0] * 32, i[1] * 32))

    def movement1(self):
        x = 2
        for i in reversed(SNAKE[1:]):
            i[0], i[1] = SNAKE[len(SNAKE) - x][0], SNAKE[len(SNAKE) - x][1]
            x += 1

    def movement2(self):
        global direction
        global direction1
        if direction == 'left':
            snake.movement1()
            SNAKE[0][0] -= 1
            direction1 = 'left'
        if direction == 'right':
            snake.movement1()
            SNAKE[0][0] += 1
            direction1 = 'right'
        if direction == 'up':
            snake.movement1()
            SNAKE[0][1] -= 1
            direction1 = 'up'
        if direction == 'down':
            snake.movement1()
            SNAKE[0][1] += 1
            direction1 = 'down'


class Apple:
    def __init__(self):
        self.x = random.randint(0, 24)
        self.y = random.randint(0, 24)
        self.image = pygame.image.load('apple.jpg').convert_alpha()

    def generation(self):
        while [self.x, self.y] in SNAKE:
            self.x = random.randint(0, 24)
            self.y = random.randint(0, 24)
        return [self.x, self.y]

    def render(self):
        game_window.blit(self.image, (self.x * 32, self.y * 32))


snake = Snake()
apple = Apple()
direction = ''
direction1 = ''
menu = True
selected = "start"

while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected = "start"
            elif event.key == pygame.K_DOWN:
                selected = "quit"
            if event.key == pygame.K_RETURN:
                if selected == "start":
                    running = True
                    menu = False
                    print('start')
                if selected == "quit":
                    pygame.quit()
                    quit()
    game_window.fill(DARK_GREEN)
    title = text_format("Snake", font, 90, YELLOW)
    if selected == "start":
        text_start = text_format("START", font, 50, WHITE)
    else:
        text_start = text_format("START", font, 50, BLACK)
    if selected == "quit":
        text_quit = text_format("QUIT", font, 50, WHITE)
    else:
        text_quit = text_format("QUIT", font, 50, BLACK)

    title_rect = title.get_rect()
    start_rect = text_start.get_rect()
    quit_rect = text_quit.get_rect()

    # Main Menu Text
    game_window.blit(title, (SIZE[0] / 2 - (title_rect[2] / 2), 80))
    game_window.blit(text_start, (SIZE[0] / 2 - (start_rect[2] / 2), 300))
    game_window.blit(text_quit, (SIZE[0] / 2 - (quit_rect[2] / 2), 360))
    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if direction1 != 'right':
                    direction = 'left'
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if direction1 != 'left':
                    direction = 'right'
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if direction1 != 'down':
                    direction = 'up'
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if direction1 != 'up':
                    direction = 'down'
    apple_coord = apple.generation()
    snake.movement2()
    if SNAKE[0] == apple_coord:
        SNAKE.append([SNAKE[len(SNAKE) - 1][0], SNAKE[len(SNAKE) - 1][1]])
        pygame.mixer.music.play()
        pygame.mixer.music.play()
    draw_field()
    apple.render()
    snake.render()
    pygame.display.flip()
    pygame.time.delay(150)
