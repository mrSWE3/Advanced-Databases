from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Programmes.csv', newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]

        names = list(set([l[2] for l in lines]))
        values = [[n] for n in names]
        insert = insert_clazz(clazz="Department", 
                     node_names=names,
                     properties=["departmentName"],
                     values=values, 
                     prefixes=PREFIXES
                     )
        print(insert)