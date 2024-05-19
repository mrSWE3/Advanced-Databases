from create_grapth import *
import csv

with open('Students.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
values = [[l[0], l[1]] for l in lines if l[0][:2] != "TA"]
print(create_value([Person.n, Student.n],[Person.name, Person.id], values))