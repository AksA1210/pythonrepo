# -*- coding: utf-8 -*-
"""Question1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Vkr-yE7qHldo8VamwnSRsluEJgl8XBo
"""

#1.Develop a program to read a four-digit number and find its:  
# a. Sum of digits   
# b. Reverse
# c. Difference between the product of digits at the odd position and the product of digits at the even position.
x=int(input("Enter a 4 digit number : "))
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

"""<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Test cases no.</th>
    <th class="tg-c3ow">                                                               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    Description                                                      </th>
    <th class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-c3ow">Expected Outcome</th>
    <th class="tg-c3ow">Actual Outcome</th>
    <th class="tg-0pky">&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1</td>
    <td class="tg-0pky"> Sum of digits </td>
    <td class="tg-0pky">1,2,3,4</td>
    <td class="tg-0pky">           10</td>
    <td class="tg-c3ow">10</td>
    <td class="tg-c3ow">     True</td>
  </tr>
  <tr>
    <td class="tg-0pky">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2</td>
    <td class="tg-0pky"> Sum of digits</td>
    <td class="tg-0pky">5,9,3,7</td>
    <td class="tg-0pky">             24</td>
    <td class="tg-0pky">          24</td>
    <td class="tg-c3ow">     True</td>
  </tr>
  <tr>
    <td class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3</td>
    <td class="tg-0lax"> Reverse of the number</td>
    <td class="tg-0lax">1234</td>
    <td class="tg-baqh">4321</td>
    <td class="tg-0lax">        4321</td>
    <td class="tg-baqh">     True</td>
  </tr>
  <tr>
    <td class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4</td>
    <td class="tg-0lax"> Reverse of the number</td>
    <td class="tg-0lax">5937</td>
    <td class="tg-0lax">            7395</td>
    <td class="tg-0lax">        7395</td>
    <td class="tg-baqh">     True</td>
  </tr>
  <tr>
    <td class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5</td>
    <td class="tg-0lax"> Difference between the products of the digits at the odd position and the product of the digits at the even position</td>
    <td class="tg-0lax">1234</td>
    <td class="tg-baqh"> -5</td>
    <td class="tg-0lax">          -5</td>
    <td class="tg-baqh">True</td>
  </tr>
  <tr>
    <td class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6</td>
    <td class="tg-0lax"> Difference between the products of the digits at the odd position and the product of the digits at the even position</td>
    <td class="tg-0lax">5937</td>
    <td class="tg-baqh">      -48</td>
    <td class="tg-baqh">    -48</td>
    <td class="tg-baqh"> True</td>
  </tr>
</tbody>
</table>
"""