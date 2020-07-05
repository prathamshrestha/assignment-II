def is_prime(num):
    count=0
    for i in range(num):
        if i%num==0:
            count+=1

    if count==1:
        return True
    else:
        return False

if __name__ == "__main__":
    num=int(input('enter a number to check prime '))
    if is_prime(num)==True:
        print('prime')
    else:
        print('not prime')