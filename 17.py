
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__ == "__main__":
    a=input('enter a no. ')
    b=input('enter a no. ')
    if a.isnumeric()==True or b.isnumeric()==True:
        a=int(a)
        b=int(b)
        choice=int(input('enter 1 for addition \n enter 2 for substraction \n enter 3 for multiplication \n enter 4 for division'))
        if choice==1:
            print('added no. is ',sum(a,b))
        elif choice==2:
            print('subtracted no. is ',sub(a,b))
        elif choice==3:
            print('multipled no. is ',mul(a,b))
        elif choice==4:
            if (b==0):
                print('input invalid')
            else:
                print(' no. is ',div(a,b))
        else:
            print('input invalid')
        
    else:
        print('invalid input')