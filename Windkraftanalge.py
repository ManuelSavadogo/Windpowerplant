#import csv data

import csv
import os
import sys
city = input("Enter City ")
with open(city) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'Start: {row[0]} End: {row[1]} Pace: {row[2]} m/s')

            line_count += 1

    print('\n')

    print(f'Processed {line_count} lines.')

