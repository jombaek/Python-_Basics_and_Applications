import os

with open('result.txt', 'w') as f:
    for current_dir, dirs, files in os.walk(r'D:\Загрузки\main'):
        if list(filter(lambda x: x.endswith('.py'), files)):
            rel_path = current_dir.replace("D:\Загрузки\\", "")
            f.write('{}\n'.format(rel_path))
