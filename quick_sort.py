def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        
    items_greater = []
    items_lower = []
    
    for item in arr:
        if item > pivot:
            items_greater.append(item)
            
        else:
            items_lower.append(item)
        
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([7,5,4,3,6,3,1,3,5,3,1]))
        