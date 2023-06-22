objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

unique_objects = set()

for obj in objects:
    unique_objects.add(id(obj))

count = len(unique_objects)

print(count)