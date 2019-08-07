import math
a=float(input("trvache:a"))
x=float(input("trvache:x"))

if math.fabs(a)<3:
    y=1-math.cos(2)*math.fabs(x+a)/2
    print(y)

else:
    y=math.pow(a,1/2)+math.pow(x,1/2)*math.log2(math.pow(a,2)+math.pow(x,4))
    print("hakarak depqum")