from typing import List, Tuple

def create_label(label: str, props: List[str], uniq_props: List[str]):
    assert all([up in props for up in uniq_props])
    constraints = [f"CREATE CONSTRAINT ON (n:{label}) ASSERT exists(n.{p});" for p in props]
    uniqs = [f"CREATE CONSTRAINT ON (n:{label}) ASSERT n.{up} IS UNIQUE;" for up in uniq_props]
    statements = "\n".join(constraints + uniqs)
    return statements
def fill(values: List[str], label: str, props: List[str], node_name:str = "n"):   
    prop_list = ",".join([f"{p}: {v}" for p,v in zip(props, values)])
    return f"{node_name}:{label} {"{"} {prop_list} {"}"}"

def create_value(label: str, props: List[str], values: List[list[str]]):
    assert len(props) == len(values[0])
    
    value_statemnts = ",\n".join([f"({fill(vs, label, props)})" for vs in values])
    return f"CREATE {value_statemnts}"

def create_nodes(label: str, props: List[str], uniq_props: List[str], values: List[list[str]]):
    label_stmts = create_label(label, props, uniq_props)
    value_stmts = create_value(label, props, values)
    return label_stmts + "\n" + value_stmts

def create_relation(relation: str, relation_props: List[str], uniqe_relation_props:List[str]):
    constraints = [f"CREATE CONSTRAINT ON ()-[r:{relation}]-() ASSERT exists(r.{p});" for p in relation_props]
    uniqs = [f"CREATE CONSTRAINT ON ()-[r:{relation}]-() ASSERT r.{up} IS UNIQUE;" for up in uniqe_relation_props]
    statements = "\n".join(constraints + uniqs)
    return statements
def create_edge(from_label:str, from_keys: List[str], from_values: List[str],
                 to_label: str , to_keys: List[str], to_values: List[str],
                 relation: str, relation_props: List[str], relation_values:List[str], multiway = False ):
    relation_prop_statment = fill(relation_values, relation, relation_props)
    from_dict = fill(from_values, from_label, from_keys, "a")
    to_dict = fill(to_values, to_label, to_keys, "b")
    return f"MATCH ({from_dict}), ({to_dict}) \n" + \
           f"CREATE (a)-[{relation_prop_statment}]-{">" if not multiway else ""}(b)"
def create_edges(relation: str, relation_props: List[str], uniqe_relation_props:List[str],
                 edge_data: List[Tuple[Tuple[str, List[str], List[str]], Tuple[str, List[str], List[str]], List[str]]],
                 multiway = False):
    relation_statments = create_relation(relation, relation_props, uniqe_relation_props)
    values_statments = "n".join([create_edge(ed[0][0],ed[0][1], ed[0][2],
                                    ed[1][0],ed[1][1], ed[1][2],
                                    relation, relation_props, ed[2], multiway) for ed in edge_data])
    return relation_statments + "\n" + values_statments


if __name__ == "__main__":
    print(create_nodes(label="Student", 
                      props=["name", "id"], 
                      uniq_props=["name"],
                      values=[["KG", "1"],["Lukas","2"]]))
    print(create_edges("Friend", ["started"], ["started"], 
                       [(("Student", ["name"], ["Lukas"]), ("Student", ["name"], ["KG"]), ["2021"])],True))
   