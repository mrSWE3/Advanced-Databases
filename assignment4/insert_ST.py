from create_grapth import *
import csv

with open('Senior_Teachers.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
values = [[l[0], l[1]] for l in lines]
print(create_value(labels=[Person.n, ST.n], props=[Person.name, Person.id], values=values))