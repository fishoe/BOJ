def conto1(num):
    nl = [0,0]
    for i in range(2,num+1):
        a = nl[i-1] +1
        if i%2==0 and a>nl[i//2]:
            a = nl[i//2] +1
        if i%3==0 and a>nl[i//3]:
            a = nl[i//3] +1
        nl.append(a)
    return nl[-1]

print(conto1(56))