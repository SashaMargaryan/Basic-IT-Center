f=float(input("trvache:f"))

a=int(f/100)
b=int((f%100)/10)
c=int((f%100)%10)
print(a)
print(b)
print(c)

if c+a<5:
    print("a")
else:
    print("b")
