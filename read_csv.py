import numpy as np

def read_csv05(path):
    with open(path, encoding='utf-8-sig') as f:
        data = np.loadtxt(f, str, delimiter=',', skiprows=0)
    data = data.astype('float64')
    data = data.T
    return data

def read_csv10(path):
    with open(path, encoding='utf-8-sig') as f:
        data = np.loadtxt(f, str, delimiter=',', skiprows=0)
    data = data.astype('float64')
    data = data.T
    return data

def read_csv20(path):
    with open(path, encoding='utf-8-sig') as f:
        data = np.loadtxt(f, str, delimiter=',', skiprows=0)
    data = data.astype('float64')
    data = data.T
    return data