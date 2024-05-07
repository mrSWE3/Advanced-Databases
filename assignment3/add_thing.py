def add_node(name:str, clazz: str):
    s = """"
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:ex="http://www.semanticweb.org/lukasgar/ontologies/2024/3/untitled-ontology-3/">

    <rdf:Description rdf:about="http://www.semanticweb.org/lukasgar/ontologies/2024/3/untitled-ontology-3/{name}">
        <rdf:type rdf:resource="http://www.semanticweb.org/lukasgar/ontologies/2024/3/untitled-ontology-3/{clazz}"/>
    </rdf:Description>

    </rdf:RDF>"""
    return s
print(add_node("Hugo", "student"))