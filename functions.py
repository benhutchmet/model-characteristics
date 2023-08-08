# Functions for the notebook

# Local imports
import os
import sys
import glob
import re

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
def get_institution(model, base_path, variable):
    # institution name is the 6th element in the path
    # which is formed as:
    # base_path + / + institution + / + model
    # e.g. /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1

    # form the path
    path = base_path + "/*/" + model

    # find the directory which matches the path
    dirs = glob.glob(path)

    # if the dirs list is empty
    # then the variable is not available
    if len(dirs) == 0:
        print("Model not available")
        return None

    # split the path to get the institution name
    institution = dirs[0].split("/")[6]

    # #print the institution name
    #print("Institution: ", institution)

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

        # #print the experiment name
        #print("Experiment: ", experiment)

        return experiment
    except:
        #print("Experiment not found")
        return None
    

# Define a function to get the number of runs for a given model
# and experiment
def get_runs(model, base_path, experiment):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*"

    # find the directory which matches the path
    dirs = glob.glob(path)

    # #print the directory which matches the path
    #print("Directory: ", dirs)

    # get the final element of the path
    # which is the r*i*p*f* directory
    final_dirs = [dirs.split("/")[-1] for dirs in dirs]

    # #print the final directories
    #print("Final directories: ", final_dirs)

    # extract the number of runs
    # as the substring between the characters 'r' and 'i'
    runs = len(set([final_dirs.split("r")[1].split("i")[0] for final_dirs in final_dirs]))

    # #print the number of runs
    #print("Number of runs: ", runs)

    return runs

# Define a similar function to get the number of initialisations
def get_inits(model, base_path, experiment):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # #print the directories which match the path
    #print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # #print the final directories
    #print("Final directories: ", final_dirs)

    # extract the number of unique initializations
    # as the substring between the characters 'i' and 'p'
    inits = len(set([fd.split("i")[1].split("p")[0] for fd in final_dirs]))

    # #print the number of initializations
    #print("Number of initializations: ", inits)

    return inits

# Define a function to get the number of physics ensembles
def get_physics(model, base_path, experiment):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # #print the directories which match the path
    #print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # #print the final directories
    #print("Final directories: ", final_dirs)

    # extract the number of unique physics forcings
    # as the substring between the characters 'p' and 'f'
    physics = len(set([fd.split("p")[1].split("f")[0] for fd in final_dirs]))

    # #print the number of physics forcings
    #print("Number of physics forcings: ", physics)

    return physics

# For the forcing
def get_forcing(model, base_path, experiment):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # #print the directories which match the path
    #print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # #print the final directories
    #print("Final directories: ", final_dirs)

    # extract the number of unique forcing scenarios
    # as the substring after the character 'f'
    forcing = len(set([fd.split("f")[-1] for fd in final_dirs]))

    # #print the number of forcing scenarios
    #print("Number of forcing scenarios: ", forcing)

    return forcing

# Define a function to get the total number of ensemble members
# this is the total number of directories which match the path
def get_total_ensemble_members(model, base_path, experiment):
    # form the path
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # #print the directories which match the path
    #print("Directories: ", dirs)

    # get the final element of each directory path
    final_dirs = [d.split("/")[-1] for d in dirs]

    # #print the final directories
    #print("Final directories: ", final_dirs)

    # extract the number of ensemble members
    ensemble_members = len(final_dirs)

    # #print the number of ensemble members
    #print("Number of ensemble members: ", ensemble_members)

    return ensemble_members

# Define a function to get the table_id
# such as Amon, Omon, SImon, day, fx, etc.
# check that the table_id is the same for all ensemble members
# function takes the model name and the base path and table_id = "Amon"
# and returns the table_id
def get_table_id(model, base_path, experiment, table_id):
    # Form the path
    # # /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*/" + table_id

    # find the directories which match the path
    dirs = glob.glob(path)

    # #print the first directory which matches the path
    #print("First directory: ", dirs)
    #print("no of directories: ", len(dirs))

    # if the dirs list is empty
    # then the variable is not available
    if len(dirs) == 0:
        print("Table_id not available for model: ", model + " and experiment: ", experiment)
        first_table_id = table_id + " not available"

    # Get the table_id from the path
    first_table_id = dirs[0].split("/")[-1]

    # #print the first table_id
    #print("First table_id: ", first_table_id)

    # Check that the table_id is the same for all ensemble members
    for d in dirs:
        if d.split("/")[-1] != first_table_id:
            #print("Table_id is not the same for all ensemble members")
            raise ValueError("Table_id is not the same for all ensemble members")
            return None
        
    # #print the table_id
    #print("Table_id: ", first_table_id)

    return first_table_id

# define a function to extract the years
# using different methods for different experiments
def get_years(model, base_path, experiment, table_id, variable):
    # Form the path
    if experiment == 'dcppA-hindcast':
        
        # set up the path
        path = base_path + "/*/" + model + "/" + experiment + "/s????-r*i*p*f*/" + table_id + "/" + variable + "/" + "g?" + "/" + "files" + "/" + "d*" + "/"

        # find the directories which match the path
        dirs = glob.glob(path)

        # Check that the list of directories is not empty
        if len(dirs) == 0:
            print("No files available")
            return None
        
        # extract the min and max years from the path
        # if the paths are /badc/cmip6/data/CMIP6/DCPP/NCC/NorCPM1/dcppA-hindcast/s1960-r1i1p1f1/Amon/rsds/gn/files/d* and /badc/cmip6/data/CMIP6/DCPP/NCC/NorCPM1/dcppA-hindcast/s1970-r1i1p1f1/Amon/rsds/gn/files/d*
        # then the min and max years are 1960 and 1970
        # first extract the s????-r*i*p*f* directory from the path
        # which is the fifth from last element
        # e.g. s1960-r1i1p1f1
        years_init_dirs = [dirs.split("/")[-7] for dirs in dirs]
        # print("years_init_dirs: ", years_init_dirs)

        # extract the min and max years from the years_init_dirs
        # as the substring between the characters 's' and 'r'
        years = [years_init_dirs.split("s")[1].split("r")[0] for years_init_dirs in years_init_dirs]
        # ensure that each element in the years list is an integer
        # currently 1960-
        # get rid of the -
        years = [years.split("-")[0] for years in years] 
        # print("years: ", years)

        # find the min and max years
        min_year = min(years)
        max_year = max(years)

        # form the range of years
        # e.g 1960-1970
        years_range = min_year + "-" + max_year

    elif experiment == 'historical':
        # get the list of files in the final directory
        files_list = get_files(model, base_path, experiment, table_id, variable)
        # Check that the list of files is not empty
        if len(files_list) == 0:
            print("No files available")
            years_range = "No files"
            return years_range
        # extract the years from the filenames
        # these will be in the format: psl_Amon_BCC-CSM2-MR_historical_r1i1p1f1_gn_185001-201412.nc
        min_year = re.findall(r'\d{4}', files_list[0])[0]
        max_year = re.findall(r'\d{4}', files_list[0])[1]

        # form the range of years
        # e.g 1850-2014
        years_range = min_year + "-" + max_year
    else:
        print("Experiment not recognized")
        return None
    # return the list of years
    return years_range    


# Define a function to get the variable name
# such as psl, tas, tos, rsds, sfcWind, etc.
# check that the variable is the same for all ensemble members
# function takes the model name and the base path and the experiment name and table_id and variable name
# and returns the variable name
def get_variable(model, base_path, experiment, table_id, variable):
    # Form the path
    # based on /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*/" + table_id + "/" + variable

    # path for the runs directory
    path_runs_dir = base_path + "/*/" + model + "/" + experiment + "/r*i*p*f*"

    # find the directories which match the path
    dirs = glob.glob(path)

    # if the dirs list is empty
    # then the variable is not available
    if len(dirs) == 0:
        #print("Variable not available")

        # Set up output for variable not available
        first_variable = variable
        no_members = 0
        members_list = []
        return first_variable, no_members, members_list

    # find the directories which match the path for the runs directory
    dirs_runs_dir = glob.glob(path_runs_dir)

    # #print the directories which match the path
    #print("Directories: ", dirs)

    # set the number of members available
    # i.e. the number of directories which match the path
    no_members = len(dirs)
    #print("Number of members: ", no_members)

    # extract the r*i*p*f* directory from the path
    # which is the third from last element
    # e.g. r1i1p1f1
    members_list = [dirs.split("/")[-3] for dirs in dirs]
    #print("Members list: ", members_list)

    # Get the variable name from the first directory
    first_variable = dirs[0].split("/")[-1]

    # #print the first variable
    #print("First variable: ", first_variable)

    # Check whether the lens of the dirs for the runs directory is the same as the lens of the dirs for the variable
    if len(dirs_runs_dir) != len(dirs):
        print("Not all runs are available for the variable")
        print("Number of runs available for the runs directory: ", len(dirs_runs_dir))
        print("Number of runs available for the variable: ", len(dirs))

    # #print the variable
    #print("Variable: ", first_variable)

    return first_variable, no_members, members_list

# Define a function to get the list of files for a given model, experiment, table_id, variable
# in the final directory
def get_files(model, base_path, experiment, table_id, variable):
    # Form the path
    path = base_path + "/*/" + model + "/" + experiment + "/*r*i*p*f*/" + table_id + "/" + variable + "/" + "g?" + "/" + "files" + "/" + "d*" + "/"
    print("Path: ", path)

    # find the directories which match the path
    dirs = glob.glob(path)

    # Check that the list of directories is not empty
    if len(dirs) == 0:
        print("No files available")
        files_list = []
        return files_list
    
    # # print the directories which match the path
    # print("Directories: ", dirs)

    # get a list of the files in the final directory
    files_list = []
    for d in dirs:
        files_list.extend(glob.glob(os.path.join(d, "*")))

    # # print the files in the final directory
    # print("Files list: ", files_list)

    # extract the final element following the last "/"
    # from each file in the files_list
    files_list = [f.split("/")[-1] for f in files_list]

    # # print the files in the final directory
    # print("Files list final dir: ", files_list)

    return files_list

# Define a function to fill in the dataframe
def fill_dataframe(models, variables, columns, experiments, table_ids):
    # create an empty dataframe with the desired columns
    df = pd.DataFrame(columns=columns)

    # create a dictionary to map column names to functions
    column_functions = {
        "institution": lambda table_id, experiment, model, base_path, variable: get_institution(model, base_path, variable),
        "source": lambda table_id, experiment, model, base_path, variable: model,
        "experiment": lambda table_id, experiment, model, base_path, variable: experiment,
        "table_id": lambda table_id, experiment, model, base_path, variable: get_table_id(model, base_path, experiment=experiment, table_id=table_id),
        "runs": lambda table_id, experiment, model, base_path, variable: get_runs(model, base_path, experiment=experiment),
        "inits": lambda table_id, experiment, model, base_path, variable: get_inits(model, base_path, experiment=experiment),
        "physics": lambda table_id, experiment, model, base_path, variable: get_physics(model, base_path, experiment=experiment),
        "forcing": lambda table_id, experiment, model, base_path, variable: get_forcing(model, base_path, experiment=experiment),
        "total ensemble members": lambda table_id, experiment, model, base_path, variable: get_total_ensemble_members(model, base_path, experiment=experiment),
        "no_members": lambda table_id, experiment, model, base_path, variable: get_variable(model, base_path, experiment=experiment, table_id=table_id, variable=variable)[1],
        "members_list": lambda table_id, experiment, model, base_path, variable: get_variable(model, base_path, experiment=experiment, table_id=table_id, variable=variable)[2],
        "variable": lambda table_id, experiment, model, base_path, variable: get_variable(model, base_path, experiment=experiment, table_id=table_id, variable=variable)[0],
        "model": lambda table_id, experiment, model, base_path, variable: model,
        "files_list": lambda table_id, experiment, model, base_path, variable: get_files(model, base_path, experiment=experiment, table_id=table_id, variable=variable),
        "years_range": lambda table_id, experiment, model, base_path, variable: get_years(model, base_path, experiment=experiment, table_id=table_id, variable=variable)
    }


    # iterate over the list of table ids
    for table_id in table_ids:
        # Print the table_id which is being processed
        print("Table_id: ", table_id)

        # iterate over the experiments and variables
        for experiment in experiments:
            # Print the experiment which is being processed
            print("Experiment: ", experiment)

            # Set the base path
            if experiment == "historical":
                base_path = "/badc/cmip6/data/CMIP6/CMIP"
            elif experiment == "dcppA-hindcast":
                base_path = "/badc/cmip6/data/CMIP6/DCPP"
            else:
                print("Experiment not recognized")
                return None
            
            # iterate over the models and variables
            for model in models:

                # Print the model which is being processed
                print("Model: ", model)

                for variable in variables:

                    # Print the variable which is being processed
                    print("Variable: ", variable)
                    # create a dictionary to hold the values for this combination of model and variable
                    row_dict = {}

                    # iterate over the columns and add the values to the dictionary
                    for column in columns:
                        # get the function corresponding to the column name
                        column_function = column_functions[column]

                        # call the function to get the value for the current model, variable, and column and experiment
                        value = column_function(table_id, table_id, experiment, model, base_path, variable)

                        # add the column value to the dictionary
                        row_dict[column] = value

                    # append the row dictionary to the dataframe as a new row
                    df = df.append(row_dict, ignore_index=True)

    return df