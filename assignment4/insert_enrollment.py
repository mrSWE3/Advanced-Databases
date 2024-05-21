from create_grapth import *
import csv

with open('Students.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]

print(create_relation(Enrollment.n, [Enrollment.graduated], []))


for _,student_id,programme,year,graduated in lines:
    
    print(create_edge(Student.n, [Person.id], [student_id], 
                      PI.n,[PI.year],[year], Enrollment.n,
                       [Enrollment.graduated], [graduated]))