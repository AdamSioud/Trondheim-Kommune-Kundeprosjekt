from generate_geojson.converters import *

link_geo_json_file = "https://kart.trondheim.kommune.no/levekar2020/personer0_17/2018.js"

final_columns = ["Andel", "Antall", "Gjennomsnittspris"]

properties = {
    "Levekårsnavn": [],
    "age": [],
    "price": [],
    "neighborhood": [],
    "geometry": []
}

POPULATION = "120UjUkUfX5is20D_SX3z99vfuCHOVuN8RI1yE3-L4OM"
HOUSING = "1pU_p7FToI3VerocJXSp1-zMtWNk9SsKL_Tv7nImiXF8"
NEIGHBORHOOD = "1s51rcfCGPpjc1hx-6B7IqC6IfBjgSR2JAwOsW9ykI3U"

sheets = {
    "age": {
        "key": POPULATION,
        "values": {
            "0-17": "1-10",
            "18-34": "1-40",
            "35-66": "1-70",
            "67+": "1-100",
        }
    },
    "price": {
        "key": HOUSING,
        "values": {
            "average": "2-260",
        }
    },
    "neighborhood": {
        "key": NEIGHBORHOOD,
        "values": {
            "wellBeingW": "10-10",
            "wellBeingM": "10-20",
            "safetyW": "10-30",
            "safetyM": "10-40",
            "cultureW": "10-50",
            "cultureM": "10-60",
            "outdoorLifeW": "10-90",
            "outdoorLifeM": "10-100",
            "publicTransportW": "10-110",
            "publicTransportM": "10-120",
            "groceryStoresW": "10-130",
            "groceryStoresM": "10-140",
            "walkwayAndBikePathW": "10-150",
            "walkwayAndBikePathM": "10-160",
            "noiseTrafficW": "10-170",
            "noiseTrafficM": "10-180",
            "noiseOtherM": "10-190",
            "noiseOtherW": "10-200",

        }
    }
}

converters = {
    "Andel": lambda s: percent_to_float(s),
    "Gjennomsnittspris": lambda s: string_to_int(s)
}

# Configuration for general data of Trondheim
properties_trondheim = {
    "age": [],
    "price": [],
    "neighborhood": []
}

final_columns_trondheim = ["Andel i \nTrondheim", "Gjennomsnittspris i \nTrondheim", "Andel i Trondheim"]

converters_trondheim = {
    "Andel i \nTrondheim": lambda s: percent_to_float(s),
    "Andel i Trondheim": lambda s: percent_to_float(s),
    "Gjennomsnittspris i \nTrondheim": lambda s: string_to_int(s)
}

renaming = {
    "Andel i Trondheim": "portion",
    "Andel i \nTrondheim": "portion",
    "Gjennomsnittspris i \nTrondheim": "averagePrice"
}

# Configuration for interval
final_names_interval = ["intervall"]

properties_interval = {
    "neighborhood": []
}

sheets_interval = {
    "neighborhood": {
        "key": NEIGHBORHOOD,
        "values": {
            "wellBeing": "10-10",
            "safety": "10-30",
            "culture": "10-50",
            "outdoorLife": "10-90",
            "publicTransport": "10-110",
            "groceryStores": "10-130",
            "walkwayAndBikePath": "10-150",
            "noiseTraffic": "10-170",
            "noiseOther": "10-190",
        }
    }
}

converters_interval = {
    "intervall ": lambda s: interval_converter(s)
}
