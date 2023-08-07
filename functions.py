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

# Define a function to get the table_id
# such as Amon, Omon, SImon, day, fx, etc.
# check that the table_id is the same for all ensemble members
# function takes the model name and the base path and table_id = "Amon"
# and returns the table_id
def get_table_id(model, base_path, experiment="historical", table_id="Amon"):
    # Form the path
    # # /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*/" + table_id

    # find the directories which match the path
    dirs = glob.glob(path)

    # print the first directory which matches the path
    print("First directory: ", dirs)
    print("no of directories: ", len(dirs))

    # Get the table_id from the path
    first_table_id = dirs[0].split("/")[-1]

    # print the first table_id
    print("First table_id: ", first_table_id)

    # Check that the table_id is the same for all ensemble members
    for d in dirs:
        if d.split("/")[-1] != first_table_id:
            print("Table_id is not the same for all ensemble members")
            raise ValueError("Table_id is not the same for all ensemble members")
            return None
        
    # print the table_id
    print("Table_id: ", first_table_id)

    return first_table_id

# Define a function to get the variable name
# such as psl, tas, tos, rsds, sfcWind, etc.
# check that the variable is the same for all ensemble members
# function takes the model name and the base path and the experiment name and table_id and variable name
# and returns the variable name
def get_variable(model, base_path, experiment="historical", table_id="Amon", variable="psl"):
    # Form the path
    # based on /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914
    path = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*/" + table_id + "/" + variable

    # path for the runs directory
    path_runs_dir = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # find the directories which match the path for the runs directory
    dirs_runs_dir = glob.glob(path_runs_dir)

    # print the directories which match the path
    print("Directories: ", dirs)

    # set the number of members available
    # i.e. the number of directories which match the path
    no_members = len(dirs)
    print("Number of members: ", no_members)

    # extract the r*i*p*f* directory from the path
    # which is the third from last element
    # e.g. r1i1p1f1
    members_list = [dirs.split("/")[-3] for dirs in dirs]
    print("Members list: ", members_list)

    # Get the variable name from the first directory
    first_variable = dirs[0].split("/")[-1]

    # print the first variable
    print("First variable: ", first_variable)

    # Check whether the lens of the dirs for the runs directory is the same as the lens of the dirs for the variable
    if len(dirs_runs_dir) != len(dirs):
        print("Not all runs are available for the variable")
        print("Number of runs available for the runs directory: ", len(dirs_runs_dir))
        print("Number of runs available for the variable: ", len(dirs))

    # print the variable
    print("Variable: ", first_variable)

    return first_variable, no_members, members_list

# Define a function to fill in the dataframe
# function calls the functions above
# to set up the dataframe and fill in the columns
# function takes the list of models and the base path 
# and the experiment name and table_id and the list of variables
# and returns the dataframe
import pandas as pd
import glob

def fill_dataframe(models, base_path, columns, experiment="historical", table_id="Amon"):
    # create an empty dataframe with the desired columns
    df = pd.DataFrame(columns=columns)

    # create a dictionary to map column names to functions
    column_functions = {
        "institution": get_institution,
        "source": lambda model, base_path: model,
        "experiment": lambda model, base_path: experiment,
        "runs": lambda model, base_path: get_runs(model, base_path, experiment=experiment, table_id=table_id),
        "inits": lambda model, base_path: get_inits(model, base_path, experiment=experiment, table_id=table_id),
        "physics": lambda model, base_path: get_physics(model, base_path, experiment=experiment, table_id=table_id),
        "forcing": lambda model, base_path: get_forcing(model, base_path, experiment=experiment),
        "total ensemble members": lambda model, base_path: get_total_ensemble_members(model, base_path, experiment=experiment)
    }

    # iterate over the models and columns
    for model in models:
        for column in columns:
            # get the function corresponding to the column name
            column_function = column_functions[column]

            # call the function to get the value for the current model and column
            value = column_function(model, base_path)

            # add a row to the dataframe with the model and column value
            df = df.append({"Model": model, column: value}, ignore_index=True)

    return df