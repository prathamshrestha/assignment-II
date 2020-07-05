list_profile=[("Pranish","acharya",24),("Shyam","Poudel",22),("Samip","Poudel",None),("Ram","Bahadur",21),("Samir","Shrestha",None)]
collect_age = [each[2] for each in list_profile if each[2] is not None]
avg_age=sum(collect_age)/len(collect_age)
print (f'average age is {avg_age}')
for each in list_profile:
    if each[2] is not None:
        if each[2] > avg_age:
            print(f'{each} is old')
        else:
            print(f'{each} is young')
    else:
        print(f'{each} has no age to determine')