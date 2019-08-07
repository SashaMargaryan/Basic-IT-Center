import math
a=float(input("trvache:a"))
b=float(input("trvache:b"))
x=float(input("trvache:x"))

if math.pow(a,2)+math.pow(b,2)>5:
    y=3*math.pow(math.e,a)*math.pow(math.e,x)+math.log(math.pow(2,2)+math.pow(b,2)+5,3)
    print(y)

elif math.pow(a,2)+math.pow(b,2)<1:
    y=math.cos(4)*(a+b)-4*math.cos(2)*(a+b)+3/math.cos(4)*(a+b)+4*math.cos(2)*(a+b)+3
    print(y)

else:
    y=-3
    print("mnachat depqum")
