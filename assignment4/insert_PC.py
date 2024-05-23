from create_grapth import *
import csv
label = PC.n
props = [PC.studyYear, PC.type]

print(create_label(label=PC.n, 
                   props=props,
                     uniq_props=[]))


with open('Programme_Courses.csv') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]

values = [[l[1], l[-1]] for l in lines]
print(create_value([PC.n], props, values))  



for i, (p_code, studyYear, academicYear, course_code, type) in enumerate(lines):
    pc_name = f"pc{i}"
    c_name = f"c{i}"
    p_name = f"p{i}"

    print(create_singel_value([PC.n], props, [studyYear, type], pc_name))
    print(match(p_name, Programme.n, [Programme.code], [p_code]))
    print(create_edges_simpel(pc_name, PC.availableFor, p_name))
    print(match(c_name, Course.n, [Course.code], [course_code]))
    print(create_edges_simpel(pc_name, PC.referenceTo, c_name))


    