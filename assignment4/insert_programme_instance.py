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
weak_values = [(Node_id(Programme.n, [Programme.name], [v[1]]), [v[0]]) for v in values]
#print(weak_values)
print(create_label(PI.n, [PI.year], []))
print(create_weak_node_value([PI.n], [PI.year], weak_values, PI.belongs_to))
#print(create_nodes(PI.n, [PI.year], [], values))