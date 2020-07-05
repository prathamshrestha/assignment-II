import csv
reader = csv.DictReader(open('persons.csv'))

result = {}
for row in reader:
    for column, value in row.items(): 
        result.setdefault(column, []).append(value)
print(result)