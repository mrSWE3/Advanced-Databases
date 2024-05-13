from add_thing import insert_clazz, PREFIXES
import csv
from itertools import groupby


if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Programme_Courses.csv', newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]

      
        values = [(l[0], l[2]) for l in lines]
        # Sort the data based on the first element of each tuple
        values.sort(key=lambda x: x[0])

        # Group the data by the first element of each tuple
        grouped_data = {key: list(set([g[1] for g in group])) for key, group in groupby(values, key=lambda x: x[0])}
        print(grouped_data.items())
"""
        insert = insert_clazz(clazz="Programme", 
                     node_names=names,
                     properties=["programmeInstanceYear"],
                     objectProps=["programmeInstanceOf"],
                     values=values, 
                     prefixes=PREFIXES
                     )
        print(insert)"""