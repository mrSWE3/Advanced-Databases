from os import walk
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "12345678")

ls = next(walk("./assignment4/cypher_query"))
QUERY_FILES = [f"{ls[0]}/{x}" for x in sorted(ls[2], key=lambda x: int(x.split("_")[0]))]

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    session = driver.session()
    # Clear database
    session.run("match (a) -[r] -> () delete a, r")
    session.run("match (a) delete a")
    # Run queries
    for num, path in enumerate(QUERY_FILES):
        with open(path, newline='') as file:
            file_name = path.split("/")[3]
            print(file_name + f" [{num+1} of {len(QUERY_FILES)}]")
            for line in file:
                if line.strip():
                    session.run(line)
    print("Done")
    session.close()
