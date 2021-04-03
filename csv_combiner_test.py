#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:56:42 2021

@author: sumeetsarode
"""

import unittest
from io import StringIO
import pandas as pd
from csv_combiner import csv_combiner
import sys

class test(unittest.TestCase):
    
    # Checking output for empty file list
    def test_empty_file_list(self):
        self.assertIsNone(csv_combiner([]))

    # Checking if file exists
    def test_file_not_found(self):
        with self.assertRaises(Exception) as context:
            csv_combiner(['./fixtures/accessories.csv', './fixtures/clothing1.csv'])
            self.assertEqual('File Not Found Error: No such file', str(context.exception))

    # Checking for "csv" extension
    def test_invalid_extension(self):

        with self.assertRaises(Exception) as context:
            csv_combiner(['./fixtures/accessories.csv', './fixtures/clothing'])
            self.assertEqual('Not a valid CSV file.', str(context.exception))

    # Checking if columns are same as initial file
    def test_same_columns(self):

        with self.assertRaises(Exception) as context:
            csv_combiner(['./fixtures/accessories.csv', './fixtures/clothing.csv'])
            self.assertEqual('Columns are not same', str(context.exception))

    # Checking if filename column is added in the output file
    def test_filename_column_added(self):
        
        output = StringIO()
        sys.stdout = output
        csv_combiner(['./fixtures/accessories.csv', './fixtures/clothing.csv'])

        test_output = open('test_output.csv', 'w+')
        test_output.write(output.getvalue())
        test_output.close()
    
        self.assertIn('filename', pd.read_csv('test_output.csv', nrows = 1).columns.values)

if __name__ == '__main__':
    unittest.main()