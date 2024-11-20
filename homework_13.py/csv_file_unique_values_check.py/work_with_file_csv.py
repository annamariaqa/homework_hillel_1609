import csv

my_set = set()

def open_file(first_file, second_file):
    with open(first_file, newline='') as csvfile1, open(second_file, newline='') as csvfile2:
        reader1 = csv.reader(csvfile1)
        reader2 = csv.reader(csvfile2)
        for row in reader1:
            my_set.update(row)
        for row in reader2:
            my_set.update(row)

    return str(my_set)

print(open_file('rmc.csv', 'random.csv'))

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in my_set:
        writer.writerow([item])
