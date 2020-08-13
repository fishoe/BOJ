n = int(input())
meetlist=[]
for i in range(n):
    b,e = map(int,input().split())
    meetlist.append((b,e))

meetlist.sort(key=lambda m:[m[1],m[0]])

answer = 1
end = meetlist[0][1]

for i in meetlist[1:]:
    if end <= i[0]:
        end = i[1]
        answer = answer+1
print(answer)

