def binary_search(arr, low, high, x): 
  
    
    if high >= low: 
  
        mid = (high + low) // 2
  
        
        if arr[mid] == x: 
            return mid 
  
       
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
       
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
     
        return -1
    

if __name__ == "__main__":
    str_arr = input('enter an array ').split(' ') 
    l = [int(num) for num in str_arr]
    b=int(input('enter a number u want to search '))
    print('the number is in the index ',binary_search(l,0,len(l),b)+1)