t=float(input("trvache:t"))

a=int((t/100)/10)
b=int((t/100)%10)
c=int((t%100)/10)
d=int((t%100)%10)
print(a)
print(b)
print(c)
print(d)

if a==1 or b==1 or c==1 or d==1:
    print("1")
else:
    print("0")