
import pandas as pd


class GeoDataCensal(object):
    """GeoData of the censo information. There is information of the codes,
    names, censo and geometry. This class manage the hierharchy of geometry
    levels in which the data results are aggregated.

    """

    def __init__(self, data_censal, var_hierarchy):
        self._check_inputs(data_censal, var_hierarchy)
        self.data_censal = data_censal
        self.var_hierarchy = var_hierarchy
        self.levels = len(var_hierarchy['codes'])

    def _check_inputs(self, data_censal, var_hierarchy):
        assert('geometry' in var_hierarchy)
        assert('codes' in var_hierarchy)
        assert('names' in var_hierarchy)
        assert('censo' in var_hierarchy)
        assert(isinstance(var_hierarchy['geometry'], str))
        assert(isinstance(var_hierarchy['codes'], list))
        assert(isinstance(var_hierarchy['names'], list))
        assert(isinstance(var_hierarchy['censo'], list))
        assert(len(var_hierarchy['codes']) == len(var_hierarchy['names']))

    def _get_columns_level(self, level, outer=False):
        outer_cols = []
        if outer:
            outer_cols = self.outer_cols
        geo_cols = [self.var_hierarchy['geometry']]
        if level == 0:
            columns = outer_cols+geo_cols
        elif level > self.levels or level < 0:
            msg = "Not correct 'level' input."
            raise IndexError(msg)
        else:
            names_cols = self.var_hierarchy['names'][self.levels-level:]
            codes_cols = self.var_hierarchy['codes'][self.levels-level:]
            columns = list(set(outer_cols+names_cols+codes_cols+geo_cols))
        return columns

    def _filter4level(self, level, outer=False):
        return self.data_censal[self._get_columns_level(level, outer)]

    @classmethod
    def _data_reduction(cls, data_censo, var_hierarchy):
        return cls(data_censo, var_hierarchy)

    @property
    def inner_cols(self):
        inner_cols = [var_hierarchy['geometry']]
        inner_cols += var_hierarchy['codes']
        inner_cols += var_hierarchy['names']
        inner_cols += var_hierarchy['censo']
        inner_cols = list(set(inner_cols))
        return inner_cols

    @property
    def outer_cols(self):
        outer_cols = [col for col in self.data_censal
                      if col not in self.inner_cols]
        return outer_cols

    def _filter_censo_by_level(self, level, outer=False):
        data_censo = self._filter4level(level, outer)
        pivot_lvl_col = self.var_hierarchy['codes'][self.levels-level]
        data = data_censo.dissolve(by=pivot_lvl_col).reset_index(level=0)
        if self.var_hierarchy['censo']:
            data_censal = self.data_censal[[pivot_lvl_col]]
            vars_censo = self.var_hierarchy['censo']
            data_censal[vars_censo] = self.data_censal[vars_censo]
            data_cns = data_censal.dissolve(by=pivot_lvl_col,
                                            aggfunc="sum")
            data_cns = data_cns.reset_index(level=0)
            data = pd.merge(data, data_cns, on=pivot_lvl_col)
        return data

    def _filter_hierharchy_by_level(self, level):
        var_hierarchy = {}
        var_hierarchy['geometry'] = self.var_hierarchy['geometry']
        var_hierarchy['censo'] = self.var_hierarchy['censo']
        pivot_lvl = self.levels-level
        var_hierarchy['codes'] = self.var_hierarchy['codes'][pivot_lvl:]
        var_hierarchy['names'] = self.var_hierarchy['names'][pivot_lvl:]
        return var_hierarchy

    def filter_data_by_level(self, level, outer=False, raw=False):
        data_censo = self._filter_censo_by_level(level, outer)
        var_hierarchy = self._filter_hierharchy_by_level(level)
        if raw:
            return data_censo, var_hierarchy
        else:
            return self._data_reduction(data_censo, var_hierarchy)


class Votations(object):
    """Votations data. The data of the results of votes by party in columns.
    Each columns has a party and some codes. The result is the votes.

    """

    def __init__(self, votes, var_info, collapse_ways):
        self._check_inputs(votes, var_info, collapse_ways)
        self.collapses = collapse_ways
        self.var_info = var_info
        self.votes = votes

    def _check_inputs(self, votes, var_info, collapse_ways):
        assert('codes' in var_info)
        assert('parties' in var_info)
        assert(isinstance(var_info['parties'], list))
        assert(isinstance(var_info['codes'], list))
        assert(isinstance(collapse_ways, dict))
        for w, ps in collapse_ways.items():
            assert(all([p in var_info['parties'] for p in ps]))

    def get_results(self, code, collapse_way=None):
        if collapse_way is None:
            collapsing = dict(zip(self.var_info['parties'],
                                  self.var_info['parties']))
        else:
            collapsing = self.collapses[collapse_way]
        votes_collapse = self.votes[[code]]
        for group, parties in collapsing.items():
            votes_collapse[group] = self.votes[parties].sum(1)
        votes = votes_collapse.dissolve(by=code, aggfunc='sum')
        votes = votes.reset_index(level=0)
        return votes
