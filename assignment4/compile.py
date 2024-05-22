import chardet
import subprocess
base = "assignment4/"
file_paths_order = ["insert_department.py", 
                    "create_division.py"
                    ]

output = ""
for path in (file_paths_order):
        output += f"//from: {path}\n" 
        o = subprocess.run(
        ['python',  base + path],  
        capture_output=True,          
        text=True)
       
        output += o.stdout
        
           

print(output)