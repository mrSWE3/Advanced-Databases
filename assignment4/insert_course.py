from create_grapth import *
import csv
label = Course.n
props = [Course.name, Course.code, Course.creditss, Course.level]

print(create_label(label=Course.n, 
                   props=props,
                     uniq_props=[Course.code]))


with open('Courses.csv') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
values = [l[:4] for l in lines]
print(create_value([label], props, values)) 

for i, (name, code, credits, level, _, division, programme) in enumerate(lines):
  course_name_p = f"c{i}"
  course_name2 = f"cc{i}"
  programme_name = f"p{i}"
  devision_name = f"d{i}"
  print(create_edge(course_name_p, Course.n, [Course.code], [code], 
              programme_name, Programme.n, [Programme.code], [programme],
              Course.owned_by_programme, [], []))
  print(create_edge(course_name2, Course.n, [Course.code], [code], 
                    devision_name, Division.n, [Division.name], [division], 
                    Course.belongs_to_devision, [], []))
