'''1. Suppose a newly born pair of rabbits, one male and one female, are put in a field. 
Rabbits can mate at the age of one month so that at the end of its second month, a female has produced another pair of rabbits.
 Suppose that our rabbits never die and that the female always produces one new pair every month from the second month. 
Develop a program to show a table containing the number of pairs of rabbits in the first N months.'''


N=int(input("Enter the no: of months(N) : "))
f0=1
f1=1
print("%10s"%"Number of months(N)","%20s"%"  Number of pairs of rabbit")
print("***********************************************************")
print("%10s"%"1","%20s"%"1")
print("%10s"%"2","%20s"%"1")
k=2
for i in range(N-2):
    f=f0+f1
    f0=f1
    f1=f
    print("%10d %20d"%(k+1,f))
    N=N+1
    i=i+1
    k=k+1
    

