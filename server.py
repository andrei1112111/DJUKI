from flask import Flask, jsonify, request

app = Flask(__name__)

ochered = 0
game_data = {'ball': [1920 // 2, 1080 // 2, 1], 'juck1': [100, 100, 0, 2], 'juck2': [1920 - 100, 1080 - 100, 180, 2],
             'och': ochered, 'mocha': []}


@app.route('/och/', methods=['GET', 'POST'])
def och():
    global ochered
    global game_data
    if request.method == 'GET':
        if ochered == 2:
            return jsonify({"game": True})
        else:
            return jsonify({"game": False})
    elif request.method == 'POST':
        if ochered == 1:
            ochered += 1
            game_data['och'] = ochered
            return jsonify({"game": True, "you": "juck2"})
        elif ochered == 0:
            ochered += 1
            game_data['och'] = ochered
            return jsonify({"game": False, "you": "juck1"})


@app.route('/end/', methods=['POST'])
def end():
    global ochered
    global game_data
    ochered = 0
    game_data = {'ball': [1920 // 2, 1080 // 2, 1], 'juck1': [100, 100, 0, 2],
                 'juck2': [1920 - 100, 1080 - 100, 180, 2], 'och': ochered, 'win': ''}
    return jsonify({'all': 'ok'})


@app.route('/', methods=['GET', 'POST'])
def index():
    global game_data
    if request.method == 'GET':
        return jsonify(game_data)
    elif request.method == 'POST':
        data = request.json
        game_data[data["name"]] = data["my"]
        if data["name"] == 'juck1':
            game_data["ball"] = data["ball"]
        game_data['mocha'] = data['mocha']
    return jsonify({"all": 'ok'})


app.run(debug=True, host='127.0.0.1', port=5000)
