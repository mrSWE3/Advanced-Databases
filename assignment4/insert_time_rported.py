from create_grapth import *
import csv
relation  = TimeReported.n
props = [TimeReported.hours]

with open('Reported_Hours.csv', newline='') as csvfile:
    lines = [l for l in csv.reader(csvfile)][1:]
print(create_edges(relation, props, [],
              [Edge_data(f"ci{i}", CI.n, [CI.id], [course],
                         f"t{i}", Teacher.n, [Person.id], [teahcer], [hours])
                for i,(course, teahcer, hours) in enumerate(lines)],
                True))