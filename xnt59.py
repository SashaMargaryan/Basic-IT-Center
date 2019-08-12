t=float(input("trvache:t"))

a=int(t/100)
b=int((t%100)/10)
c=int((t%100)%10)


if a<b and a<c and b<c:
    print(a,b,c)
elif a>b and a>c and b>c:
    print(c,b,a)
elif a>b and a<c and c>b:
    print(b,a,c)


