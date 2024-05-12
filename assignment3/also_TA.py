from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open("Teaching_Assistants.csv", newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]

        names = [l[0] for l in lines]
        insert = insert_clazz(clazz="TeachingAssistant", 
                     node_names=names,
                     prefixes=PREFIXES
                     )
        print(insert)