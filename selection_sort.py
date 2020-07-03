#bubble sort
987654321
876543219
765432189
654321789
543216789
432156789
321456789
213456789
123456789


#Insertion Sort
987654321
187654329
127654389
123654789
123456789

def selection_sort(arr):
    length = range(0, len(arr)-1)
    
    for i in length:
        min_value = i
        
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
            
        if min_value != i:
            arr[min_value],arr[i] = arr[i],arr[min_value]
            
    return arr

print(insertion_sort([4,3,1,4,6,8,6,8,5,9,2]))





