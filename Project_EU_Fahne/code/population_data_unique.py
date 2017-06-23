
"""
# Process data of files `r_gind3`

## Tutorial
1. Transform the population data in r_gind3 to csv.
2. Move that data to your data folder of the project.
3. Use that script

"""

import sys
import os
from os.path import isdir, isfile
import pickle

import pandas as pd
import numpy as np

## Generic parameters
new_features = ['NUTS_country', 'NUTS_idxs', 'NUTS1', 'NUTS2', 'NUTS3', 'NUTS_level']
non_EU_members = ['UK', 'IS', 'LI', 'NO', 'CH', 'ME', 'MK', 'AL', 'TR']
filt_eu_members = lambda x: x not in non_EU_members

## Useful function tools
def treat_code_beta(code):
    country_code, subindices = '', ''
    for letter in code:
        if not str.isdigit(letter):
            country_code += letter
        else:
            subindices += letter
    nuts_lvl = len(subindices)
    return country_code, subindices, nuts_lvl


def treat_code(code):
    country_code, subindices = code[:2], code[2:]
    nuts_lvl = len(subindices)
    nuts1, nuts2, nuts3 = '', '', ''
    if nuts_lvl > 0:
        nuts1 = subindices[0]
    if nuts_lvl > 1:
        nuts2 = subindices[1]
    if nuts_lvl > 2:
        nuts3 = subindices[2]
    return country_code, subindices, nuts1, nuts2, nuts3, nuts_lvl


def cleaner_population(s):
    if type(s) in [unicode, str]:
        s = s.strip().replace(' ','')
        if s.isdigit():
            s = int(s)
        else:
            s = np.nan
    return s


def detect_external_territories(code_idxs):
    ## FAIL
    flag = False
    if len(code_idxs):
        if not str.isdigit(code_idxs[0]):
            flag = True
    return flag


def filter_populations(pop_data, parameters):
    # TODO: Other cases
    pop_output = pop_data[pop_data['NUTS_level'] == parameters['level']]
    pop_output = pop_output[pop_output['NUTS_country'].apply(filt_eu_members)]
    return pop_output


def input_arguments_parser(args):
    ## Parse the parameters
    # Only pathdata can be default
    pathdata = 'data/'
    if len(args) == 3:
        assert(type(args[1]) == str)
        assert(type(args[2]) == str)
        namedata = args[1]
        nameproject = args[2]
        outpath = os.path.join(pathdata, nameproject)
    else:
        assert(len(args) == 4)
        pathdata = args[1]
        assert(type(args[2]) == str)
        namedata = args[2]
        assert(type(args[3]) == str)
        nameproject = args[3]
        outpath = os.path.join(pathdata, nameproject)
    if not isdir(outpath):
        os.mkdir(outpath)
    assert(isdir(pathdata))
    assert(isfile(os.path.join(pathdata, namedata)))
    parameters = {'level': 1}
    ## Update the locals
    globals().update(locals())


if __name__ == "__main__":
    ## Read arguments (pathdata, namedata, nameproject) -> (outpath)
    input_arguments_parser(sys.argv)

    ## Read data
    data = pd.read_csv(os.path.join(pathdata, namedata),
                       sep=',', na_values=':')

    ## Process data
    data.columns = [col.strip() for col in data.columns]
    data[new_features] = data['GEO'].apply(lambda s: pd.Series(treat_code(s)))
    data.loc[:, 'Value'] = data['Value'].apply(cleaner_population)

    ## Filter only with the last time
    codes_id = data['GEO'].unique()
    pop_data = []
    for i in range(len(codes_id)):
        aux_table = data[data['GEO'] == codes_id[i]]
        aux_table = aux_table[aux_table['Value'].apply(lambda x: not pd.isnull(x))]
        aux_table = aux_table[aux_table['TIME'] == aux_table['TIME'].max()]
        pop_data.append(aux_table)
    pop_data = pd.concat(pop_data)

    ## Countries treatment
    EU_members = [c for c in pop_data['NUTS_country'] if c not in non_EU_members]

    ## Filter with the lower level of aggregation
    ## First approach country level
    pop_output = filter_populations(pop_data, parameters)

    ## Outputs
    pop_output.to_csv(os.path.join(outpath, 'pop_output.csv'))
    with open(os.path.join(outpath, 'extra_data.pkl'), 'wb') as f:
        pickle.dump({'NUTS_codes': list(pop_output['GEO']),
                     'parameters': parameters},
                    f)



