from create_grapth import *
import csv
label = CI.n
props = [CI.studyPeriod, CI.academicYear, CI.id,]

print(create_label(label=CI.n, 
                   props=props,
                     uniq_props=[CI.id]))


with open('Course_Instances.csv') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
values = [l[1:4] for l in lines]
print(create_value([label], props, values)) 

for i, (course, studyPeriod, academicYear, id, examiner) in enumerate(lines):
  ci_name_c = f"ci{i}"
  ci_name_c2 = f"cci{i}"
  course_name = f"c{i}"
  examiner_name = f"e{i}"
  print(create_edge(ci_name_c, CI.n, [CI.id], [id], 
              course_name, Course.n, [Course.code], [course],
              CI.instanceOf, [], []))
  print(create_edge(ci_name_c2, CI.n, [CI.id], [id], 
                    examiner_name, ST.n, [Person.id], [examiner], 
                    CI.examinedBy, [], []))
