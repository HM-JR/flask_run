from flask import Flask,make_response,render_template
from flask_restful import Api,Resource
from flask_cors import CORS,cross_origin
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
connect = Api(app)


class index(Resource):
    def get(self):

        return make_response(render_template('index.html'))


class return_json(Resource):
    @cross_origin(origin='*',headers=['Content-Type','Authorization'])
    def get(self):
        list_r=['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg']
        data ={'data':list_r,'code':200}
        return json.dumps(data)

connect.add_resource(index,'/')
connect.add_resource(return_json,'/h/info')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)