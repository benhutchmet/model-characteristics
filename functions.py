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

# JASMIN dir
# for historical data
# # data on JASMIN path
# /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914

# Set up dataframe with columns specified in dictionaries.py
def setup_dataframe(columns):
    # create an empty pandas dataframe with the specified columns
    df = pd.DataFrame(columns=columns)
    
    return df

# Function to get the institution name from the path
# for a given model
# function takes the model name and the base path
# and returns the institution name
def get_institution(model, base_path):
    # institution name is the 6th element in the path
    # which is formed as:
    # base_path + / + institution + / + model
    # e.g. /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1

    # form the path
    path = base_path + "/*/" + model

    # find the directory which matches the path
    dirs = glob.glob(path)

    # split the path to get the institution name
    institution = dirs[0].split("/")[6]

    # print the institution name
    print("Institution: ", institution)

    return institution

# function to check whether experiment 'historical' exists
# for a given model
# function takes the model name and the base path
# and returns the experiment name
def check_experiment(model, base_path, experiment="historical"):
    # use a try/except block to check whether the experiment exists
    try:
        # form the path
        path = base_path + "/*/" + model + "/" + experiment

        # find the directory which matches the path
        dirs = glob.glob(path)

        # split the path to get the experiment name
        experiment = dirs[0].split("/")[8]

        # print the experiment name
        print("Experiment: ", experiment)

        return experiment
    except:
        print("Experiment not found")
        return None
    

# Define a function to get the number of runs for a given model
# and experiment
def get_runs(model, base_path, experiment="historical"):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directory which matches the path
    dirs = glob.glob(path)

    # print the directory which matches the path
    print("Directory: ", dirs)

    # get the final element of the path
    # which is the r*i*p*f* directory
    final_dirs = [dirs.split("/")[-1] for dirs in dirs]

    # print the final directories
    print("Final directories: ", final_dirs)

    # extract the number of runs
    # as the substring between the characters 'r' and 'i'
    runs = len(set([final_dirs.split("r")[1].split("i")[0] for final_dirs in final_dirs]))

    # print the number of runs
    print("Number of runs: ", runs)

    return runs

# Define a similar function to get the number of initialisations
def get_inits(model, base_path, experiment="historical"):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # print the directories which match the path
    print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # print the final directories
    print("Final directories: ", final_dirs)

    # extract the number of unique initializations
    # as the substring between the characters 'i' and 'p'
    inits = len(set([fd.split("i")[1].split("p")[0] for fd in final_dirs]))

    # print the number of initializations
    print("Number of initializations: ", inits)

    return inits

# Define a function to get the number of physics ensembles
def get_physics(model, base_path, experiment="historical"):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # print the directories which match the path
    print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # print the final directories
    print("Final directories: ", final_dirs)

    # extract the number of unique physics forcings
    # as the substring between the characters 'p' and 'f'
    physics = len(set([fd.split("p")[1].split("f")[0] for fd in final_dirs]))

    # print the number of physics forcings
    print("Number of physics forcings: ", physics)

    return physics

# For the forcing
def get_forcing(model, base_path, experiment="historical"):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # print the directories which match the path
    print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # print the final directories
    print("Final directories: ", final_dirs)

    # extract the number of unique forcing scenarios
    # as the substring after the character 'f'
    forcing = len(set([fd.split("f")[-1] for fd in final_dirs]))

    # print the number of forcing scenarios
    print("Number of forcing scenarios: ", forcing)

    return forcing

# Define a function to get the total number of ensemble members
# this is the total number of directories which match the path
def get_total_ensemble_members(model, base_path, experiment="historical"):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # print the directories which match the path
    print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # print the final directories
    print("Final directories: ", final_dirs)

    # extract the number of ensemble members
    ensemble_members = len(final_dirs)

    # print the number of ensemble members
    print("Number of ensemble members: ", ensemble_members)

    return ensemble_members