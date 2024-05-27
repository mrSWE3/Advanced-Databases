import os
import glob
import subprocess
base = "assignment4/"
file_paths_order = ["create_person.py",
                    "insert_student.py",
                    "insert_senior_teachers.py",
                    "insert_teaching_assistants.py",
                    "insert_department.py",
                    "create_division.py",
                    "insert_programme.py",
                    "insert_programme_instance.py",
                    "insert_course.py",
                    "insert_course_instance.py",
                    "insert_PC.py",
                    "insert_enrollment.py",
                    "insert_registrations.py",
                    "insert_time_assigned.py",
                    "insert_time_rported.py"
                    ]

files = glob.glob(f"{base}cypher_query/*")
for f in files:
    os.remove(f)

for i, path in enumerate(file_paths_order):
        name = f"{i}_{path[:-2]}txt" 
        o = subprocess.run(
        ['python',  base + path],  
        capture_output=True,          
        text=True)
        with open(base + "cypher_query/" + name, mode="w") as f:
                f.writelines(o.stdout)
