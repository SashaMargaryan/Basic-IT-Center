y=float(input("trvache:y"))

a=int((y/100)/10)
b=int((y/100)%10)
c=int((y%100)/10)
d=int((y%100)%10)
print(a)
print(b)
print(c)
print(d)

if a*b*c*d>200:
    print("0")
else:
    print("1")