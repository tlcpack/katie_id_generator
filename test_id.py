import csv

with open('nametest.csv', newline='') as csvfile:
    uat_id = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        uat_id.append(row['fn'])
        uat_id.append(row['ln'])
        uat_id.append(row['age'])

print(uat_id)