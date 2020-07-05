import csv

persons=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
header=['name','address','age']
csvfile=open('persons.csv','w', newline='')
obj=csv.writer(csvfile)
obj.writerow(header)
for person in persons:
    obj.writerow(person)

csvfile.close() 