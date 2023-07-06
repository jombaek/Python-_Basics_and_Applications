import sys
import re

pattern = r"human"
for line in sys.stdin:
    print(re.sub(pattern, "computer", line.rstrip()))