# -*- coding: utf-8 -*-
"""Lab_cycle_2_Q_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1khncHBApDKwACdYTxfqC0r7OTLqSF7XM
"""

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