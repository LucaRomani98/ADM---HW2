import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import datetime as dt
import time

from scipy.stats import chi2_contingency, ttest_ind ,chisquare, kruskal, pearsonr

def dateparse(time_in_secs):
    return pd.to_datetime(time_in_secs, unit='s')

def load_csv():
    dataset = pd.read_csv('steam_reviews.csv', header='infer', nrows = 1000000,
    parse_dates=['timestamp_created',
    'timestamp_updated', 'author.last_played'],
    date_parser=dateparse)
    return dataset