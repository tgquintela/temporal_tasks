# Tutorial `EU_Demo_Fahne`

## Main files
Ensure you have:
* `population_data_unique.py`
* `fahne_creator.py`
* `fahne_formatter.py`
* `fahne_plotter.py`
* `r_gind3` data from the EU in [eurostat](http://ec.europa.eu/eurostat/web/products-datasets/-/demo_r_gind3).

## Steps

1. Transform the population data in r_gind3 to csv using a GIS program as QGIS.
2. Move that data to your data folder of the project.
3. Use script `population_data_unique.py` with the parameters of the data folder and name of the project preferred. It is going to generate some files in your project folder.
4. Join the new file computed and placed in your project folder `pop_output.csv` against the data of population with geometry using some GIS program as QGIS. Use the EU data as base. Be careful of using the point data.
5. Save that file with the name of pop_output_geo.csv`
6. Run script `fahne_creator.py` using parameters of the pathtodata and name of the project. It is going to generate an `*.svg` file with the new Flag.


## TODO
* [ ] Ensure proper stars.
* [ ] Ensure not crossing.
* [ ] File of parameters.
* [ ] Intelligent setting to avoid crossing stars.
