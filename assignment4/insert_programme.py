from create_grapth import *
import csv

with open('Programmes.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
names = [[l[0]] for l in lines]
print(create_nodes(Programme.n, [Programme.n], [Programme.n], names))