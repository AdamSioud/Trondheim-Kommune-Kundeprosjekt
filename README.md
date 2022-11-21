# Trondheim Kommune Kundeprosjekt 

## Presentation
Trondheim Kommune has commissioned a group of students to create a prototype to find out the best place to live in Trondheim according to certain criteria

This project is divided into two parts, this repository is the server part (backend).

You can find the interface part (frontend) here: https://github.com/AdamSioud/Trondheim-Kommune-Prosjekt-Frontend

A part of the repository is dedicated to the generation of GeoJSON (our database): `generate_geojson`.
Another part is dedicated to the server with Flask: ``server``

## Installation
You can find more details about the installation with the following folders:
- [`generate_geojson`](/generate_geojson/README.md)
- [`server`](/server/README.md)

## Folder structure
<pre>
.
├── README.md
└── server
    ├── README.md
    ├── app.py
    ├── model
    │   ├── generated_map.html
    │   ├── src
    │   │   ├── data
    │   │   │   ├── data.geojson
    │   │   │   ├── data.py
    │   │   │   └── data_interval.json
    │   │   ├── models.py
    │   │   └── parameters
    │   │       ├── age_param.py
    │   │       ├── culture_param.py
    │   │       ├── distance_param.py
    │   │       ├── environment_param_interface.py
    │   │       ├── grocery_param.py
    │   │       ├── noise_param.py
    │   │       ├── outdoor_param.py
    │   │       ├── param_interface.py
    │   │       ├── price_param.py
    │   │       ├── safety_param.py
    │   │       ├── transport_param.py
    │   │       ├── walkway_param.py
    │   │       └── well_being_param.py
    │   └── test
    │       ├── mock_data
    │       │   ├── age.json
    │       │   ├── distance.json
    │       │   ├── general_df.json
    │       │   ├── neighborhood.json
    │       │   └── price.json
    │       ├── test_age_param.py
    │       ├── test_distance_param.py
    │       ├── test_models.py
    │       ├── test_noise_param.py
    │       ├── test_price_param.py
    │       └── test_safety_param.py
    └── requirements.txt
</pre>
