def findpartial(arr,s):
    lidx = 0
    ridx = 1

    answer = 0
    mn = min(arr)
    mn = 0 if mn > 0 else mn * -1
    temsum = arr[0] + mn
    for i in arr[1:]:
        if temsum < s +mn*(ridx-lidx):
            temsum += arr[ridx] + mn
            ridx += 1
            print(lidx,ridx,temsum)
        elif temsum > s+mn*(ridx-lidx):
            temsum -= arr[lidx] + mn
            lidx += 1
            print(lidx,ridx,temsum)
        else :
            answer += 1
            temsum += arr[ridx] + mn
            ridx +=1
            print(lidx,ridx)
    return answer

import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))

print(findpartial(arr,m))