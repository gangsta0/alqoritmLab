b=-1
a = int(input("a= "))
while b<=1:
    if b**2-a==1.5:
        print(3*b+1.6*a)
    elif b**2-a<1.5:
        print(8*a-1.7*b)
    elif b**2-a>1.5:
        print(4*b+7*a)
    b+=2
