s = input()
a = input()
b = input()

count = 0

while a in s:
    if count > 1000:
        print("Impossible")
        break
    s = s.replace(a, b)
    count += 1
else:
    print(count)