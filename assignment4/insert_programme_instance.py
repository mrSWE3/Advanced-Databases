from create_grapth import *
import csv

def group_by_first_element(tuples):
    grouped_dict = {}
    for tup in tuples:
        key = tup[0]
        group: set = grouped_dict.get(key, set())
        group.add(tup[1])
        grouped_dict[key] = group

    return {k:sorted(list(v)) for k,v in grouped_dict.items()}

with open('Programme_Courses.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]

values = [(l[0], l[2]) for l in lines]
grouped = group_by_first_element(values)
values = sum([[[year,k] for year in v] for k,v in grouped.items()], [])
values = [[f"{t[0]}_{t[1]}", t[0]] for t in values]
print(create_nodes(PI.n, [PI.year], [], values))