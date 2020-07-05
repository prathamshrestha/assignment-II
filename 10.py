def change_case(str,choice): 
    res1 = [str[0].lower()] 
    res2 = [str[0].lower()] 
    
    for c in str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            res1.append('_') 
            res1.append(c.lower()) 
            res2.append('-')
            res2.append(c.lower())
        else: 
            res1.append(c) 
            res2.append(c)
    if choice=='1':  
        return ''.join(res1)
    else:
        return ''.join(res2)

if __name__ == "__main__":
    string=input('enter a camel case string ')
    choice=input('enter 1 for snake case and 2 for kebab case ')
    if choice=='1':
        print('the snake case string is ',change_case(string,choice))
    else:
        print('the kebab case string is ',change_case(string,choice))
        
    