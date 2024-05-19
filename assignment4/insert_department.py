from create_grapth import *
import csv

with open('Programmes.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
names = list(set([l[2] for l in lines]))
print(create_nodes(Department.n, [Department.name], [Department.name], [[n] for n in names]))
