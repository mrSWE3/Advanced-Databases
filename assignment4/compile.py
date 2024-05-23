import chardet
import subprocess
base = "assignment4/"
file_paths_order = ["insert_department.py", 
                    "create_division.py",
                    "insert_programme.py",
                    "insert_programme_instance.py",
                    "create_person.py", 
                    "insert_student.py",
                    "create_senior_teachers.py",
                    "create_teaching_assistants.py",
                    "insert_course.py",
                    "insert_course_instance.py",
                    "insert_PC.py",
                    "insert_enrollment.py",
                    "insert_registrations.py",
                    "insert_time_assigned.py",
                    "insert_time_rported.py"
                
                
                    ]


for i, path in enumerate(file_paths_order):
        name = f"{i}_{path[:-2]}txt" 
        o = subprocess.run(
        ['python',  base + path],  
        capture_output=True,          
        text=True)
        with open(base + "cypher_query/" + name, mode="w") as f:
                f.writelines(o.stdout)
