#!/usr/bin/env python

from db_table import *
import argparse
import xlrd

# Create an argument parser
parser = argparse.ArgumentParser()

# Add a positional argument for the filename
parser.add_argument('filename')

# Parse the command line arguments
args = parser.parse_args()

# Get the filename from the command line arguments
filename = args.filename


# Open agenda file
book = xlrd.open_workbook(filename)
sh = book.sheet_by_index(0)

# Get column names and clean them of unnecessary characters
raw_titles = sh.row(14)
clean_titles = []
for row in raw_titles:
    # Cleans titles of preceding "text:" and all "\\n"
    # Also added brackets so that white space and nonalphanumeric characters could be included
    clean_titles.append('[' + str(row).strip("'").split("'")[1].replace('\\n', '') + ']')

# Create Agenda table
agenda = db_table("Agenda", {clean_titles[0]: "text NOT NULL", 
                             clean_titles[1]: "text NOT NULL", 
                             clean_titles[2]: "text NOT NULL", 
                             clean_titles[3]: "text NOT NULL", 
                             clean_titles[4]: "text NOT NULL", 
                             clean_titles[5]: "text", 
                             clean_titles[6]: "text", 
                             clean_titles[7]: "text" })

# Cleans cells of preceding "text:" and changes <empty> cells to be empty strings
for row_num in range(15, sh.nrows):
    # Create list of data to hold data for one row
    data = []
    for cell in sh.row(row_num):
        data.append(str(cell).replace("text:", "").replace("'", "").replace("empty:", ""))

    # Insert row of data into Agenda table
    agenda.insert({ clean_titles[0]: data[0], 
                    clean_titles[1]: data[1], 
                    clean_titles[2]: data[2], 
                    clean_titles[3]: data[3], 
                    clean_titles[4]: data[4], 
                    clean_titles[5]: data[5], 
                    clean_titles[6]: data[6], 
                    clean_titles[7]: data[7] })


