def qsort(arr):
    if len(arr) <= 1 :
        return arr
    pvtlist = [arr[0],arr[-1],arr[(len(arr)-1)//2]]
    pvt = sum(pvtlist) - min(pvtlist) - max(pvtlist)

    low = []
    high = []
    mid = []
    for n in arr:
        if n < pvt:
            low.append(n)
        elif n > pvt:
            high.append(n)
        else :
            mid.append(n)
    return qsort(low) + mid + qsort(high)

print(qsort([9,5,8,7,5,2,1,3]))