from flask import Flask
from flask import request, jsonify
from logic import do
from classes.User import User

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        # так остаем QueryParam
        return do(request.args['name'])
    return 'Hello World!'


# так остаем pathParam
@app.route('/<name>', methods=['GET', 'POST'])
def hello_world2(name):
    if request.method == 'GET':
        return do(name)
    if request.method == 'POST':
        data = request.get_json() or {}
        user = User()
        user.from_dict(data)
        user.name = do(user.name)
        response = jsonify(user.to_dict())
        return response
        # return do(request.json['name'])
    return 'Hello World!'

# request.form - тело запроса в пост


if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0")
