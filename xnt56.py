t=float(input("trvache:t"))

a=int(t/100)
b=int((t%100)/10)
c=int((t%100)%10)
print(a)
print(b)
print(c)

if c>b:
    print((a+b+c)/t)
else:
    print(t)