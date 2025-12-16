import numpy as np
from scipy import stats

def calculate_basics(data):
    n = len(data)
    mean_val = np.mean(data)
    variance = np.var(data, ddof=1)
    std_dev = np.std(data, ddof=1)
    std_error = std_dev / np.sqrt(n)
    return mean_val, variance, std_dev, std_error

def get_student_coef(n, confidence):
    return stats.t.ppf((1 + confidence) / 2, df=n-1)

def get_confidence_interval(mean_val, std_error, n, confidence):
    t_val = get_student_coef(n, confidence)
    delta = std_error * t_val
    return delta, t_val

def calculate_correlation(x, y):
    x = np.array(x)
    y = np.array(y)
    r = np.corrcoef(x, y)[0, 1]
    return r

def gaussian_func(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)