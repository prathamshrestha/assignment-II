new_list = []
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n=len(arr)
for i in range(0, n-2): 
    for j in range(i+1, n-1): 
        for k in range(j+1, n): 
            if (arr[i] + arr[j] + arr[k] == 0): 
                new_list.append([arr[i], arr[j], arr[k]])
print(new_list)