import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from datetime import datetime
import time

from scipy.stats import chi2_contingency, ttest_ind ,chisquare, kruskal, pearsonr


def dateparse(time_in_secs):
    return pd.to_datetime(time_in_secs, unit='s')

def load_csv():
    
    fields = ['app_name','language','timestamp_created', 'timestamp_updated', 'recommended',
              'votes_helpful', 'votes_funny', 'weighted_vote_score','steam_purchase',
              'received_for_free','author.steamid']
    
    dataset = pd.read_csv('steam_reviews.csv', header='infer',
                            usecols = fields,
                            parse_dates=['timestamp_created',
                            'timestamp_updated'],
                            date_parser=dateparse)
    return dataset

    
def custom_time_intervals():
    intervals = [
    ( datetime.strptime('06:00:00', "%H:%M:%S"), datetime.strptime('10:59:59', "%H:%M:%S") ),
    ( datetime.strptime('11:00:00', "%H:%M:%S"), datetime.strptime('16:59:59', "%H:%M:%S") ),
    ( datetime.strptime('14:00:00', "%H:%M:%S"), datetime.strptime('16:59:59', "%H:%M:%S") ), 
    ( datetime.strptime('17:00:00', "%H:%M:%S"), datetime.strptime('19:59:59', "%H:%M:%S") ),
    ( datetime.strptime('20:00:00', "%H:%M:%S"), datetime.strptime('23:59:59', "%H:%M:%S") ),
    ( datetime.strptime('00:00:00', "%H:%M:%S"), datetime.strptime('02:59:59', "%H:%M:%S") ),
    ( datetime.strptime('03:00:00', "%H:%M:%S"), datetime.strptime('05:59:59', "%H:%M:%S") )]
    
    return intervals



def filter_by_language(my_dataset, language_list):
    new_dataset = my_dataset[my_dataset['language'].isin(language_list)]
    return new_dataset


def funny_percentage(dataset):
    num_funny_votes = dataset[dataset['votes_funny'] != 0].shape[0]
    num_total_entries = dataset.shape[0]
    my_percentage = num_funny_votes / num_total_entries
    return(my_percentage)


def helpful_percentage(dataset):
    num_helpful_votes = dataset[dataset['votes_helpful'] != 0].shape[0]
    num_total_entries = dataset.shape[0]
    my_percentage = num_helpful_votes / num_total_entries
    return(my_percentage)


def received_for_free_percentage(dataset):
    num_frees = dataset[dataset['received_for_free'] == True].shape[0]
    num_total_entries = dataset.shape[0]
    my_percentage = num_frees / num_total_entries
    return(my_percentage)


def steam_purchase_percentage(dataset):
    num_purchases = dataset[dataset['steam_purchase'] == True].shape[0]
    num_total_entries = dataset.shape[0]
    my_percentage = num_purchases / num_total_entries
    return(my_percentage)


def plot_percentage(percentage, my_title = ''):
    labels = 'True', 'False'
    sizes = [100*percentage, 100 - 100*percentage]
    explode = (0.1, 0)
    fig1, ax1 = plt.subplots()
    plt.title(my_title)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')
    
    
def plot_and_count(dataset, percentage, column, xlabel = '', my_title = '', ylabel = 'Number of Revies'):
    labels = 'True', 'False'
    sizes = [100*percentage, 100 - 100*percentage]
    explode = (0.1, 0)
    plt.subplot(131)
    plt.title(my_title)
    pie = plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.subplot(133)
    dataset[column].value_counts().plot.bar(title = my_title, xlabel = xlabel, ylabel = ylabel)
    

def weighted_vote_score_percentage(dataset, threshold = 0.5):
        new_ds = dataset[dataset['weighted_vote_score'] > threshold]
        my_percentage = new_ds.shape[0] / dataset.shape[0]
        return(my_percentage)
    
    
def funny_vote_given_score(dataset, threshold = 0.5):
    new_ds = dataset[dataset['weighted_vote_score'] > threshold]
    return(funny_percentage(new_ds))

