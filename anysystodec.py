n, sys = input().split()
sys = int(sys)

result = 0
for cnt, i in enumerate(n[::-1]):
    d = 0
    if ord(i) < 65 : #65 is ascii(A)
        d=int(i)
    else :
        d= 10 +ord(i) - 65
    result += d * (sys**cnt)
print(result)


