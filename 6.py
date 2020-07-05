def find_name(input_list):
    for each in input_list:
        if each=='John':
            return f'Found'
    return f'Not Found'
    
if __name__ == "__main__":
    print(find_name(["ram", "shyam","pranish","Abhishek","Samir","Sumip","Sajan"]))