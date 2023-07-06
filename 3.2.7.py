import sys
import re

pattern = r"\b[Aa]+\b"
for line in sys.stdin:
    print(re.sub(pattern, "argh", line.rstrip(), count=1))