#!/usr/bin/env python

from db_table import *
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()

# Add a positional argument for the filename
parser.add_argument('column')
parser.add_argument('value')

# Parse the command line arguments
args = parser.parse_args()

column = args.column
value = args.value

print(column)
print(value)