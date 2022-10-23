import json

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
        model = Model()
        result = model.generate_map(request.json)
        global_properties = {
            "scoreMin": result['Score'].min(),
            "scoreMax": result['Score'].max()
        }
        result = {
            "geoJSONGlobalProperties": global_properties,
            "geoJSON": result.to_json(),
            "request": request.json
        }
        return result




""" This should take in an ID which is the levekår sone """

class ZoneData(Resource):
    def get(self):
        return {'Ila': 'Here is all the data'}


api.add_resource(Map, '/Map')

api.add_resource(ZoneData, '/ZoneData')


if __name__ == '__main__':
    app.run(debug=True)
