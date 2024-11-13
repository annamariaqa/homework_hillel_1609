import csv

my_set = set()
with open('random.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        my_set.update(row)
print(str(my_set))

with open('result_polovykh.csv', 'w') as f:
    f.write(str(my_set))

my_set_rmc = set()
with open('rmc.csv', newline='') as csvfile_rmc:
    reader = csv.reader(csvfile_rmc)
    for row in reader:
        my_set_rmc.update(row)
print(str(my_set_rmc))

with open('result_polovykh.csv', 'w') as f:
    f.write(str(my_set_rmc))
