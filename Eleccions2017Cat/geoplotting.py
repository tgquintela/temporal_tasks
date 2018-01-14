
"""
GeoPlotting tools
-----------------
Tools to plot the results in a geographic map.

"""

import folium
import matplotlib
import numpy as np
import seaborn as sns
from splitters import Splitters


def results_map(center_loc, zoom_start, geodata, results, key_on, key_data):
    """Results map. Geographic plot of the results.    

    """
    m = folium.Map(center_loc, tiles='cartodbpositron',
                   zoom_start=zoom_start)

    n_splits = 10
    par_splits = {'n_splits': n_splits, 'limits': (0, 1),
                  'open_limits': False, 'reverse': False}
    splitter = Splitters('equispaced_splitters', par_splits,
                         ranges=list(range(n_splits)))
    colors = sns.color_palette('RdYlGn', n_splits)

    def color_map(x):
        return matplotlib.colors.rgb2hex(colors[splitter(x)])

    def create_function_style(features):
        style_function = lambda x: {'fillColor': color_map(features),
                                    'fillOpacity': 0.4,
                                    'color': 'black',
                                    'weight': 0.5,
                                    'opacity': 1}
        return style_function


    highlight_function = lambda x: {'weight': 1.5,
                                    'fillOpacity': 0.75}

    for i in range(len(geodata)):
        geodata_i = geodata.iloc[[i], :]
        key_on_i = geodata_i[key_on].ravel()[0]
        idxs = np.where(results[key_on].apply(lambda x: x == key_on_i))[0]
        if not len(idxs):
            continue
        idx_key = idxs[0]
        style_function = create_function_style(results.iloc[idx_key, :][key_data])
        geo_cens = folium.folium.GeoJson(geodata_i,
                                         style_function=style_function,
                                         highlight_function=highlight_function,
                                         overlay=True,
                                         control=False)
        geo_cens.add_child(folium.features.Popup(key_on_i))
        geo_cens.add_to(m, geodata.iloc[i, :][key_on])
    return m


def choropleth_map(center_loc, zoom_start, file_geojson, results, key_on, key_data):
    """Choropleth map from folium.
    """
    m = folium.Map(center_loc, tiles='cartodbpositron',
                   zoom_start=zoom_start)
    columns = [key_on, key_data]
    key_on_v = 'feature.properties.' + key_on
    m.choropleth(
        geo_data=file_geojson,
        data=results,
        columns=columns,
        key_on=key_on_v,
        fill_color='YlGn',
        highlight=True,
        )
    return m
