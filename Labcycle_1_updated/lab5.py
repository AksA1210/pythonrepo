'''5. Develop a program to read a string and perform the following operations:

 • Print all possible substring
 • Print all possible substrings of length K
 • Print all possible substrings of length K with N distinct characters
 • Print all palindrome substrings'''





def substring(s):                    # To display all the possible substrings
  for i in range(len(s)):                    
    for j in range(i+1,len(s)+1):
      string=s[i:j]
      print(string)
  i=i+1
s=str(input("Enter string : "))    
a=substring(s)
def K_len():                        # To display those substrings whose length is K
  for i in range(len(s)):                    
    for j in range(i+1,len(s)+1):
      string=s[i:j]                     
      if len(string)==K:
        print(string)
K=int(input("Enter the length of the substring : "))    
Length=K_len()    


def K_Ndistinct():                    # To display those substrings whose length is K and has N distinct characters
  N=int(input("Enter the no: of distinct characters in the substring : "))
  for i in range(len(s)):                    
    for j in range(i+1,len(s)+1):
      string=s[i:j]        
      Set=set(string)
      if len(string)==K and len(Set)==N:
        print(string) 
      else:
        print("Substrings whose length is",K,"and which has",N,"distinct characters is absent")                 
K_Ndistinct()

def palindrome(s):                   #Palindrome
  for i in range(len(s)+1):                    
    for j in range(i+1,len(s)+1):
      string=s[i:j]    
      r=string[ : :-1]
      count=0  
      if (r==string):
        print(string,end="     ")
      count+=1  
  if count==0:
     print("No palindromes present ")
print("The palindrome strings are listed below : ")       
palindrome(s)
