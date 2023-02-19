import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


FPS = 50
pygame.init()
size = width, height = 1920, 1000

bug_sprite = pygame.sprite.Group()

display = pygame.display
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Навозники')
clock = pygame.time.Clock()

bug_image = load_image('bug.png')
tile_width = tile_height = 50


class Bug(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(bug_sprite)
        self.image = bug_image
        self.rect = self.image.get_rect().move(0, 0)
        self.pos = pos_x, pos_y

    def move(self, x, y):
        pass


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        if not (0 <= mouse_pos[0] - self.left <= self.width * self.cell_size and 0 <= mouse_pos[
            1] - self.top <= self.height * self.cell_size):
            return None
        i = mouse_pos[1] - self.top
        j = mouse_pos[0] - self.left
        i = i // self.cell_size
        j = j // self.cell_size
        return (j, i)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def terminate():
    pygame.quit()
    sys.exit()


'''def get_management_server() -> dict:
    """dict:
            ОЧЕРЕДЬ:
                    [Начало игры / не начало игры(bool: True - начало игры, False - еще ждем)]
            ИГРА:
                [[ПОложение врежеского жука X(int), ПОложение врежеского жука Y(int)], [ПОложение говна X(int), ПОложение говна Y(int)], Игра закончилась?(bool: False - играем, True - конец игры)]
    """
    # ОЧЕРЕДЬ return [True]
    # ИГРА return [[12, 123], [123, 123], False]
    pass


def send_data(game_data: dict[[int, int], [int, int]]):
    """game_data:
                [[ПОложение жука X(int), ПОложение жука Y(int)], [ПОложение говна X(int), ПОложение говна Y(int)]]"""
    pass
'''
# КОД ИГРЫ -->
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(pygame.Color(22, 74, 27))
    bug_sprite.draw(screen)
    display.flip()
