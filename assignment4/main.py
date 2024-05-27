from os import walk
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "12345678")

base = "./assignment4/cypher_query/"
ls = next(walk(base))
QUERY_FILES = [f"{ls[0]}/{x}" for x in sorted(ls[2], key=lambda x: int(x.split("_")[0]))]
# QUERY_FILES = [f"{base}{x}" for x in ["8_insert_course.txt"]]

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    session = driver.session()
    # Clear database
    while session.run("MATCH (n) WITH n LIMIT 1000 MATCH (n) DETACH DELETE n RETURN count(*);").value()[0]: pass
    # # Run queries
    for num, path in enumerate(QUERY_FILES):
        with open(path, newline='') as file:
            file_name = path.split("/")[4]
            print(file_name + f" [{num+1} of {len(QUERY_FILES)}]")
            for line in file:
                if line.strip():
                    session.run(line)
    print("Done")
    session.close()
