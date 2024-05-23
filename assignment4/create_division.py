from create_grapth import *
label = Division.n
props = [Division.name]

print(create_label(label=label, props=props, uniq_props=[Division.name]))

with open('Senior_Teachers.csv', newline='') as division_csv:
    lines = division_csv.readlines()[1:]
    divisions_and_departments = map(lambda d: [d.split(",")[-1].rstrip('\n'), d.split(",")[2]], lines)
    dd = dict()
    for d in divisions_and_departments:
        dd[d[0]] = d[1]
        
    print(create_value([Division.n], [Division.name], [[d] for d in dd.keys()]))
    label = Division.n
props = [Division.name]

print(create_relation(Division.under, [], []))

with open('Senior_Teachers.csv', newline='') as division_csv:
    lines = division_csv.readlines()[1:]
    divisions_and_departments = map(lambda d: [d.split(",")[-1].rstrip('\n'), d.split(",")[2]], lines)
    dd = dict()
    for d in divisions_and_departments:
        dd[d[0]] = d[1]
        
    print(create_edges(Division.under, [], [], [Edge_data(f"a{i}", Division.n, [Division.name], [ed[0]],f"b{i}", Department.n, [Department.name], [ed[1]], []) for i, ed in enumerate(dd.items())]))
