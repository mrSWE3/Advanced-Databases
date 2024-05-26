from create_grapth import *
import csv

with open('Students.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]

print(create_relation(Enrollment.n, [Enrollment.graduated], []))



for i, (_,student_id,programme_code,year,graduated )in list(enumerate(lines)):
    pi_name = f"PI{i}"
    p_name = f"P{i}"
    s_name = f"S{i}"

    programme_match = match(p_name, Programme.n, [Programme.code], [programme_code])
    belongs_to_match = match_on_edge(pi_name, p_name, PI.belongs_to, [], [])
    extra_matches = f"{programme_match} {belongs_to_match}"
    print(create_edge(s_name, Student.n, [Person.id], [student_id], 
                      pi_name,PI.n,[PI.year],[year], Enrollment.n,
                       [Enrollment.graduated], [graduated], 
                       extra_match=extra_matches, multiway=True))