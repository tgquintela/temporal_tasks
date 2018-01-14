
import numpy as np


class Splitters(object):

    def __init__(self, mode, parameters, ranges=None):
        if mode == 'equispaced_splitters':
            self.splitters, self.open_limits, self.reverse =\
                create_equispaced_splitters_ind(**parameters)

        self.ranges = ranges

    def __call__(self, value):
        if '__len__' not in dir(value):
            value = np.array([value])
        category =\
            split_column_data(value, self.splitters, ranges=self.ranges,
                              open_limits=self.open_limits,
                              reverse=self.reverse)
        category = category[0]
        return category


def create_equispaced_splitters_ind(n_splits, limits=None,
                                    open_limits=True, reverse=False):
    ## Formatting parameters and defensive checking
    pos_ints = (int, np.int, np.int0, np.int8, np.int16, np.int32,
                np.int64, np.integer)
    if limits is None:
        limits = (0, 1)
        open_limits = False
    elif not isinstance(limits, (list, tuple)):
        raise TypeError("Not proper type for the parameter limits.")
    if not isinstance(n_splits, pos_ints):
        raise TypeError("Not proper type for the parameter n_splits.")
    if open_limits is None:
        open_limits = True
    elif not isinstance(open_limits, bool):
        raise TypeError("Not proper type for the parameter open_limits.")
    if reverse is None:
        reverse = False
    elif not isinstance(reverse, bool):
        raise TypeError("Not proper type for the parameter reverse.")

    splitters = list(np.linspace(limits[0], limits[1], n_splits+1))

    return splitters, open_limits, reverse


def create_equispaced_splitters(variables, n_splits, limits=None,
                                open_limits=True, reverse=False):
    """Create splitters throught the variables we want using intervals of the
    same size over the limits given.

    Parameters
    ----------
    variables: list of str
        The variable names we want to use to split the data.
    n_splits: list of int or int
        The number of splits over the data for each variable.
    limits: list of tuples, tuple or None
        the limits over the ones we want to create the splits.
    open_limits: boolean or list of booleans
        if the limits are defined open or close. If there are open limits,
        the limits have to consider the -inf and +inf.

    Returns
    -------
    abs_splitters: dict of lists
        the splitters defined in absolute numbers. It is a dictionary in which
        each key represent each column to split and each value is a list of the
        splitters defined in absolute limits.
    open_limits: dict of booleans
        if the splits should be performed using open limits or closed limits.
    reverse: dict of booleans
        if the scores have to be assigned in the descending or ascending way.

    """
    ## Formatting parameters and defensive checking
    pos_ints = (int, np.int, np.int0, np.int8, np.int16, np.int32,
                np.int64, np.integer)
    if limits is None:
        limits = [(0, 1) for _ in range(len(variables))]
        open_limits = False
    elif isinstance(limits, (list, tuple)):
        if len(limits) != len(variables):
            raise IndexError("Not proper length for the limits parameter.")
    else:
        raise TypeError("Not proper type for the parameter limits.")
    if isinstance(n_splits, pos_ints):
        n_splits = [n_splits for _ in range(len(variables))]
    elif isinstance(n_splits, (list, tuple)):
        if len(n_splits) != len(variables):
            raise IndexError("Not proper length for the n_splits parameter.")
    else:
        raise TypeError("Not proper type for the parameter n_splits.")
    if open_limits is None:
        open_limits = [True for e in variables]
    elif isinstance(open_limits, (tuple, list)):
        if len(open_limits) != len(variables):
            msg = "Not proper length for the open_limits parameter."
            raise IndexError(msg)
    elif isinstance(open_limits, bool):
        logi = open_limits
        open_limits = [logi for v in variables]
    else:
        raise TypeError("Not proper type for the parameter open_limits.")
    if reverse is None:
        reverse = [False for e in variables]
    elif isinstance(reverse, (tuple, list)):
        if len(reverse) != len(variables):
            raise IndexError("Not proper length for the reverse parameter.")
    elif isinstance(reverse, bool):
        logi = reverse
        reverse = [logi for v in variables]
    else:
        raise TypeError("Not proper type for the parameter reverse.")
    ## Create splitters
    splitters = {}
    for i, var in enumerate(variables):
        splitters[var] = list(np.linspace(limits[i][0], limits[i][1],
                                          n_splits[i]+1))
    open_limits = dict(zip(variables, open_limits))
    reverse = dict(zip(variables, reverse))
    return splitters, open_limits, reverse


def create_equispaced_abs_splitters(data, variables, n_splits, limits=None,
                                    open_limits=True, reverse=False):
    """Create absolute splitters throught the variables we want using intervals
    of the same size over the limits given.
    WARNING: Assumption that limits are defined in a quantile way: [0, 1]

    Parameters
    ----------
    data: pandas.DataFrame
        the data we want to split in categories regarding its values relative\
        to the splitters.
    variables: list of str
        The variable names we want to use to split the data.
    n_splits: list of int or int
        The number of splits over the data for each variable.
    limits: list of tuples, tuple or None
        the limits over the ones we want to create the splits.
    open_limits: boolean or list of booleans
        if the limits are defined open or close. If there are open limits,
        the limits have to consider the -inf and +inf.

    Returns
    -------
    abs_splitters: dict of lists
        the splitters defined in absolute numbers. It is a dictionary in which
        each key represent each column to split and each value is a list of the
        splitters defined in absolute limits.
    open_limits: dict of booleans
        if the splits should be performed using open limits or closed limits.
    reverse: dict of booleans
        if the scores have to be assigned in the descending or ascending way.

    """
    ## Relative splitters
    splitters, open_limits, reverse =\
        create_equispaced_splitters(variables, n_splits, limits, open_limits,
                                    reverse)
    abs_splitters = from_relative_splits_to_abs(data, splitters)
    return abs_splitters, open_limits, reverse


def from_relative_splits_to_abs(data, splitters):
    """Function to transform the splitters defined by quantiles to a absolute
    splitters.

    Parameters
    ----------
    data: pandas.DataFrame
        the data we want to split in categories regarding its values relative\
        to the splitters.
    splitters: dict of lists
        the splitters defined by quantiles. It is a dictionary in which each
        key represent each column to split and each value is a list of the
        splitters defined by quantiles.

    Returns
    -------
    abs_splitters: dict of lists
        the splitters defined in absolute numbers. It is a dictionary in which
        each key represent each column to split and each value is a list of the
        splitters defined in absolute limits.

    """
    abs_splitters = {}
    for column in splitters:
        abs_splitters[column] = [data[column].quantile(quantile)
                                 for quantile in splitters[column]]
    return abs_splitters


#### Splits management
######################
def classify_with_absolute_splits(data, splitters, ranges=None,
                                  open_limits=None, reverse=None):
    """Classification on absolute splits. Each column is split individually and
    independently.

    Parameters
    ----------
    data: pandas.DataFrame
        the data we want to split in categories regarding its values relative
        to the splitters.
    splitters: dict of lists
        the splitters defined by absolute value. It is a dictionary in which
        each key represent each column to split and each value is a list of the
        splitters.
    ranges: dict of lists (default None)
        the assigned values for the categories of each of the variables.
    open_limits: dict of booleans (default None)
        the open_limits set if the limits are defined open or close. It is a
        dictionary in which each key represent each column to split and each
        value is if it is defined open or close the limit.
    reverse: dict of booleans (default None)
        the revese set if the splittings are defined in direct or reverse way.
        It is a dictionary in which each key represent each column to split
        and each value is if it is defined reversely or not.

    Returns
    -------
    categories_by_col: numpy.ndarray
        the categories or scores associated to each column or variable.

    """
    ## Setting parameters
    if open_limits is None:
        open_limits = {}
        for k in splitters:
            open_limits[k] = True
    elif isinstance(open_limits, dict):
        to_defaults = set(splitters.keys()).difference(set(open_limits))
        for v in to_defaults:
            open_limits[v] = True
    elif isinstance(open_limits, list):
        if len(open_limits) != len(splitters.keys()):
            raise IndexError("Not proper lenght of open_limits parameter.")
        open_limits = dict(zip(list(splitters.keys()), open_limits))
    elif isinstance(open_limits, bool):
        logi = open_limits
        open_limits = {}
        for v in splitters:
            open_limits[v] = logi
    else:
        raise TypeError("Incorrect type of open_limits parameter.")
    ## Reverse
    if reverse is None:
        reverse = {}
        for k in reverse:
            reverse[k] = False
    elif isinstance(reverse, dict):
        to_defaults = set(splitters.keys()).difference(set(reverse))
        for v in to_defaults:
            reverse[v] = False
    elif isinstance(reverse, list):
        if len(reverse) != len(splitters.keys()):
            raise IndexError("Not proper lenght of reverse parameter.")
        reverse = dict(zip(list(splitters.keys()), reverse))
    elif isinstance(reverse, bool):
        logi = reverse
        reverse = {}
        for v in splitters:
            reverse[v] = logi
    else:
        raise TypeError("Incorrect type of reverse parameter.")
    if ranges is None:
        ranges = {}
        for e in splitters:
            ranges[e] = list(range(len(splitters[e])+1))
    categories_by_col = []
    for column in splitters:
        if not len(splitters[column]):
            categories_col = null_split_column_data(data[column])
            continue
        categories_col = split_column_data(data[column], splitters[column],
                                           ranges[column],
                                           open_limits[column],
                                           reverse[column])
        categories_by_col.append(categories_col)
    return categories_by_col


def null_split_column_data(data_column):
    """Null split. Not categorize. Only using the same values as the variable.
    Parameters
    ----------
    data_column: pandas.Series
        a column from the  data we want to split in categories regarding its
        values relative to the splitters.
    """
    return np.array(data_column)


def split_column_data(data_column, splitters, ranges=None, open_limits=True,
                      reverse=False):
    """Classification of data for the given column using absolute splitters.
    Parameters
    ----------
    data_column: pandas.Series
        a column from the  data we want to split in categories regarding its
        values relative to the splitters.
    splitters: list
        the splitters defined by absolute value. It is a list with the cutoff
        values which define the limits of the categories.
    ranges: list (default None)
        the assigned categories for each individual variable.
    open_limits: boolean (default True)
        if the limits are defined open or close. If there are open limits,
        the limits have to consider the -inf and +inf.
    reverse: boolean (default False)
        if the split should be performed in the reversed way.
    Returns
    -------
    categories: numpy.ndarray
        the categories or scores creating after the splitting.
    """
    ## Apply splits
    if open_limits and not reverse:
        categories =\
            split_values_open_limits_direct(data_column, splitters, ranges)
    elif open_limits and reverse:
        categories =\
            split_values_open_limits_reverse(data_column, splitters, ranges)
    elif not open_limits and not reverse:
        categories =\
            split_values_close_limits_direct(data_column, splitters, ranges)
    elif not open_limits and reverse:
        categories =\
            split_values_close_limits_reverse(data_column, splitters, ranges)
    return categories


def split_values_open_limits_direct(values, splitters, ranges=None):
    """Splitting over the limits using direct splitting (doing it in the
    ascending order) using open limits in the extremes.
    """
    ## Prepare inputs
    if ranges is None:
        ranges = list(range(len(splitters)+1))
    ranges = list(ranges)
    assert(len(splitters)+1 == len(ranges))
    splitters = sorted(splitters)
    ## Compute splits
    categories = -1*np.ones(len(values), dtype=int)
    logi = values < splitters[0]
    categories[logi] = ranges[0]
    for i in range(0, len(splitters)-1):
        logi_higher = values >= splitters[i]
        logi_lower = values < splitters[i+1]
        logi = np.logical_and(logi_lower, logi_higher)
        categories[logi] = ranges[i+1]
    logi = values >= splitters[-1]
    categories[logi] = ranges[len(splitters)]
    assert(np.sum(categories == -1) == 0)
    return categories


def split_values_open_limits_reverse(values, splitters, ranges=None):
    """Splitting over the limits using reverse splitting (doing it in the
    descending order) using open limits in the extremes.
    """
    ## Prepare inputs
    if ranges is None:
        ranges = list(range(len(splitters)+1))
    ranges = list(ranges)
    assert(len(splitters)+1 == len(ranges))
    splitters = sorted(splitters)[::-1]
    ## Compute splits
    categories = -1*np.ones(len(values), dtype=int)
    logi = values > splitters[0]
    categories[logi] = ranges[0]
    for i in range(0, len(splitters)-1):
        logi_higher = values <= splitters[i]
        logi_lower = values > splitters[i+1]
        logi = np.logical_and(logi_lower, logi_higher)
        categories[logi] = ranges[i+1]
    logi = values <= splitters[-1]
    categories[logi] = ranges[len(splitters)]
    assert(np.sum(categories == -1) == 0)
    return categories


def split_values_close_limits_direct(values, splitters, ranges=None):
    """Splitting over the limits using direct splitting (doing it in the
    ascending order) using close limits in the extremes.
    """
    ## Prepare inputs
    if ranges is None:
        ranges = list(range(len(splitters)-1))
    ranges = list(ranges)
    assert(len(splitters)-1 == len(ranges))
    splitters = sorted(splitters)
    ## Compute splits
    categories = -1*np.ones(len(values), dtype=int)
    for i in range(0, len(splitters)-1):
        logi_higher = values >= splitters[i]
        logi_lower = values < splitters[i+1]
        logi = np.logical_and(logi_lower, logi_higher)
        categories[logi] = ranges[i]
    ## Extreme case
    categories[values == splitters[i+1]] = ranges[i]
    assert(np.sum(categories == -1) == 0)
    return categories


def split_values_close_limits_reverse(values, splitters, ranges=None):
    """Splitting over the limits using reverse splitting (doing it in the
    descending order) using close limits in the extremes.
    """
    ## Prepare inputs
    if ranges is None:
        ranges = list(range(len(splitters)-1))
    ranges = list(ranges)
    assert(len(splitters)-1 == len(ranges))
    splitters = sorted(splitters)[::-1]
    ## Compute splits
    categories = -1*np.ones(len(values), dtype=int)
    for i in range(0, len(splitters)-1):
        logi_higher = values <= splitters[i]
        logi_lower = values > splitters[i+1]
        logi = np.logical_and(logi_lower, logi_higher)
        categories[logi] = ranges[i]
    categories[values == splitters[i+1]] = ranges[i]
    assert(np.sum(categories == -1) == 0)
    return categories
