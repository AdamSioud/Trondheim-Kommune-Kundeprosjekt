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
├── DockerFile
├── README.md
├── generate_geojson
│   ├── README.md
│   ├── build_files.py
│   ├── configuration.py
│   ├── converters.py
│   ├── data.geojson
│   ├── data_general.json
│   ├── data_interval.json
│   ├── generate.py
│   └── renaming.py
├── requirements.txt
└── server
    ├── README.md
    ├── api.py
    └── model
        ├── src
        │   ├── data
        │   │   ├── data.geojson
        │   │   ├── data_general.json
        │   │   ├── data_interval.json
        │   │   └── data_manager.py
        │   ├── map_manager.py
        │   └── parameters
        │       ├── abstract_neighborhood_parameter.py
        │       ├── abstract_parameter.py
        │       ├── age_parameter.py
        │       ├── culture_parameter.py
        │       ├── distance_parameter.py
        │       ├── grocery_parameter.py
        │       ├── noise_parameter.py
        │       ├── outdoor_parameter.py
        │       ├── price_parameter.py
        │       ├── safety_parameter.py
        │       ├── transport_parameter.py
        │       ├── walkway_parameter.py
        │       └── well_being_parameter.py
        └── test
            ├── mock_data
            │   ├── age.json
            │   ├── distance.json
            │   ├── general_df.json
            │   ├── neighborhood.json
            │   └── price.json
            ├── test_age_parameter.py
            ├── test_distance_parameter.py
            ├── test_map_manager.py
            ├── test_noise_parameter.py
            ├── test_price_parameter.py
            └── test_safety_parameter.py

</pre>
