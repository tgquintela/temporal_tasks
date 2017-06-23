

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from shapely.geometry import Point, MultiPoint, MultiPolygon, Polygon, LinearRing
from descartes import PolygonPatch
import numpy as np
import pandas as pd


def star_creation(center, radius):
    #http://www.mathalino.com/reviewer/plane-geometry/area-of-regular-five-pointed-star
    r_pent = np.sin(np.pi/10)/np.sin(0.7*np.pi)*radius
    original_dir = np.random.uniform(0, 2*np.pi)

    angles = []
    for i in range(10):
        angles.append(i*2*np.pi/10+original_dir)
    
    points = []
    for i in range(5):
        points.append((radius*np.sin(angles[2*i])+center[0],
                       radius*np.cos(angles[2*i])+center[1])
                      )
        points.append((r_pent*np.sin(angles[2*i+1])+center[0],
                       r_pent*np.cos(angles[2*i+1])+center[1])
                      )

    #[points]+[points[0]]
    poly = Polygon(points)
    return poly


def stars_creation(data):
    stars = []
    for i in range(len(data)):
        stars.append(star_creation(data.iloc[i][['x', 'y']].as_matrix(),
                                   data.iloc[i]['radius']))
    return stars


def plot_stars(stars):
    fig = plt.figure(1, figsize=(9, 6), dpi=90)#, frameon=False)
#    canvas = FigureCanvas(fig)
    if matplotlib.__version__ > '2':
        axes = fig.add_subplot(1, 1, 1, facecolor='#003399')
    else:
        axes = fig.add_subplot(1, 1, 1, axis_bgcolor='#003399')
    fig.tight_layout(pad=0.)
    axes.set_xlim([-1.5, 1.5])
    axes.set_ylim([-1, 1])
    axes.axes.get_xaxis().set_visible(False)
    axes.axes.get_yaxis().set_visible(False)
    for star_poly in stars:
        star_patch = PolygonPatch(star_poly, color='#FFCC00')
        axes.add_patch(star_patch)
    fig = plt.gcf()
    plt.close()
    return fig


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
    data = pd.read_csv(os.path.join(pathproject, 'fahne_pop.csv'))

    ## Compute data
    stars_poly = stars_creation(data)
    fahne = plot_stars(stars_poly)

    ## Output
    fahne.savefig(os.path.join(pathproject, 'eu_'+nameproject+'_fahne.svg'),
                  transparent=False, bbox_inches='tight', pad_inches=0)



