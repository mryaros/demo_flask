from flask import Flask
from flask import request
from logic import do

app = Flask(__name__)
api = Api(app=app, doc='/docs', version='1.0.0-oas3', title='TEST APP API',
          description='TEST APP API')


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
    return 'Hello World!'

# request.form - тело запроса в пост


if __name__ == '__main__':
    app.run()
