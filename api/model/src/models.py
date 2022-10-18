# folder that contains all the data base model classes with constraints

from shapely.speedups._speedups import Point
import geopandas as gpd

from api.model.src.parameters.AgeParam import AgeParam
from api.model.src.parameters.CultureParam import CultureParam
from api.model.src.parameters.GroceryParam import GroceryParam
from api.model.src.parameters.OutdoorParam import OutdoorParam
from api.model.src.parameters.PriceSliderParam import PriceSliderParam
from api.model.src.parameters.SafetyParam import SafetyParam
from api.model.src.parameters.TransportParam import TransportParam
from api.model.src.parameters.WalkwayParam import WalkwayParam
from api.model.src.parameters.WellBeinParam import WellBeingParam
from api.model.src.data.Data import Data


class Model:
    def __init__(self):
        self.data = Data()
        self.parameters = [
            PriceSliderParam(self.data, 0, 1),
            AgeParam(self.data, 0, 1),
            # DistanceParam(self.data),
            WellBeingParam(self.data),
            SafetyParam(self.data),
            CultureParam(self.data),
            OutdoorParam(self.data),
            TransportParam(self.data),
            GroceryParam(self.data),
            WalkwayParam(self.data),
            # NoiseTrafficParam(self.data),
            # NoiseOtherParam(self.data)
        ]

    def generate_map(self, param_input: dict ):
        result = self.data.GENERAL_DF.copy().filter(items=['Levekårsnavn', 'Score'])
        result['Score'] = 0
        for param in self.parameters:
            if param.INPUT_NAME in param_input.keys():
                inp = param_input[param.INPUT_NAME]
                tmp = param.calculate_score(inp)
                result['Score'] = result['Score'].add(tmp['Score'], fill_value=0)
        return gpd.GeoDataFrame(result, geometry=self.data.GEOMETRY)



# Testing ...
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

model = Model()
result = model.generate_map(param_input)
m = result.explore('Score')
outfp = "../generated_map.html"
m.save(outfp)

