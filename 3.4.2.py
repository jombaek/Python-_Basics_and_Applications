import json

class_list  = json.loads(input())

with_children = {element['name']: set() for element in class_list }

for eli in class_list :
    for elc in with_children:
        if elc in eli['parents']:
            with_children[elc].add(eli['name'])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))