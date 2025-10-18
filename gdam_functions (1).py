"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math
import numpy as np

# Define your new functions below
def mean(data):
    return sum(data)/len(data)

def standard_deviation (data):
    m=mean(data)
    return (sum((x - m) ** 2 for x in data) / len(data)) ** 0.5

def standard_error(data):
    return standard_deviation (data)/len(data) **0.5

def gaussian(x,mean,std_dev):
    return(1/(std_dev*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mean)/std_dev)**2)


