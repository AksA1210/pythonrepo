''' 2.Develop a program to read the three sides of two triangles and calculate the area of both. Define a function to read the three sides
  and call it. Also, define a function to calculate the area. Print the total area enclosed by both triangles and each triangle's contribution (%) 
  towards it.'''

def getsides():              # To get the sides of the triangles from the user
  a=int(input("Enter the first side length : "))
  b=int(input("Enter the second side length : "))
  c=int(input("Enter the third side length : "))
  return a,b,c
def area(a,b,c):             # To calculate the area of the triangle
  s=(a+b+c)//2
  p=s*(s-a)*(s-b)*(s-c)
  ar=p**0.5
  return(ar)

print("Triangle 1")
a,b,c=getsides()
print("Triangle 2")
p,q,r=getsides()
A1=area(a,b,c)
A2=area(p,q,r)
print("Area of triangle 1 is : ",A1)
print("Area of triangle 2 is : ",A2)
Total_area=A1+A2
print("Total area : ",Total_area)
percont1=(A1/Total_area)*100
percont2=100-percont1
print("The percentage contribution of triangle 1 to the total area is : ",percont1)
print("The percentage contribution of triangle 2 to the total area is : ",percont2)


