string=input("Enter the list of numbers seperated by a space : ")
print(string)
list_num=list(string.split(" "))
print(list_num)
list_integers=[]
for i in list_num:
    list_integers.append(i)
print("The list of the integers : ",list_integers)
k=int(input("Enter the value by which the elements in the list is rotated to a position to the right"))
print("The list after rotating by ",k," positions to right is : ")
print(list_integers[-k:]+list_integers[:-k])
tuple_integers=tuple(list_integers)
print("Tuple : ",tuple_integers)
tuple_integers=tuple(set(tuple_integers))
print("Tuple with unique elements : ",tuple_integers)
print(tuple_integers)

square_integers=[]
for i in list_integers:
    square_integers.append((i**2)-i)
    s=(i**2)-i
print("Results of the function : ",square_integers)
sorted_list=list_integers_+square_integers
sorted_list.sort()
print("Sorted list : ",sorted_list)
