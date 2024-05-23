from create_grapth import *
import csv
relation  = TimeAssigned.n
props = [TimeAssigned.hours]

with open('Assigned_Hours.csv', newline='') as csvfile:
    lines = [l for l in csv.reader(csvfile)][1:]
print(create_edges(relation, props, [],
              [Edge_data(f"ci{i}", CI.n, [CI.id], [course],
                         f"t{i}", Teacher.n, [Person.id], [teahcer], [hours])
                for i,(_, _, _, teahcer, hours, course) in enumerate(lines)],
                True))