t=float(input("trvache:t"))

b=int((t%100)/10)
a=int(t/100)
c=int((t%100)%10)
print(b)
print(a)
print(c)

if b+c==b+a:
    print(True)
else:
    print(False)

