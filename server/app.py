import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from server.model.src.models import Model

# from model.models import Classes


app = Flask(__name__)
api = Api(app)
CORS(app)

MODEL = Model()

class Map(Resource):

    def post(self):
        # Run function in service
        # res = main(param_input)
        # return main(param_input)

        # model = Model()
        # result = model.generate_map(request.json)
        result = MODEL.generate_map(request.json)

        global_properties = {
            "scoreMin": result['Score'].min(),
            "scoreMax": result['Score'].max()
        }

        result = {
            "geoJSONGlobalProperties": global_properties,
            "geoJSON": result.to_json()
        }
        return result

class Score(Resource):
    def post(self):
        result = MODEL.calculate_scores(request.json)
        global_properties = {
            "scoreMin": result['Score'].min(),
            "scoreMax": result['Score'].max()
        }
        new_max = global_properties.get("scoreMax") - global_properties.get("scoreMin")
        for i, row in result.iterrows():
            print(i, result['Score'][i], (result['Score'][i] - global_properties.get("scoreMin")) * 100 / new_max)
            result.at[i, 'Score'] = (result['Score'][i] - global_properties.get("scoreMin")) * 100 / new_max
        return result.to_json()


""" This should take in an ID which is the levekår sone """
class ZoneData(Resource):
    def get(self, zone_id):
        return MODEL.get_zone_by_id(zone_id)


api.add_resource(Map, '/map')
api.add_resource(Score, '/score')
api.add_resource(ZoneData, '/zone/<int:zone_id>')



if __name__ == '__main__':
    app.run(debug=True, port=5001)
