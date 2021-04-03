#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:49:00 2021

@author: sumeetsarode
"""

import sys
import pandas as pd
import os

def csv_combiner(filenames):
    
    # Check if filenames are given
    if not filenames: return None
    
    for filename in filenames:
        
        # Checking if file exists
        if not os.path.exists(filename): raise IOError('File Not Found Error: No such file')
        
        # Checking for "csv" extension
        if not filename.endswith('.csv'): raise Exception('Not a valid CSV file.')
    
    init_cols = None
    for filename in filenames:
        
        cols = list(pd.read_csv(filename, nrows=1).columns) + ['filename']
        if not init_cols:

            # Adding columns in the output file
            print(','.join(cols))

            init_cols = set(cols)

        # Checking if columns are same as initial file
        elif init_cols != set(cols): raise Exception('Columns are not same')

        # Reading the csv file in chunks to avoid memory error
        chunk_size = 64000
        for chunk in pd.read_csv(filename, chunksize=chunk_size, low_memory=False):

            # Creating the "filename" column
            chunk['filename'] = filename.split('/')[-1]
            
            print(chunk.to_csv(header=False, index=None, chunksize=chunk_size))

# Main Function
def main():
    filenames = sys.argv[1:]
   
    csv_combiner(filenames)
    
if __name__ == '__main__': main()
