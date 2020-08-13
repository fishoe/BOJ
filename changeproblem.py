n,money = map(int,input().strip().split())

mlist = []
for i in range(n):
    mlist.append(int(input()))
mlist.sort()
change = money
nnote = []
for m in mlist[::-1]:
    nnote.append( change // m )
    change = change % m

print(sum(nnote))