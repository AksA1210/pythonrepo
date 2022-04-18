'''1.Develop a program to read a four-digit number and find its:  
 a. Sum of digits 
 b. Reverse
 c. Difference between the product of digits at the odd position and the product of digits at the even position.'''
 

def digits(x):
   dig_1=x%10
   dig_2=(x//10)%10
   dig_3=(x//100)%10
   dig_4=(x//1000)%10
   sum=dig_1+dig_2+dig_3+dig_4
   print("Sum of the digits of ",x,"is : ",sum)
   print("Reverse of ",x,"is :",dig_1,dig_2,dig_3,dig_4)
   evenpr=dig_1*dig_3
   oddpr=dig_2*dig_4
   print("Difference between the product of digits at the odd position and the product of digits at the even position: ",oddpr-evenpr)
x=int(input("Enter a 4 digit number : "))
digits(x)
