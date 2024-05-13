from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Programme_Courses.csv', newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]

        names = [l[1] for l in lines]
        values = [[l[0], l[1], l[2] ,l[3] ,l[5], l[6]] for l in lines]
        insert = insert_clazz(clazz="ProgrammeCourse", 
                     node_names=names,
                     properties=["studyYear", "programmeCourseType"],
                     objectProps=["programmeCourseAvailableFor"],
                     values=values, 
                     prefixes=PREFIXES
                     )
        print(insert)