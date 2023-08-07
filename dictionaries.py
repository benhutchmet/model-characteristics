# Dictionaries used in the functions.py file and the model_charac.ipynb notebook

canari_dir = "/gws/nopw/j04/canari/users/benhutch/"

models = [ "BCC-CSM2-MR", "MPI-ESM1-2-HR", "CanESM5", "CMCC-CM2-SR5", "HadGEM3-GC31-MM", "EC-Earth3", "MPI-ESM1-2-LR", "FGOALS-f3-L", "MIROC6", "IPSL-CM6A-LR", "CESM1-1-CAM5-CMIP5", "NorCPM1" ]

variables = [ "psl", "tas", "tos", "rsds", "sfcWind" ]

# data on JASMIN path
# /badc/cmip6/data/CMIP6/CMIP/NCC/NorCPM1/historical/r1i1p1f1/Amon/psl/gn/files/d20190914
base_JASMIN_dir = "/badc/cmip6/data/CMIP6/CMIP"

columns = ['institution', 'source', 'experiment', 'runs', 'inits', 'physics', 'forcing', 'total ensemble members', 'table_id', 'variable', 'grid', 'version', 'path']

experiment = "historical"

table_id = "Amon"