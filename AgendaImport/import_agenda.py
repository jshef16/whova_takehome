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

# Create Agenda table
agenda = db_table("Agenda", {'id': "number NOT NULL PRIMARY KEY",
                             'date': "text NOT NULL", 
                             'time_start': "time NOT NULL", 
                             'time_end': "time NOT NULL", 
                             'session_type': "text NOT NULL", 
                             'title': "text NOT NULL", 
                             'location': "text", 
                             'description': "text", 
                             'speaker': "text" })

# Cleans cells of preceding "text:" and changes <empty> cells to be empty strings
for row_num in range(15, sh.nrows):
    # Create list of data to hold data for one row
    data = []
    for cell in sh.row(row_num):
        data.append(str(cell).replace("text:", "").replace("'", "").replace("empty:", ""))

    # Insert row of data into Agenda table, rownum - 15 so that id starts at 0
    agenda.insert({ 'id': row_num - 15,
                    'date': data[0], 
                    'time_start': data[1], 
                    'time_end': data[2], 
                    'session_type': data[3], 
                    'title': data[4], 
                    'location': data[5], 
                    'description': data[6], 
                    'speaker': data[7] })
    
agenda.close()


