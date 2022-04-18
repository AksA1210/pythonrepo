'''1.Develop a program to read a four-digit number and find its:  
 a. Sum of digits 
 b. Reverse
 c. Difference between the product of digits at the odd position and the product of digits at the even position.'''
 

def digits(x):
   dig_1=x%10
   dig_2=(x//10)%10
   dig_3=(x//100)%10
   dig_4=(x//1000)%10
   return dig_1,dig_2,dig_3,dig_4
def sum_dig(dig_1,dig_2,dig_3,dig_4):
   sum=dig_1+dig_2+dig_3+dig_4
   print("Sum of the digits of ",x,"is : ",sum)
def reverse(dig_1,dig_2,dig_3,dig_4):
  reverse = (dig_1*1000) + (dig_2*100) + (dig_3*10) + dig_4
  print("The reverse of ",x,"is : ",reverse)
def prdt_dig(dig_1,dig_2,dig_3,dig_4):
   evenpr=dig_1*dig_3
   oddpr=dig_2*dig_4
   print("Difference of the product: ",oddpr-evenpr)
x=int(input("Enter a 4 digit number : "))
d1,d2,d3,d4=digits(x)  
sum_dig(d1,d2,d3,d4)
reverse(d1,d2,d3,d4)
prdt_dig(d1,d2,d3,d4)
