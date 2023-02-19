import requests

server_path = "http://127.0.0.1:5000"


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
    else:
        return requests.post(f'{server_path}', json=game_data).json()
    pass


# КОД ИГРЫ -->

while True:
    exec(f"print({input('-> ')})")
