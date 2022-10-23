from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from server.model.src.models import Model

# from model.models import Classes


app = Flask(__name__)
api = Api(app)
CORS(app)

class Map(Resource):
    def post(self):
        # Run function in service
        # res = main(param_input)
        # return main(param_input)
        print(request.json)
        model = Model()
        return model.generate_map(request.json)




""" This should take in an ID which is the levekår sone """

class ZoneData(Resource):
    def get(self):
        return {'Ila': 'Here is all the data'}


api.add_resource(Map, '/Map')

api.add_resource(ZoneData, '/ZoneData')


if __name__ == '__main__':
    app.run(debug=True)
