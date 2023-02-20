try:
    import requests
    import pygame
    import sys

    pygame.init()
    s = input("--> ")
    if s:
        server_path = s
    else:
        server_path = "http://127.0.0.1:5000"

    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Навозники')
    clock = pygame.time.Clock()
    FPS = 50

    all_sprites = pygame.sprite.Group()


    def get_management_server(current=''):
        """get_management_server('ochered') ---> {'game': True}"""
        """get_management_server() ---> {'govno': [13, 13], 'juck1': [12, 113], 'juck2': [122, 113]}"""
        if current == 'ochered':
            return requests.get(f'{server_path}/och/').json()
        else:
            return requests.get(f'{server_path}').json()


    def send_data(game_data, current=''):
        """send_data({}, 'ochered') ---> {'game': False, 'you': 'juck1'}  ||  {'game': True}"""
        """send_data({'name': 'juck1', 'my': [12, 113], 'govno': [13, 13]}) ---> {'all': 'ok'}"""
        if current == 'ochered':
            return requests.post(f'{server_path}/och/', json=game_data).json()
        elif current == 'end':
            return requests.post(f'{server_path}/end/').json()
        else:
            return requests.post(f'{server_path}', json=game_data).json()
        pass

    class Bug(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, angle, name):
            pygame.sprite.Sprite.__init__(self)
            self.image = bug_image
            self.rect = self.image.get_rect()
            self.rect.center = (pos_x, pos_y)
            self.angle = angle
            self.rotate(angle)
            self.name = name

        def rotate(self, a):
            self.image = pygame.transform.rotate(self.image, a)

        def update(self, data):
            self.rect.center = data[self.name][:2]
            self.rotate(data[self.name][-2] - self.angle)
            self.angle = data[self.name][-2]


    class Ball(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, k):
            pygame.sprite.Sprite.__init__(self)
            self.image = ball_image
            self.rect = self.image.get_rect()
            self.rect.center = (pos_x, pos_y)
            self.k = k

        def update(self, data):
            self.rect.center = data['ball'][:2]

        def generation(self):
            self.k += 1
            x, y = self.rect.center
            self.image = pygame.transform.scale(ball_image, (100 + self.k // 10, 100 + self.k // 10))
            self.rect = self.image.get_rect()
            self.rect.center = x, y

    class Mocha(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y, k):
            pygame.sprite.Sprite.__init__(self)
            self.image = ball_image
            self.rect = self.image.get_rect()
            self.rect.center = (pos_x, pos_y)
            self.k = k

        def update(self, data):
            self.rect.center = data['ball'][:2]

        def generation(self):
            self.k += 1
            x, y = self.rect.center
            self.image = pygame.transform.scale(ball_image, (100 + self.k // 10, 100 + self.k // 10))
            self.rect = self.image.get_rect()
            self.rect.center = x, y

    def terminate():
        send_data('', 'end')
        pygame.quit()
        sys.exit()


    def end_window(n):
        while True:
            clock.tick(FPS)
            screen.fill((43, 43, 43))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
            if n == 'win':
                screen.blit(win, (0, 0))
            else:
                screen.blit(lose, (0, 0))
            pygame.display.flip()


    bug_image = pygame.image.load('data/bug.png').convert()
    bug_image.set_colorkey((255, 255, 255))
    bug_image = pygame.transform.scale(bug_image, (100, 70))

    ball_image = pygame.image.load('data/ball.png').convert()
    ball_image.set_colorkey((255, 255, 255))
    ball_image = pygame.transform.scale(ball_image, (100, 100))

    menu_image = pygame.image.load('data/menu.png').convert()
    menu_image.set_colorkey((255, 255, 255))
    menu_image = pygame.transform.scale(menu_image, (1920, 1080))

    back = pygame.image.load('data/back.png').convert()
    back.set_colorkey((255, 255, 255))
    back = pygame.transform.scale(back, (1920, 1080))

    back1 = pygame.image.load('data/back1.png').convert()
    back1.set_colorkey((255, 255, 255))
    back1 = pygame.transform.scale(back1, (1920, 1080))

    back2 = pygame.image.load('data/back2.png').convert()
    back2.set_colorkey((255, 255, 255))
    back2 = pygame.transform.scale(back2, (1920, 1080))

    win = pygame.image.load('data/win.png').convert()
    win.set_colorkey((255, 255, 255))
    win = pygame.transform.scale(win, (1920, 1080))

    lose = pygame.image.load('data/lose.png').convert()
    lose.set_colorkey((255, 255, 255))
    lose = pygame.transform.scale(lose, (1920, 1080))

    mocha = pygame.image.load('data/mocha.png').convert()
    mocha.set_colorkey((255, 255, 255))
    mocha = pygame.transform.scale(mocha, (50, 50))

    # НАЧАЛО ИГРЫ ---->

    data = send_data({}, 'ochered')  # {'game': False, 'you': 'juck1'}
    my_name = data['you']
    print(my_name)
    k = 0
    if not data['game']:
        while True:
            clock.tick(FPS)
            screen.fill((43, 43, 43))
            k += 1
            if k >= 55:
                k = 0
                if get_management_server('ochered')['game']:  # {'game': True}
                    break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
            screen.blit(menu_image, (0, 0))
            pygame.display.flip()

    juck1 = Bug(100, 100, 0, 'juck1')
    juck2 = Bug(1920 - 100, 1080 - 100, 180, 'juck2')
    ball = Ball(1920 // 2, 1080 // 2, 1)

    all_sprites.add(juck1)
    all_sprites.add(juck2)
    all_sprites.add(ball)

    data = get_management_server()

    while True:
        clock.tick(FPS)
        screen.fill((33, 33, 33))
        if my_name == 'juck1':
            screen.blit(back, (0, 0))
        else:
            screen.blit(back2, (0, 0))
        # screen.blit(back1, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            data[my_name][0] -= data[my_name][-1]
            data[my_name][-2] = 0
            if juck1.rect.colliderect(juck2.rect):
                data[my_name][0] += data[my_name][-1] + 1
        if keys[pygame.K_w]:
            data[my_name][1] -= data[my_name][-1]
            data[my_name][-2] = 270
            if juck1.rect.colliderect(juck2.rect):
                data[my_name][1] += data[my_name][-1] + 1
        if keys[pygame.K_d]:
            data[my_name][0] += data[my_name][-1]
            data[my_name][-2] = 180
            if juck1.rect.colliderect(juck2.rect):
                data[my_name][0] -= data[my_name][-1] - 1
        if keys[pygame.K_s]:
            data[my_name][1] += data[my_name][-1]
            data[my_name][-2] = 90
            if juck1.rect.colliderect(juck2.rect):
                data[my_name][1] -= data[my_name][-1] - 1

        if data[my_name][0] <= 0:
            data[my_name][0] += 3
        if data[my_name][1] <= 0:
            data[my_name][1] += 3
        if data[my_name][0] >= 1920:
            data[my_name][0] -= 3
        if data[my_name][1] >= 1080:
            data[my_name][1] -= 3
        if data['ball'][0] <= 0:
            data['ball'][0] += 3
        if data['ball'][1] <= 0:
            data['ball'][1] += 3
        if data['ball'][0] >= 1920:
            data['ball'][0] -= 3
        if data['ball'][1] >= 1080:
            data['ball'][1] -= 3

        send_data({'name': my_name, 'my': data[my_name], 'ball': data['ball']})
        data = get_management_server()
        if data['och'] == 0:
            terminate()

        if juck1.rect.colliderect(ball.rect):
            ball.generation()
            data['juck1'][-1] = 2
            if data['juck1'][0] <= data['ball'][0]:
                data['ball'][0] += data['juck1'][-1]
            if data['juck1'][1] <= data['ball'][1]:
                data['ball'][1] += data['juck1'][-1]
            if data['juck1'][0] > data['ball'][0]:
                data['ball'][0] -= data['juck1'][-1]
            if data['juck1'][1] > data['ball'][1]:
                data['ball'][1] -= data['juck1'][-1]
        else:
            data['juck1'][-1] = 3
        if juck2.rect.colliderect(ball.rect):
            ball.generation()
            data['juck2'][-1] = 2
            if data['juck2'][0] <= data['ball'][0]:
                data['ball'][0] += data['juck2'][-1]
            if data['juck2'][1] <= data['ball'][1]:
                data['ball'][1] += data['juck2'][-1]
            if data['juck2'][0] > data['ball'][0]:
                data['ball'][0] -= data['juck2'][-1]
            if data['juck2'][1] > data['ball'][1]:
                data['ball'][1] -= data['juck2'][-1]
        else:
            data['juck2'][-1] = 3

        if my_name == 'juck1':
            if data['ball'][0] <= 0:
                end_window('lose')
            if data['ball'][0] >= 1920:
                end_window('win')
        if my_name == 'juck2':
            if data['ball'][0] <= 0:
                end_window('win')
            if data['ball'][0] >= 1920:
                end_window('lose')

        all_sprites.update(data)

        all_sprites.draw(screen)
        pygame.display.flip()
except Exception as ex:
    with open('1.txt', 'w+') as f:
        f.write(str(ex))
