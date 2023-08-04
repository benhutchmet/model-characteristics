# Functions for the notebook

# Local imports
import os
import sys
import glob

# Third-party imports
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def setup_dataframe(variable):
    # create a dictionary with the column names as keys and empty lists as values
    data = {'experiment': [], 'time period': [], 'runs': [], 'initialization': []}
    
    # add data to the dictionary
    data['experiment'] = ['experiment1', 'experiment2', 'experiment3']
    data['time period'] = ['period1', 'period2', 'period3']
    data['runs'] = [1, 2, 3]
    data['initialization'] = ['init1', 'init2', 'init3']
    
    # create a pandas dataframe from the dictionary
    df = pd.DataFrame(data)
    
    # add the variable column to the dataframe
    df['variable'] = variable
    
    return df