#import csv data

#usr/venv/binpython
 #-*- coding: utf-8 -*-


import csv
import matplotlib.py


p = Path(/Users/manuelsavadogo/Desktop/PycharmProjects/Windkraftanlage/daressalam_-6.8161_39.2804.csv)
with p.open('r') as file:
   mycsv = csv.reader(file)
   header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)