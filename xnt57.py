t=float(input("trvache:t"))

a=int(t/100)
b=int((t%100)/10)
c=int((t%100)%10)
print(a)
print(b)
print(c)

if t>300:
    print(b/c)
else:
    print(a/c)