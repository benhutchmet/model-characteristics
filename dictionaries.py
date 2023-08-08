    # Dictionaries used in the functions.py file and the model_charac.ipynb notebook

# example canari pattern = /gws/nopw/j04/canari/users/benhutch/historical/data/psl/BCC-CSM2-MR
canari_dir = "/gws/nopw/j04/canari/users/benhutch/"


models = [ "BCC-CSM2-MR", "MPI-ESM1-2-HR", "CanESM5", "CMCC-CM2-SR5", "HadGEM3-GC31-MM", "EC-Earth3", "MPI-ESM1-2-LR", "FGOALS-f3-L", "MIROC6", "IPSL-CM6A-LR", "CESM1-1-CAM5-CMIP5", "NorCPM1" ]

historical_models = [ "BCC-CSM2-MR", "MPI-ESM1-2-HR", "CanESM5", "CMCC-CM2-SR5", "HadGEM3-GC31-MM", "EC-Earth3", "MPI-ESM1-2-LR", "FGOALS-f3-L", "MIROC6", "IPSL-CM6A-LR", "NorCPM1" ]

variables = [ "psl", "tas", "tos", "rsds", "sfcWind" ]

# data on JASMIN path
# /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914
# example for dcppA-hindcast data: /badc/cmip6/data/CMIP6/DCPP/NCC/NorCPM1/dcppA-hindcast/s1970-r1i1p1f1/Amon/rsds/gn/files/d20190914
base_JASMIN_dir_cmip = "/badc/cmip6/data/CMIP6/CMIP"

base_JASMIN_dir_dcpp = "/badc/cmip6/data/CMIP6/DCPP"

columns = [ 'institution', 'source', 'experiment', 'runs', 'inits', 'physics', 'forcing', 'total ensemble members', 'no_members', 'members_list', 'variable', 'model', 'files_list', 'years_range' ]

experiment_hist = "historical"

experiment_dccp = "dcppA-hindcast"

experiments = [ "historical", "dcppA-hindcast" ]

table_id = "Amon"

table_ids = [ "Amon", "day", "6hr" ]

test_variable = "psl"

test_model = [ "BCC-CSM2-MR", "MPI-ESM1-2-HR" ]

test_model_can = [ "CanESM5" ]

test_model_cmcc = [ "CMCC-CM2-SR5" ]

test_model_hadgem = [ "HadGEM3-GC31-MM" ]

test_models_nocan = [ "BCC-CSM2-MR", "MPI-ESM1-2-HR", "CMCC-CM2-SR5", "HadGEM3-GC31-MM", "EC-Earth3", "MPI-ESM1-2-LR", "FGOALS-f3-L", "MIROC6", "IPSL-CM6A-LR", "NorCPM1" ]