list_name=['dikshyant']
print(f'id of new list{list_name} :{id(list_name)}')
list_name.append('xudin')
print(f'id of 2nd append list{list_name}: {id(list_name)}')

list_name.sort()
print(f'Sorted list is:{list_name}')
print(f'the second item on thelist is {list_name[1]}')