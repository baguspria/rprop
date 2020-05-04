#imports
import numpy as np
import pandas as pd

#returns df of selected col indexes from csv
def fetch_data(dir, filenames, col_idx):
    return pd.concat([pd.read_csv(dir+file, usecols=col_idx) for file in filenames])

#returns zip of min and max longitudes & latitudes
def grid_num(lats, longs, x_grids, y_grids):
    #calc length and width of one grid
    length = (np.max(lats)-np.min(lats)) / y_grids
    width = (np.max(longs)-np.min(longs)) / x_grids

    #create a list of lats&longs with calculated steps
    lat_grids = [i for i in np.arange(np.min(lats), np.max(lats)+1, length)]
    long_grids = [i for i in np.arange(np.min(longs), np.max(longs)+1, width)]

    #create zip of min-max for each longs&lats
    lat_grids = np.array(list(zip(lat_grids, lat_grids[1:])))
    long_grids = np.array(list(zip(long_grids, long_grids[1:])))
    lat_grids[1:,0] = lat_grids[1:,0] + 0.001
    long_grids[1:,0] = long_grids[1:,0] + 0.001
    
    #create zip of longs-lats
    return [(i, j) for i in lat_grids for j in long_grids]


#---------------------M A I N-----------------------#

dir = 'USGS datasets/'
filenames = ['2000-2005.csv', '2006-2013.csv', '2014-2019.csv']
col_idx = [0,1,2,4]

data = fetch_data(dir, filenames, col_idx)


