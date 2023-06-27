def is_exception_ancestor(exceptions, start, end):
    visited = set()

    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for child in exceptions[node]:
            if child not in visited and dfs(child):
                return True
        return False

    return dfs(start)


n = int(input())
exceptions = {}

for _ in range(n):
    line = input().split()
    child = line[0]
    parents = line[2:]
    exceptions[child] = parents

m = int(input())
unneeded_exceptions = []

for i in range(m):
    exception = input()
    for unneeded_exception in unneeded_exceptions:
        if is_exception_ancestor(exceptions, exception, unneeded_exception):
            print(exception)
            break
    unneeded_exceptions.append(exception)