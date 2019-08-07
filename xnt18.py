import math
x=float(input("trvache:x"))
z=float(input("trvache:z"))

if 1<=x<=7:
    y=math.fabs(x)+2*math.fabs(z)**4+math.pow(math.e,x+1)
    print(y)

else:
    y=1-math.cos(2)*math.pow(x,7)+math.pow(z,7)/ 1+math.cos(2)*math.pow(x,7)+math.pow(z,7)
    print("hakarak depqum")
