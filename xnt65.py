t=float(input("trvache:t"))

a=int((t/100)/10)
b=int((t/100)%10)
c=int((t%100)/10)
d=int((t%100)%10)
print(a)
print(b)
print(c)
print(d)

if d*c==12:
    print("y=12")
else:
    print("y=0")