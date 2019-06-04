import csv

with open('nametest.csv', newline='') as csvfile:
    uat_id = ''
    unique = 0
    reader = csv.DictReader(csvfile)
    for row in reader:
        unique += 1
        unique_id = str(unique)
        uat_id = unique_id + "_" + row['fn'] + "_" + row['ln'] + "_" + row['age']
        
        print(uat_id)

# with open('nametest.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     unique = 0
#     for row in reader:
#         unique += 1
#         unique_id = str(unique)
#         row += unique_id
#         print("_".join(row))

# def reverse(x):
#     str = ''
#     for i in x:
#         str = i + str
#     return str

# print(reverse('Taylor'))