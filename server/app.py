from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from server.model.src.models import Model

app = Flask(__name__)
api = Api(app)
CORS(app)
MODEL = Model()


class Map(Resource):
    """API call for getting the map with the scores for each zone"""
    def post(self):
        result = MODEL.generate_map(request.json)
        global_properties = {
            "scoreMin": result['score'].min(),
            "scoreMax": result['score'].max()
        }
        result = {
            "geoJSONGlobalProperties": global_properties,
            "geoJSON": result.to_json()
        }
        return result


class Score(Resource):
    """API call for getting the scores without the geometry column"""
    def post(self):
        result = MODEL.calculate_scores(request.json)
        global_properties = {
            "scoreMin": result['score'].min(),
            "scoreMax": result['score'].max()
        }
        # new_max = global_properties.get("scoreMax") - global_properties.get("scoreMin")
        # for i, row in result.iterrows():
        #     result.at[i, 'score'] = (result['score'][i] - global_properties.get("scoreMin")) * 100 / new_max
        return result.to_json()


class ZoneData(Resource):
    """"API call for getting all the data for a single zone from its id,"""
    def get(self, zone_id):
        return MODEL.get_zone_by_id(zone_id)


api.add_resource(Map, '/map')
api.add_resource(Score, '/score')
api.add_resource(ZoneData, '/zone/<int:zone_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
