from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Registrations.csv', newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]
        lines = [l for l in lines if l[2] != "completed"]
        values = [[l[2], l[0], l[1]] for l in lines]
        names = [f"ImcompltedCourse{i}" for i in range(len(lines))]
        insert = insert_clazz(clazz="Registrations", 
                     node_names=names, 
                     properties=["imcompleted"],
                     objectProps=["registered", "registered"],
                     values=values, 
                     prefixes=PREFIXES
                     )
        print(insert)