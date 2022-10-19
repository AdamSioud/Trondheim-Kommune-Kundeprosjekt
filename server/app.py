from flask import Flask
from flask_restful import Resource, Api
# from model.models import Classes


app = Flask(__name__)
api = Api(app)


"""

Inputs

param_input = {
    "age_input": {
        "selected": ['underage (0-17)', 'young adult (18-34)'],
        "percent": 0.5
    },
    "price_input": {
        "selected": ['small', "medium"],
        "budget": 2400000
    },
    "distance_input": {
        "posistion": Point (10.39628304564158, 63.433247153410214)
    },
    "well_being_input": {
        "weight": 4
    },
    "safety_input": {
        "weight": 4
    },
    "culture_input": {
        "weight": 4
    },
    "outdoor_input": {
        "weight": 4
    },
    "transport_input": {
        "weight": 4
    },
    "walkway_input": {
        "weight": 4
    },
    "noise_traffic_input": {
        "weight": 4
    },
    "noise_other_input": {
        "weight": 4
    },
    "grocery_input": {
        "weight": 4
    }
}
"""
class Map(Resource):
    def get(self):
        # Run function in service
        # res = main(param_input)
        # return main(param_input)
        return {'Map': 'This is our map'}




""" This should take in an ID which is the levekår sone
class ZoneData(Resource):
    def get(self):
        return {'Ila': 'Here is all the data'}
"""

api.add_resource(Map, '/')

# api.add_resource(ZoneData, '/')


if __name__ == '__main__':
    app.run(debug=True)