from create_grapth import *
import csv

with open('Programmes.csv', newline='') as csvfile:
    # Create a CSV reader object
    lines = [l for l in csv.reader(csvfile)][1:]
names = [[l[0], l[1]] for l in lines]
print(create_nodes(Programme.n, [Programme.name, Programme.code], [Programme.code], names))
print(create_edges(Programme.bellongs_to, [], [], 
                   [Edge_data(f"p{i}", Programme.n, [Programme.code], [p],
                              f"d{i}", Department.n, [Department.name], [d], []) 
                    for i, (_,p,d,_) in enumerate(lines)]))
print(create_edges(Programme.has_director, [], [], 
                   [Edge_data(f"p{i}", Programme.n, [Programme.code], [p],
                              f"d{i}", ST.n, [Person.id], [dir], []) 
                    for i, (_,p,_,dir) in enumerate(lines)]))
