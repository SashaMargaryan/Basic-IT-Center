t=float(input("trvache:t"))

a=int((t/100)/10)
b=int((t/100)%10)
c=int((t%100)/10)
d=int((t%100)%10)
print(a)
print(b)
print(c)
print(d)

if b==4 or c==4:
    print("YES")
else:
    print("NO")
