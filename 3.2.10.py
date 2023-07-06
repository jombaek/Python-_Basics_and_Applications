import sys
import re

pattern = r"(1(01*0)*1|0)*"
for line in sys.stdin:
    line = line.strip()
    if re.search(r"\A[01]+\Z", line):
        if re.fullmatch(pattern, line[::-1]):
            print(line)