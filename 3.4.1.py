import csv
from collections import Counter

with open(r'D:\Загрузки\Crimes.csv') as fin:
    reader = csv.reader(fin)
    data = list(reader)[1:]
    crimes = (row[5] for row in data if '2015' in row[2])
    crime_counts = Counter(crimes)
    print(*crime_counts.most_common(1)[0])