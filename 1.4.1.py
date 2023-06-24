def create(namespace, parent):
    namespaces[namespace] = {'parent': parent, 'vars': []}

def add(namespace, var):
    namespaces[namespace]['vars'].append(var)

def get(namespace, var):
    if var in namespaces[namespace]['vars']:
        return namespace
    elif namespace == "global":
        return "None"
    else:
        return get(namespaces[namespace]['parent'], var)

n = int(input())
namespaces = {'global': {'parent': None, 'vars': []}}

for _ in range(n):
    cmd, namesp, arg = input().split()

    if cmd == "create":
        create(namesp, arg)
    elif cmd == "add":
        add(namesp, arg)
    elif cmd == "get":
        print(get(namesp, arg))