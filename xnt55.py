t=float(input("trvache:t"))

a=int(t/100)
b=int((t%100)/10)
c=int((t%100)%10)
print(a)
print(b)
print(c)

if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
elif c<a and c<b:
    print(c)