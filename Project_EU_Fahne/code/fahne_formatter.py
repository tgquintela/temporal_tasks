
"""
Prepare the data to be plotted. There are different conditions for the output:

* All has to be between xlim(-1.5, 1.5), ylim(-1, 1)
* The stars should not be overlapped

"""

import pickle
import sys
import os
from os.path import isdir, isfile

import pandas as pd


def fahne_formatting(pop_data):
    pop_var = 'pop_output_Value'
    pop_data.loc[:, 'radius'] = pop_data[pop_var]/(10*pop_data[pop_var].max())
    fahne_data = standarizing(pop_data)
    return fahne_data.loc[:, ['x', 'y', 'radius']]


def standarizing(pop_data):
    m = pop_data[['LAT', 'LON']].mean()
    s = pop_data[['LAT', 'LON']].std()
    pop_data[['y', 'x']] = (pop_data[['LAT', 'LON']]-m)/(2*s.mean())
    return pop_data


def input_arguments_parser(args):
    ## Parse the parameters
    # Only pathdata can be default
    pathdata = 'data/'
    if len(args) == 2:
        assert(type(args[1]) == str)
        nameproject = args[1]
    else:
        assert(len(args) == 3)
        pathdata = args[1]
        assert(type(args[2]) == str)
        nameproject = args[2]
    pathproject = os.path.join(pathdata, nameproject)
    assert(isdir(pathdata))
    assert(isdir(pathproject))
    ## Update the locals
    globals().update(locals())


if __name__ == "__main__":
    ## Read arguments (pathdata, nameproject)
    input_arguments_parser(sys.argv)

    ## Read data
    with open(os.path.join(pathproject, 'extra_data.pkl'), 'rb') as f:
        extra_data = pickle.load(f)
        NUTS_codes = extra_data['NUTS_codes']
    data = pd.read_csv(os.path.join(pathproject, 'pop_output_geo.csv'))

    ## General definitions
    def filter_nuts(x):
        return x in NUTS_codes

    ## Compute data
    data = data[data['NUTS_ID'].apply(filter_nuts)]
    fahne_data = fahne_formatting(data)

    ## Output
    fahne_data.to_csv(os.path.join(pathproject, 'fahne_pop.csv'))

