from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Senior_Teachers.csv', newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]

        names = [l[0] for l in lines]
        values = [[l[0], l[1]] for l in lines]
        insert = insert_clazz(clazz="SeniorTeacher", 
                     node_names=names,
                     properties=["personName", "personId"],
                     values=values, 
                     prefixes=PREFIXES
                     )
        print(insert)