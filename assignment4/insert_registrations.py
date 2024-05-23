from create_grapth import *
import csv
relation  = Registration.n
props = [Registration.course_status]

print(create_relation(relation, props, []))

with open('Registrations.csv', newline='') as csvfile:
    lines = [l for l in csv.reader(csvfile)][1:]
egs = []
for i, (ci, s_id, status, garde) in enumerate(lines[:]):
    relation_props = [Registration.course_status] 
    relation_values = [status]
    
    if garde != "":
        relation_props.append(Registration.grade)
        relation_values.append(garde)
    print(create_edge(f"a{i}", Student.n,[Person.id], [s_id],
                               f"b{i}", CI.n, [CI.id], [ci], 
                               Registration.n, relation_props, relation_values,
                               True))

