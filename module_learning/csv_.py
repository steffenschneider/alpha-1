import csv

## dict to csv
dict1 = {'one': 1, 'two': 2, 'three': 3}
with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in dict1.items():
        writer.writerow([key, value])
