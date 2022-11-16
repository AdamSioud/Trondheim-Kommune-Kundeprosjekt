from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from server.model.src.map_manager import MapManager

app = Flask(__name__)
api = Api(app)
CORS(app)
MAP_MANAGER = MapManager()


class Map(Resource):
    """API call for getting the map with the scores for each zone"""
    def post(self):
        return MAP_MANAGER.generate_map(request.json).to_json()


class Score(Resource):
    """API call for getting the scores without the geometry column"""
    def post(self):
        return MAP_MANAGER.calculate_scores(request.json).to_json()


class ZoneData(Resource):
    """"API call for getting all the data for a single zone from its id,"""
    def get(self, zone_id):
        return MAP_MANAGER.get_zone_by_id(zone_id)


api.add_resource(Map, '/map')
api.add_resource(Score, '/score')
api.add_resource(ZoneData, '/zone/<int:zone_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
