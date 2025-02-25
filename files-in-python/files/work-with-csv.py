import csv

file = 'students.csv'

content = [
    ['oren','11','22','devops'],
    ['emad','12','100','devops']
]
with open(file,'a+') as csvfile:
    csvfile.seek(0)
    reader = csv.reader(csvfile)
    print(reader)
    csv_content= []
    for row in reader:
        print(', '.join(row))
        csv_content.append(row)
    writer = csv.writer(csvfile)
    writer.writerows(content)

    print(csv_content)