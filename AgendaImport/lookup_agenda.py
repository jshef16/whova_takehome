#!/usr/bin/env python

from db_table import *
import argparse

def main():
    DB_NAME = "interview_test.db"


    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add a positional argument for the filename
    parser.add_argument('column')
    parser.add_argument('value')

    # Parse the command line arguments
    args = parser.parse_args()

    column = args.column
    value = args.value

    # Connect to database
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()


    if column == 'speaker':
        query = f'''
        SELECT *
        FROM Agenda
        WHERE speaker LIKE '%{value}%'
        '''
    else:
        query = f'''
        SELECT *
        FROM Agenda
        WHERE {column} = '{value}'
        '''

    # Execute query
    cur.execute(query)

    res = []

    # Print results
    for tup in cur.fetchall():
        res.append(tup)
        subs = []
        if tup[4] != 'Sub':
            subs = get_subsessions(tup[0], cur, conn)
        for sub in subs:
            res.append(sub)

    for i in res:
        print(i)

    


def get_subsessions(id, cur, conn):
    query = f'''
    SELECT *
    FROM Agenda
    WHERE id > {id}
    '''
    cur.execute(query)
    rows = cur.fetchall()
    res = []
    for row in rows:
        if row[4] == "Sub":
            res.append(row)
        else:
            break
    return res


main()