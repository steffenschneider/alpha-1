import csv

## write - dict to csv
dict1 = {'one': 1, 'two': 2, 'three': 3}
with open('output.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in dict1.items():
        writer.writerow([key, value])

## read
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

## read - part 2
path = f.Pathes.todo_privat

with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    data = csv.reader((line.replace('\0', '') for line in f), delimiter=",")
    for utf8_row in data:
        print(utf8_row)

## read into dict
with open('names.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['first_name'], row['last_name'])

## read into dict - part 2
with open(path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print('{:.<40} {}'.format(row['TASK'], row['DATE']))
