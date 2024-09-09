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
