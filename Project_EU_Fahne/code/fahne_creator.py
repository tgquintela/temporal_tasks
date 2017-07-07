

"""
# Fhane creation

## Tutorial
1. Follow the steps of `population_data_unique.py` script.
2. Join the output file data `pop_output.csv` placed in the project folder
with the locations data in `r_gind3`.
3. Run that script.

"""

from fahne_formatter import *
from fahne_plotter import *


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

    ## Output data
    fahne_data.to_csv(os.path.join(pathproject, 'fahne_pop.csv'))

    ## Compute plot of stars
    stars_poly = stars_creation(fahne_data)
    fahne = plot_stars(stars_poly)

    ## Output EU fahne
    fahne.savefig(os.path.join(pathproject, 'eu_'+nameproject+'_fahne.svg'),
                  transparent=False, bbox_inches='tight', pad_inches=0)


