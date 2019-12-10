import sys, os, gc, json, pickle
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

from collections import defaultdict

# Replace these paths with your own absolute paths
data_path = '../../data/'

# Evaluation Metrics
def overlap_score(tracks, pred_tracks, test_size = 10):
    ''' Computes the overlap score for tracks and pred_tracks. 
        returns #overlap'''
    assert len(tracks) == len(pred_tracks) == test_size
    return sum([a in tracks for a in pred_tracks])

def avg_overlap(true_dict, pred):
    ''' Returns the accuracy score given true_label and pred'''
    assert len(true_dict) == len(pred)
    avg_overlap = np.mean([overlap_score(a, b) for a,b in zip(true_dict.values(), pred)])    
    return avg_overlap

def r_precision(predictions, labels, test_size = 10):
    ''' Calculates the r-precision score
        Inputs:
            Prediction: list of predictions 
            labels: list of actual labels
            test_size: size of each of the two sets
    '''
    assert len(predictions) == len(labels) == test_size
    score = len(np.intersect1d(labels, predictions)) / len(labels)
    return score

def dcg(predictions, labels, test_size = 10):
    ''' Calculates the discounted cumulative gain for prediction and labels. 
        Inputs:
            Prediction: list of predictions 
            labels: list of actual labels
            test_size: size of each of the two sets'''
    assert len(predictions) == len(labels) == test_size
    zero_one_label = [predictions[i] in labels for i in range(len(predictions))]
    zero_one_label = [zero_one_label[i]/np.log2(i+2) for i in range(len(zero_one_label))]
    return np.sum(zero_one_label)






