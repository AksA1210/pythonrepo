N=int(input("Enter the no: of months : "))
rabbit_pair=[1,1]
print("%10s"%"No : of months(N)","%20s""Number of pairs of rabbit")
print("***********************************************************")
for i in range(N):
    str1=str(i)
    str2=str(rabbit_pair[i,i])
    print("%10s"%str1,"%20s"%str2)
    rabbit_pair.append(rabbit_pair[i]+rabbit_pair[i+1])

      
