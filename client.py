def get_management_server() -> dict:
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

# КОД ИГРЫ -->
