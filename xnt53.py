t=float(input("trvache:t"))

a=int(t/100)
b=int((t%100)/10)
c=int((t%100)%10)
print(a)
print(b)
print(c)

k=200

if t>k:
    print(t/(a+b+c))
else:
    print((a+c)/t)