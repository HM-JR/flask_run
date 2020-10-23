from flask import Flask,make_response,render_template
from flask_restful import Api,Resource



app = Flask(__name__)
connect = Api(app)


class index(Resource):
    def get(self):

        return make_response(render_template('index.html'))

connect.add_resource(index,'/')


if __name__ == '__main__':
    app.run()