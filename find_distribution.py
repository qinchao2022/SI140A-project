from scipy.stats import kstest
from scipy.stats import ks_2samp
from scipy.stats import entropy
import numpy as np

def compute_cdf(data):
    len = data.size
    cdf = np.zeros(len)
    cdf[0] = data[0]
    for i in range(1, len):
        cdf[i] += cdf[i-1] + data[i]
    return cdf

def compute_loss(data1, data2):
    return np.sum(np.square(data1 - data2))

def ks_compare(data1, data2):
    return ks_2samp(data1, data2).pvalue > ks_2samp(data1, data2).statistic

def ks_2(data1, data2):
    return ks_2samp(data1, data2)

def KL_divergence(data1, data2):
    return entropy(data1, data2)