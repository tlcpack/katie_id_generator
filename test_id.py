import csv

with open('nametest.csv', newline='') as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['fn'], row['ln'], row['age'])

print(row)