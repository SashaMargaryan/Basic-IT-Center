import math
a=float(input("trvache:a"))
b=float(input("trvache:b"))
x=float(input("trvache:x"))

if a+math.fabs(b)<-5:
    y= math.pow(math.e,math.fabs(a+x))*1-math.cos(2)*(a+x+b)/2
    print(y)

elif a+math.fabs(b)>2:
    y=math.atan(a)+math.atan(x)**3
    print(y)

else:
    y=a+math.fabs(b)
    print("mnachat depqum")