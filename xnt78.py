import math
x=10

while x<20:
    if x>12:
        print("Y",x,3*math.log(x,3))
    else:
        print("Y",x,math.pow(x,3))
    x=x+2