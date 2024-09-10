#merge sort implementation
def merge_sort(arr):    
    def merge(arr,start,end):
        if start >= end:
            return [arr[end]]
        mid = (start + end) // 2
        left = merge(arr,start,mid)
        right = merge(arr,mid+1,end)
        i, j, lst = 0, 0, []
        while not ( i >= len(left) and j >= len(right)) :
            if (i < len(left) and j < len(right) and left[i] < right[j]) or (j >= len(right)):
                lst.append(left[i])
                i += 1
            elif (i < len(left) and j < len(right) and left[i] > right[j]) or (i >= len(left)):
                lst.append(right[j])
                j += 1
        return lst
    return merge(arr,0,len(arr)-1)



# quick sort implementation
def quick_sort(arr):
    def quick(low,high):    
        if low < high:
            pivot = arr[low]
            i, j = low, high
            while i < j:
                while i < high and arr[i] <= pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            arr[low], arr[j] = arr[j], arr[low]
            quick(low,j)
            quick(j+1,high)
    quick(0,len(arr)-1)



# insertion sort
def insert_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1