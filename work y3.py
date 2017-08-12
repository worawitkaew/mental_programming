#! user / 600510577
m1=(float)(input("input m1:"))
b1=(float)(input("input b1:"))
print("สมการ2:")
m2=(float)(input("input m2:"))
b2=(float)(input("input b2:"))
o1=b1-b2
x=o1/((b1*m2)-(b2*m1))
y=(m1*x)+b1

print('จุดตัด x= %.2f'%x,'จุดตัด y= %.2f'%y)

