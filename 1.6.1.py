def is_ancestor(graph, class1, class2):
    visited = set()

    def dfs(node):
        if node == class2:
            return True
        visited.add(node)
        for child in graph[node]:
            if child not in visited and dfs(child):
                return True
        return False

    return dfs(class1)


n = int(input())
graph = {}
for _ in range(n):
    line = input().split()
    child_class = line[0]
    parent_classes = line[2:]
    graph[child_class] = parent_classes

q = int(input())
for _ in range(q):
    class1, class2 = input().split()
    if is_ancestor(graph, class2, class1):
        print("Yes")
    else:
        print("No")