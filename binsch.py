import sys
input = sys.stdin.readline

def binsearch(arr,target):
    lidx = 0
    ridx = len(arr)-1
    while lidx <= ridx:
        print(' '*lidx*2 , arr[lidx:ridx+1])
        mid = (lidx + ridx)//2
        if arr[mid] == target :
            return mid
        elif arr[mid] > target :
            ridx = mid - 1
        else :
            lidx = mid + 1
    return None

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

arr.sort()

for t in targets:
    if binsearch(arr,t) is None :
        print("0")
    else :
        print("1")