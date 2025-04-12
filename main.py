#Variable and Data types

name="Suraiya Islam"
age=22
student=True
print(type(name))
print(type(age))
print(type(student))

#Arithmetic Operation
print(age*24)
print(age+24)
print(age/24)
print(age-24)

#Comparision Operator
print(age>18)
print(age==22)
print(age!=24)
print(age<18)

#Logical Operator
x=5
y=10
print(x<y and y>x)
print(x>2 or x<8)
print(not(x<y and y>x))

#Assignment Operator
a=42
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)

#Identity Operator
m=42
n=24
print(m is n)
print(m is not n)

#Membership Operator
data=["Laptop","Mouse","Charger"]
print("Mouse" in data)
print("Cables" not in data)
