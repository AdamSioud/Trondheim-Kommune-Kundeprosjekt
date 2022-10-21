# Trondheim Kommune Kundeprosjekt API



https://medium.com/geekculture/how-to-architect-your-flask-rest-api-abf95637d9f5
=======
--- Architecture

https://medium.com/geekculture/how-to-architect-your-flask-rest-api-abf95637d9f5



--- Hosting

https://www.pythonanywhere.com/?affiliate_id=00535ced 

## Installation (WINDOWS)
1. Install [python](https://www.python.org/downloads/)
2. Check if pip is installed: ``pip --version``
3. Configure your PATH
4. Clone this repository: ``git clone https://github.com/AdamSioud/Trondheim-Kommune-Kundeprosjekt-API.git``
5. In the parent folder of the repository, create a new environment: ``python -m venv ./venv``
6. Activate the environment: ``.\venv\Scripts\activate``
7. Upgrade pip and install wheel: ``python -m pip install -U pip wheel setuptools``
8. In ``venv`` create a new folder: `geopandas dependencies`
9. Go [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/) and search for these packages ``GDAL, Pyproj, Fiona, Shapely`` according to your version of python and 32 or 64 bit (E.g. for Python v3.7x (64-bit), GDAL package should be GDAL‑3.1.2‑cp37‑cp37m‑win_amd64.whl.) put them in the folder
10. Go in the folder: ``cd "geopandas dependencies"``
11. ``pip install`` on each FILE following this order ``GDAL``, ``pyproj``, ``Fiona``, ``Shapely``
12. Go in the project: ``cd ..\..\Trondheim-Kommune-Kundeprosjekt-API``
13. Run ``pip install -r requirements.txt``


I followed the instructions [here](https://towardsdatascience.com/geopandas-installation-the-easy-way-for-windows-31a666b3610f) 

## Installation (MAC)

1. Install [python](https://www.python.org/downloads/)
2. Check if pip is installed: ``pip3 --version``
3. Clone this repository: ``git clone https://github.com/AdamSioud/Trondheim-Kommune-Kundeprosjekt.git``
4. In the parent folder of the repository, create a new environment: ``python3 -m venv ./venv``
5. Activate the environment: ``chmod +x ./venv/bin/activate``
6. Upgrade pip and install wheel: ``python3 -m pip install -U pip wheel setuptools``
7. Install GDAL: ``brew install gdal``
8. Search for file ``Python.h`` (probably here: ``/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/Headers``)
9. Depending on your terminal, open the configuration file (e.g. for zsh: ``open -e $path_of_home$/.zprofile``) and write ``export C_INCLUDE_PATH=$path_to_Python.h_folder$``
10. ``pip3 install`` on the following packages ``Fiona Pyproj Shapely``
11. Go in the project: ``cd ../../Trondheim-Kommune-Kundeprosjekt-API``
12. Run ``pip3 install -r requirements.txt``


