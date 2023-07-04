s = input()
t = input()

count = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        count += 1
        
print(count)