import math
a=float(input("trvache:a"))
b=float(input("trvache:b"))
x=float(input("trvache:x"))

if a<3:
    y=math.pow(math.e,math.cos(x+a+b))*math.tan(a+math.pow(b,2))
    print(y)

else:
    y=math.log(4+math.pow(a,2)+math.pow(b,2))
    print("hakarak depqym")
