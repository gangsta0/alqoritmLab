import math as m
k = (0.273*m.log(3))**(1.573*m.log(5))
p=m.atan(m.sin(1)*m.log(m.log(3)**0.5))
if k>abs(p):
    netice=(7*k-5*p)/(2*k**2+3*p**2)
elif k<=abs(p):
    netice=abs(k-p)
print(netice)



