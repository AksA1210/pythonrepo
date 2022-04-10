# -*- coding: utf-8 -*-
"""Question 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XY-MR3aedhX5qlQRrcjOTSE0L74wb00C
"""

'''4.Develop a program to perform the following task:

 a. Define a function to check whether a number is happy or not.

 b. Define a function to print all happy numbers within a range.

 c. Define a function to print first N happy numbers.

 A happy number is a number defined by the following process:
 • Starting with any positive integer, replace the number with the sum of the squares of its digits.
 • Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
 • Those numbers for which this process ends in 1 are happy.

 Note: if a number is not being happy after 100 iterations, consider it sad.'''

def ishappy(x):     # To check whether the number is happy or not
  n=x
  for i in range(0,100):
    sum=0
    while n!=0:
      r=n%10
      sum=sum+(r*r)
      n=n//10
      if (sum==1):
       return True
      else:
       return False

x=int(input("Enter a number : "))
if ishappy(x)==True:
  print("Happy")       
else:
  print("Sad") 

  

def _range():       # To print the happy numbers present between a range
  m=int(input("Enter the lower limit : "))
  n=int(input("Enter the upper limit : "))
  print("The list of happy numbers from",m,"to",n,"is displayed below : ")
  for i in range(m,n+1):
    if ishappy(i)==True:
      print(i)
_range()      
   
def firstN():      # To print the first N happy numbers
  N=int(input("Enter the limit : "))
  j=1
  print("The first",N,"happy numbers are as follows : ")
  while (N!=0):
    if ishappy(j)==True:
      print(j)
      N=N-1
    j=j+1
firstN()

"""<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Test cases no.</th>
    <th class="tg-0pky">                                                               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    Description                                                      </th>
    <th class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0pky">Expected Outcome</th>
    <th class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Actual Outcome</th>
    <th class="tg-0pky">&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1</td>
    <td class="tg-0pky"> Check whether the inputted number is a happy number or not</td>
    <td class="tg-0pky">  &nbsp;&nbsp;123</td>
    <td class="tg-0pky">            Sad</td>
    <td class="tg-0pky">                 Sad</td>
    <td class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;True</td>
  </tr>
  <tr>
    <td class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2</td>
    <td class="tg-0pky"> Check whether the inputted number is a happy number or not</td>
    <td class="tg-0pky"> &nbsp;&nbsp; 171</td>
    <td class="tg-0pky">            Happy</td>
    <td class="tg-0pky">                Happy</td>
    <td class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;True</td>
  </tr>
</tbody>
</table>
"""