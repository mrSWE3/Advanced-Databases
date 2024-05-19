from create_grapth import *
import csv

with open('Teaching_Assistants.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
values = [[l[0], l[1]] for l in lines]
print(create_value([Person.n, Student.n, TA.n], [Person.name, TA.n], values))