from flask import Flask
from flask_restful import Resource, Api
# from model.models import Classes


app = Flask(__name__)
api = Api(app)



class Map(Resource):
    def get(self):
        # Run function in service
        # res = main(param_input)
        # return main(param_input)
        return {'Map': 'This is our map'}




""" This should take in an ID which is the levekår sone """

class ZoneData(Resource):
    def get(self):
        return {'Ila': 'Here is all the data'}


api.add_resource(Map, '/Map')

api.add_resource(ZoneData, '/ZoneData')


if __name__ == '__main__':
    app.run(debug=True)