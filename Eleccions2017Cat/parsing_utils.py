# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def parse_eleccions_2015_csv(elections2015_csv):
    """
    """
    converters = {}
    data2015 = pd.read_csv(elections2015_csv, sep=';', converters=converters)

    columns = ['Codi Província', 'Nom Província', 'Codi Vegueria',
               'Nom Vegueria', 'Codi Comarca', 'Nom Comarca', 'Codi Municipi',
               'Nom Municipi', 'Districte', 'Secció', 'Mesa', 'Cens electoral',
               'Participació 13:00', 'Participació 18.00',
               'Participació 20.00', 'Abstenció', 'Vots nuls', 'Vots en blanc',
               'Vots a candidatures', 'Vots vàlids']
    n_cols = len(columns)
    cols_new = [str(c) for c in data2015.columns]
    data2015.columns = cols_new

    party_col = [2*i for i in range((len(data2015.columns)-len(columns))//2)]
    votos = data2015.columns[len(columns):][party_col]
    parties = ["PSC", "PP", "C's", "PACMA", "JxSi", "CSQEP", "unio.cat", "CUP",
               "RECORTES0", "pirata.cat", "ganemos"]
    votos_data2015 = data2015[votos]
    votos_data2015.columns = parties

    # Votos de 2015
    # data2015[data2015.columns[:20]]
    CUSEC =\
        [str(data2015.iloc[i, 6]).zfill(5)+str(data2015.iloc[i, 8]).zfill(2) +
         str(data2015.iloc[i, 9]).zfill(3) for i in range(len(data2015))]
    CUSEC2015 = pd.DataFrame(pd.Series(CUSEC), columns=['CUSEC'])
    votos2015 = pd.concat([CUSEC2015, votos_data2015], axis=1)

    # Data information 2015
    data_info2015 = data2015.iloc[:, :20]
    data_info2015 = pd.concat([data_info2015, CUSEC2015], axis=1)

    return data_info2015, votos2015


def collapse_votes(votos):
    df = []
    u_cusec = votos['CUSEC'].unique()
    for cusec_i in u_cusec:
        df.append(votos.loc[(votos['CUSEC'] == cusec_i), :].iloc[:, 1:].sum(0))
    votos = pd.concat([pd.DataFrame(u_cusec, columns=['CUSEC']),
                       pd.DataFrame(df)], axis=1)
    return votos


def collapse_info_mesas(data_info):
    data_info_codes = data_info.iloc[:, :10]
    data_info_censo = data_info.iloc[:, 11:20]
    codes_columns = list(data_info_codes.columns)
    censo_columns = list(data_info_censo.columns)

    df_codes = []
    df_censo = []
    u_cusec = data_info['CUSEC'].unique()
    for cusec_i in u_cusec:
        idxs = np.where(data_info['CUSEC'] == cusec_i)[0]
        idx = idxs[0]
        df_codes.append(list(data_info_codes.iloc[idx, :]))
        df_censo.append(data_info_censo.iloc[idxs, :].sum(0))
    data_info = pd.concat([pd.DataFrame(u_cusec, columns=['CUSEC']),
                           pd.DataFrame(df_codes, columns=codes_columns),
                           pd.DataFrame(df_censo, columns=censo_columns)],
                          axis=1)
    return data_info


def left_filter_function(filter_data, to_filter_data, filter_code):
    assert(filter_code in list(filter_data.columns))
    assert(filter_code in list(to_filter_data.columns))

    def to_str(x):
        return str(x)
    filter_data[filter_code] = filter_data[filter_code].apply(to_str)
    to_filter_data[filter_code] = to_filter_data[filter_code].apply(to_str)
    codes_filter = set(filter_data[filter_code].unique())
    codes2filter = set(to_filter_data[filter_code].unique())
    codes_not_in2filter = codes_filter - codes2filter
    codes_not_in_filter = codes2filter - codes_filter
    codes = codes2filter & codes_filter

    df_filter = []
    df2filter = []
    for u_c in codes:
        aux = filter_data.loc[filter_data[filter_code] == str(u_c), :]
        df_filter.append(aux)
        aux = to_filter_data.loc[to_filter_data[filter_code] == str(u_c), :]
        df2filter.append(aux)
    df_filter = pd.DataFrame(df_filter)
    df2filter = pd.DataFrame(df2filter)
    df_filter = pd.DataFrame(df_filter, columns=list(filter_data.columns))
    df2filter = pd.DataFrame(df2filter, columns=list(to_filter_data.columns))
    out_data = pd.merge(df_filter, df2filter, how='left', on=filter_code)
    return out_data, codes_not_in_filter, codes_not_in2filter
