# folder that contains all the data base model classes with constraints

from shapely.speedups._speedups import Point
import geopandas as gpd
import pandas as pd
from pathlib import Path
from server.model.src.parameters.age_param import AgeParam
from server.model.src.parameters.culture_param import CultureParam
from server.model.src.parameters.distance_param import DistanceParam
from server.model.src.parameters.grocery_param import GroceryParam
from server.model.src.parameters.outdoor_param import OutdoorParam
from server.model.src.parameters.price_param import PriceParam
from server.model.src.parameters.safety_param import SafetyParam
from server.model.src.parameters.transport_param import TransportParam
from server.model.src.parameters.walkway_param import WalkwayParam
from server.model.src.parameters.well_being_param import WellBeingParam
from server.model.src.parameters.noise_param import NoiseParam
from server.model.src.data.data import Data


class Model:
    def __init__(self):
        self.data = Data()
        self.parameters = [
            PriceParam(self.data),
            AgeParam(self.data),
            DistanceParam(self.data),
            WellBeingParam(self.data),
            SafetyParam(self.data),
            CultureParam(self.data),
            OutdoorParam(self.data),
            TransportParam(self.data),
            WalkwayParam(self.data),
            GroceryParam(self.data),
            SafetyParam(self.data)
        ]

    def generate_map(self, param_input: dict):
        print((param_input))
        result = self.data.GENERAL_DF.copy().filter(items=['Levekårsnavn', 'Score'])
        result['Score'] = 0
        for param in self.parameters:
            if param.INPUT_NAME in param_input.keys():
                inp = param_input[param.INPUT_NAME]
                tmp = param.calculate_score(inp)
                result['Score'] = result['Score'].add(tmp['Score'], fill_value=0)
            elif 'environment' in param_input.keys():
                if param.INPUT_NAME in param_input['environment'].keys():
                    inp = param_input['environment'][param.INPUT_NAME]
                    tmp = param.calculate_score(inp)
                    result['Score'] = result['Score'].add(tmp['Score'], fill_value=0)
        # ---
        # res: gpd.GeoDataFrame = gpd.GeoDataFrame(result, geometry=self.data.GEOMETRY)
        # m = res.explore('Score')
        # path_base = Path(__file__).resolve().parent
        # outfp = path_base / "../generated_map.html"
        # m.save(outfp)
        # ---
        # print('result: ', result['Score'])
        # print('res: ', res['Score'])
        # result['Score'] = pd.qcut(result['Score'], 5, labels=False, duplicates='drop')
        result['Score'] = result['Score'].astype(float)
        return gpd.GeoDataFrame(result, geometry=self.data.GEOMETRY)

    def get_zone_by_id(self, i: int):
        return self.data.get_zone_by_id(i)


# Testing ...
par_input = {
    "age_input": {
        "selected": ['underage (0-17)', 'young adult (18-34)'],
        "percent": 10,
        "weight": 4
    },
    "price_input": {
        "selected": ['small', "medium"],
        "budget": 2400000,
        "weight": 4
    },
    "distance_input": {
        "position": Point(10.39628304564158, 63.433247153410214),
        "weight": 4
    },
    "environment": {
        "well_being_input": {
            "weight": 4
        },
        "safety_input": {
            "weight": 1
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
        "grocery_input": {
            "weight": 4
        },
        "noise_input": {
            "weight": 4
        }
    }
}
'''
model = Model()
res = model.generate_map(par_input)

# with open("sample.json", "w") as outfile:
#     outfile.write(res.to_json())

m = res.explore('Score')
path_base = Path(__file__).resolve().parent
outfp = path_base / "../generated_map.html"
m.save(outfp)
'''
