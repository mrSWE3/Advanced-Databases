from create_grapth import *
label = ST.n
props = [Person.id, Person.name]

print(create_label(label=label, props=props, uniq_props=[Person.id]))

with open('Senior_Teachers.csv', newline='') as teacher_csv:
    lines = teacher_csv.readlines()[1:]
    teachers = map(lambda t: [t.split(",")[1], t.split(",")[0], t.split(",")[-1].rstrip('\n')], lines)
    t = dict()
    for id, name, division in teachers:
        t[id] = (name, division)
        
    print(create_value([Person.n, Teacher.n, ST.n], props, [[id, name] for id, (name, division) in t.items()]))
