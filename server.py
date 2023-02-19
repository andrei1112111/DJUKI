from flask import Flask, jsonify, request

app = Flask(__name__)

game_data = {'ball': [1920 // 2, 1080 // 2], 'juck1': [100, 100, 0], 'juck2': [1920 - 100, 1080 - 100, 180]}
ochered = 0


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
            return jsonify({"game": True, "you": "juck2"})
        elif ochered == 0:
            ochered += 1
            return jsonify({"game": False, "you": "juck1"})


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
    return jsonify({"all": 'ok'})


app.run(debug=True)
