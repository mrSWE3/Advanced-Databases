from add_thing import insert_clazz, PREFIXES
import csv

if __name__ == "__main__":
    # Open the CSV file in read mode
    with open('Course_Instances.csv', newline='') as csvfile:
        with open('Course_plannings.csv', newline='') as csvfile2:
            # Create a CSV reader object
            lines = [l + l2 for l,l2 in zip(csv.reader(csvfile), csv.reader(csvfile2))][1:]
            print(lines[0])

            names = [l[3] for l in lines]
            values = [[l[1], l[2], l[3],l[-3],l[-2],l[-1], l[4], l[0]] for l in lines]
            insert = insert_clazz(clazz="CourseInstance", 
                        node_names=names,
                        properties=["courseInstanceStudyPeriod", 
                                    "courseInstanceAcademicYear", "courseInstanceId",
                                    "courseInstanceCapacity", "seniorPlanningHours", 
                                    "assistantPlanningHours"],
                                    
                        objectProps=["courseExaminedBy", "courseInstanceOf"],
                        values=values, 
                        prefixes=PREFIXES
                        )
            print(insert)