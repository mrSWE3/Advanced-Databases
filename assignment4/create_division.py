from create_grapth import *
label = Division.n
props = [Division.name]

print(create_label(label=label, props=props, uniq_props=[Division.name]))

with open('../Senior_Teachers.csv', newline='') as division_csv:
    lines = division_csv.readlines()[1:]
    divisions_and_departments = map(lambda d: [d.split(",")[-1].rstrip('\n'), d.split(",")[2]], lines)
    dd = dict()
    for d in divisions_and_departments:
        dd[d[0]] = d[1]
        
    print(create_value([Division.n], [Division.name], [[d] for d in dd.keys()]))
