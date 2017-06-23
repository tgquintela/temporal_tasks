
"""
Process data of file `urb_cpop1.tsv`.

"""

import sys
import os
from os.path import isdir

import pandas as pd
import numpy as np

## Generic parameters
year_cols = [str(i) for i in range(1990, 2017)]
year_cols.reverse()
indices = 'indic_ur,cities\\time'
new_indices = ['indic_ur', 'NUTS']


## Useful function tools
def extractor_f(s):
    s = [int(s) for s in str.split(s) if s.isdigit()]
    if len(s) != 0:
        s = s[0]
    else:
        s = np.nan
    return s


def get_population(pop_data):
    # Like changes in population are small (lets get the last population or null)
    for year in year_cols:
        if not pd.isnull(pop_data[year]):
            return pop_data[year]
    else:
        return 0


def input_arguments_parser(args):
    ## Parse the parameters
    pathdata = 'data/'
    if len(args) == 2:
        outpath = os.path.join(pathdata, args[1])
    else:
        assert(len(args) == 3)
        pathdata = args[1]
        assert(type(args[2]) == str)
        outpath = os.path.join(pathdata, args[2])
    if not isdir(outpath):
        os.mkdir(outpath)
    assert(isdir(pathdata))
    ## Update the locals
    globals().update(locals())


if __name__ == "__main__":

    ## Read arguments (pathdata, outputpath)
    input_arguments_parser(sys.argv)

    ## Read data
    data = pd.read_csv(os.path.join(pathdata, 'urb_cpop1.tsv'),
                       sep='\t', na_values=':')

    ## Format columns names
    data.columns = [col.strip() for col in data.columns]

    ## Format properly data
    data[year_cols] = data[year_cols].applymap(extractor_f)

    ## Clean population column
    #data[year_cols].apply(get_population)
    new_pop = []
    for i in range(len(data)):
        new_pop.append(get_population(data[year_cols].loc[i]))

    ## Outformatting data
    pop_data = data[indices].apply(lambda s: pd.Series(s.split(',')))
    pop_data.columns = new_indices
    pop_data['population'] = pd.Series(new_pop)

    ## TODO: End the process. But for now it seems a deprecated script.


