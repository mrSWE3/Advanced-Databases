from typing import List, Dict, Type, Union, Tuple
PREFIXES = ["rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
            ": <http://www.semanticweb.org/lukasgar/ontologies/2024/3/untitled-ontology-3/>"]


def insert_clazz( 
                 clazz: str,
                 node_names: Union[List[str], None] = None,
                 properties: List[str] = [],
                 values: List[List[str]] = [],
                 node_start_index = 0,
                 contex = "",
                 prefixes = []):
    assert(all([len(values[0]) == len(v) for v in values]))
    assert(len(properties) == len(values[0]))
    pefix_statment = " \n".join([f"PREFIX {p}" for p in prefixes])

    prop_statments = [f":{p} ?prop{i}" for i,p in enumerate(properties)]
    prop_statment = " ;\n".join(prop_statments) + " .\n"

    prop_names = " ".join([f"?prop{i}" for i in range(len(properties))])

    values_statemts = []
    if node_names == None:
        node_names = [f"{contex}:{clazz}{i}" for i in range(node_start_index, len(values))]
    else:
        node_names = [name.replace(" ", "_") for name in node_names]
    for v, node_name in zip(values, node_names):
        prop_values = [f"\"{p}\"" for p in v]
        statment_segments = [node_name] + prop_values
        statment = f"({" ".join(statment_segments)})"
        values_statemts.append(statment)
    values_statment = " \n".join(values_statemts)
    s =     pefix_statment                                      + \
            "\n"                                                + \
            "INSERT {\n"                                        + \
            f"?node rdf:type {contex}:{clazz} ;\n"              + \
            prop_statment                                       + \
            "}\n"                                               + \
            "WHERE {\n"                                         + \
            f"VALUES (?node {prop_names})\n"                    + \
                "{\n"                                           + \
                    values_statment                             + \
                "}"                                             + \
            "}\n"                                             
    return s


if __name__ == "__main__":
    print(insert_clazz(clazz="Student",
                    node_names=["Student 1", 
                                "Student 2"],
                    properties=["personId", "personName"],
                    values=[[   "1",        "A"], 
                            [   "2",        "B"]],
                    prefixes=PREFIXES))