from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Students.csv', newline='') as csvfile:
        # Create a CSV reader object
        lines = [l for l in csv.reader(csvfile)][1:]

        names = [l[1] for l in lines]
        values = [[l[-1], l[0], f"{l[-2]}-{int(l[-2])+1}_{l[-3]}"] for l in lines]
        insert = insert_clazz(clazz="Enrollment",
                     properties=["enrolmentGraduated"],
                     objectProps=["enrolment", "enrolment"],
                     values=values, 
                     prefixes=PREFIXES
                     )
        print(insert)