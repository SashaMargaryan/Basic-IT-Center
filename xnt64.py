y=float(input("trvache:y"))

a=int((y/100)/10)
b=int((y/100)%10)
c=int((y%100)/10)
d=int((y%100)%10)
print(a)
print(b)
print(c)
print(d)

if d+c==5:
    print("s")
else:
    print("d")

