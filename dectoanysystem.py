

n , system = map(int,input().split())
numstk = []
if system > 36 :
    print(-1)
else :
    while n != 0:
        d = n % system
        if d > 9 :
            d = chr(d-10+65)
        numstk.append(d)
        n = n//system
for i in numstk[::-1] :
    print(i,end='')