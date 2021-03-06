'''Write a program to read a string containing numbers separated by a space and convert it as a list of integers. 
Perform the following operations on it.
3.Rotate elements in a list by 'k' position to the right
4.Convert the list into a tuple using list comprehension
5.Remove all duplicates from the tuple and convert them into a list again.
6.Create another list by putting the results of the evaluation of the function f(x) = (x^2) – x with each element in the final list

5.After sorting them individually, merge the two lists to create a single sorted list.
'''

string=input("Enter the list of numbers seperated by a space : ")
print(string)
list_num=list(string.split(" "))
list_num.pop()
print(list_num)
list_integers=[]
for i in list_num:
    list_integers.append(int(i))
print("The list of the integers : ",list_integers)
print()
k=int(input("Enter the value by which the elements in the list is shifted to a position to the right : "))
print("The list after rotating by ",k," positions to the right is : ")
print(list_integers[-k:]+list_integers[:-k])
print()
tuple_integers=tuple(list_integers)
print("Tuple : ",tuple_integers)
tuple_integers=tuple(set(tuple_integers))
print("Tuple with unique elements : ",tuple_integers)
print()
square_integers=[]
for i in list_integers:
    sq=i**2
    sq=sq-i
    square_integers.append(sq)
    
print("Results of the function : ",square_integers)
sorted_list=list_integers+square_integers
sorted_list.sort()
print("Sorted list : ",sorted_list)

